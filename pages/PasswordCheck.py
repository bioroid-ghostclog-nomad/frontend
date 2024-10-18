import streamlit as st
import jwt, os
from dotenv import load_dotenv

from api import check_password, get_my_info


st.markdown(
    """
# 비밀번호 확인
"""
)

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

with st.form("password_form", enter_to_submit=False):

    password = st.text_input(
        "비밀번호",
        placeholder="비밀번호를 입력하세요",
        max_chars=20,
        type="password",
        help="비밀번호",
    )
    submitted = st.form_submit_button(
        "확인",
    )
    if submitted:
        check_password(password)
