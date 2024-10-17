import time
import streamlit as st
import requests, json

st.markdown(
    """
# 로그인
"""
)

BASE_URL = "http://14.56.184.4:8000/"


def login(username, password):
    if not username:
        st.error("아이디를 입력하세요.")
        return
    if not password:
        st.error("비밀번호를 입력하세요.")
        return

    response = requests.post(
        f"{BASE_URL}api/v1/users/login/",
        data={"username": username, "password": password},
    )
    if response.status_code == 200:
        st.success(response.json())
        time.sleep(1)
        st.switch_page("pages/Chat.py")
    else:
        st.error("로그인 실패. 아이디 혹은 비밀번호를 재확인해주세요.")


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
