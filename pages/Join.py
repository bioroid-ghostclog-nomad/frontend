import json
import time
import streamlit as st
import requests

st.markdown(
    """
# 회원가입
"""
)

BASE_URL = "http://14.56.184.4:8000/"


def join(username, email, password, password_check, is_username_valid):
    if not username:
        st.error("아이디를 입력하세요.")
        return
    if not is_username_valid:
        st.error("아이디 중복 검사를 다시 진행해 주세요.")
        return
    if not email:
        st.error("이메일을 입력하세요.")
        return
    if not password:
        st.error("비밀번호를 입력하세요.")
        return
    if not password_check:
        st.error("비밀번호 확인란을 입력하세요.")
        return
    if password != password_check:
        st.error("비밀번호가 일치하지 않습니다.")
        return

    response = requests.post(
        f"{BASE_URL}api/v1/users/regist/",
        data={"username": username, "password": password, "email": email},
    )
    if response.status_code == 201:
        st.success("회원 가입 성공! 로그인 화면으로 이동합니다.")
        time.sleep(1)
        st.switch_page("pages/Login.py")
    else:
        st.error("회원 가입에 실패했습니다. 다시 시도해주세요.")


with st.form("join_form", enter_to_submit=False):

    # 아이디
    username_col1, username_col2 = st.columns(2, vertical_alignment="bottom")
    is_username_valid = False
    with username_col1:
        username = st.text_input(
            "아이디",
            placeholder="아이디를 입력하세요",
            max_chars=20,
            help="아이디",
        )
    with username_col2:
        username_checked = st.form_submit_button(
            "중복 확인",
        )
    if username_checked:
        # 중복 확인
        response = requests.post(
            f"http://14.56.184.4:8000/api/v1/users/Idchk/",
            data={"username": username},
        )
        if response.json()["response"] != "중복 아이디입니다.":
            is_username_valid = True
            st.success(response.json()["response"], icon="✅")
        else:
            is_username_valid = False
            st.error(response.json()["response"], icon="❌")

    # 이메일
    email = st.text_input(
        "이메일",
        placeholder="이메일을 입력하세요",
        max_chars=50,
        help="이메일",
    )

    # 비밀번호
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
    if submitted:
        join(username, email, password, password_check, is_username_valid)
