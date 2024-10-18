import streamlit as st
import jwt, os
from dotenv import load_dotenv

from api import get_my_info, put_my_info


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

token = jwt.decode(
    access_token,
    key=os.getenv("SECRET_KEY"),
    algorithms=["HS256"],
)
data, status_code = get_my_info()

if status_code != 200:
    st.error("유저를 찾을 수 없습니다.")
    del st.session_state["access"]
    del st.session_state["refresh"]
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
        updated_data, updated_status_code = put_my_info(email)
        print(updated_status_code)
