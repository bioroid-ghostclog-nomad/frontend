import streamlit as st
import jwt, os
from dotenv import load_dotenv

from api import get_user_info


st.markdown(
    """
# 내 정보
"""
)

# BASE_URL = "http://14.56.184.4:8000/"
BASE_URL = "http://localhost:8000/"

load_dotenv()

access_token = st.session_state.get("access")
refresh_token = st.session_state.get("refresh")

if not access_token:
    # 만약 액세스 토큰 없으면 로그인 페이지로 이동
    st.switch_page("pages/Login.py")

token = jwt.decode(
    access_token,
    key=os.getenv("SECRET_KEY"),
    algorithms=["HS256"],
)
user_id = token["user_id"]
data, status_code = get_user_info(user_id)

if status_code != 200:
    st.error("유저를 찾을 수 없습니다.")
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
        "수정하기",
    )
