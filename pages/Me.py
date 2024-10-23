import streamlit as st
import jwt, os
from dotenv import load_dotenv

from api import (
    change_password,
    check_password,
    get_my_info,
    put_my_info,
    regist_api_key,
)


st.markdown(
    """
# 내 정보
"""
)

load_dotenv()

access_token = st.session_state.get("access")
refresh_token = st.session_state.get("refresh")

if not access_token:
    # 만약 액세스 토큰 없으면 로그인 페이지로 이동
    st.switch_page("pages/Login.py")

pwd_checked = st.session_state.get("pwd_checked")
if not pwd_checked:
    # 만약 비밀번호 확인 하지 않으면 비밀번호 확인 페이지로
    st.switch_page("pages/PasswordCheck.py")

token = jwt.decode(
    access_token,
    key=os.getenv("SECRET_KEY"),
    algorithms=["HS256"],
)
data, status_code = get_my_info()

if status_code != 200:
    st.error("유저를 찾을 수 없습니다.")
    del st.session_state.access
    del st.session_state.refresh
    st.switch_page("pages/Login.py")

with st.form("myinfo_form", enter_to_submit=False):

    username = st.text_input(
        "아이디",
        value=data["username"],
        placeholder="아이디를 입력하세요",
        max_chars=20,
        help="아이디는 수정할 수 없습니다.",
        disabled=True,
    )
    email = st.text_input(
        "이메일",
        value=data["email"],
        placeholder="이메일을 입력하세요",
        max_chars=50,
        help="이메일",
    )
    submitted = st.form_submit_button(
        "수정하기",
    )
    if submitted:
        put_my_info(email)

with st.form("password_form", enter_to_submit=False):

    old_password = st.text_input(
        "현재 비밀번호",
        placeholder="현재 비밀번호를 입력하세요",
        max_chars=20,
        help="현재 비밀번호",
        type="password",
    )
    new_password = st.text_input(
        "새 비밀번호",
        placeholder="새 비밀번호를 입력하세요",
        max_chars=20,
        help="새 비밀번호",
        type="password",
    )
    new_password_check = st.text_input(
        "새 비밀번호 확인",
        placeholder="다시 새 비밀번호를 입력하세요",
        max_chars=20,
        type="password",
        help="새 비밀번호를 다시 확인합니다.",
    )
    password_submitted = st.form_submit_button(
        "수정하기",
    )
    if password_submitted:
        change_password(old_password, new_password, new_password_check)

with st.form("regist_api_key", enter_to_submit=False):

    api_key = st.text_input(
        "API key",
        placeholder="api를 입력해주세요.",
        help="API key",
    )
    submitted = st.form_submit_button(
        "변경하기",
    )
    if api_key:
        if submitted:
            response, status = regist_api_key(api_key)
        if status == 201:
            st.success(response["response"])
        elif status == 400:
            st.warning(response["response"])
