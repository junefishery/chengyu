# 导入pyperclip模块，以及你之前的代码
import pyperclip
import streamlit as st
import random

with open("chengyu.txt", "r", encoding="utf-8") as f:
    chengyu_list = f.read().splitlines()

# 创建一个标题
st.title("随机成语生成器")

# 创建一个滑动条
num = st.slider("请选择要生成的成语的数量", 1, 10)

# 随机抽取成语
random_chengyu = random.sample(chengyu_list, num)

# 输出生成的成语
st.write("生成的成语如下：")
st.markdown(", ".join(random_chengyu))

# 创建一个复制按钮
copy_button = st.button("复制成语")

# 输出一些提示信息
st.write("请点击复制按钮，然后在其他地方粘贴")

# 判断用户是否点击了复制按钮
if copy_button:
    # 复制生成的成语列表
    pyperclip.copy(", ".join(random_chengyu))
    # 输出一些成功信息
    st.success("已复制到剪贴板")
