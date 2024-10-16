import streamlit as st

st.markdown(
    """
# 로그인
"""
)


with st.form("login_form"):
    username = st.text_input(
        "아이디",
        placeholder="아이디를 입력하세요",
        max_chars=20,
        help="아이디",
    )
    password = st.text_input(
        "비밀번호",
        placeholder="비밀번호를 입력하세요",
        max_chars=20,
        type="password",
        help="비밀번호",
    )
    submitted = st.form_submit_button(
        "로그인",
    )
