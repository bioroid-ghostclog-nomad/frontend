import streamlit as st

st.markdown(
    """
# 회원가입
"""
)


with st.form("join_form", enter_to_submit=False):
    username = st.text_input(
        "아이디",
        placeholder="아이디를 입력하세요",
        max_chars=20,
        help="아이디",
    )
    username_checked = st.form_submit_button(
        "중복 확인",
    )
    password = st.text_input(
        "비밀번호",
        placeholder="비밀번호를 입력하세요",
        max_chars=20,
        type="password",
        help="비밀번호",
    )
    password_check = st.text_input(
        "비밀번호 확인",
        placeholder="다시 비밀번호를 입력하세요",
        max_chars=20,
        type="password",
        help="비밀번호를 다시 확인합니다.",
    )
    submitted = st.form_submit_button(
        "회원가입",
    )
