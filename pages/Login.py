import streamlit as st

from api import login

st.markdown(
    """
# 로그인
"""
)

access_token = st.session_state.get("access")
refresh_token = st.session_state.get("refresh")
if access_token:
    # 만약 액세스 토큰 있으면 채팅 페이지로 이동
    st.switch_page("pages/Chat.py")

if "pwd_checked" in st.session_state:
    del st.session_state["pwd_checked"]

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
    if submitted:
        login(username, password)
