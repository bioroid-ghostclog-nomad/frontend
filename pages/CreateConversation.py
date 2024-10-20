import streamlit as st
from api import check_api
st.markdown(
    """
# 대화 생성하기
"""
)

check_api()

access_token = st.session_state.get("access")
refresh_token = st.session_state.get("refresh")

if not access_token:
    # 만약 액세스 토큰 없으면 로그인 페이지로 이동
    st.switch_page("pages/Login.py")

with st.form("conversation_form"):
    title = st.text_input(
        "대화 제목",
        placeholder="대화의 제목을 입력해주세요.",
    )
    model = st.selectbox(
        "모델을 선택해 주세요.",
        (
            "gpt-4",
            "gpt-4-turbo",
            "gpt-4o",
            "gpt-4o-mini",
        ),
    )
    pdf = st.file_uploader(
        "PDF 업로드",
        type=["pdf"],
    )
    submitted = st.form_submit_button(
        "대화 생성하기",
    )
    if submitted:
        pass
