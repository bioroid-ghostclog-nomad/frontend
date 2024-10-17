import streamlit as st

from api import check_username, join

st.markdown(
    """
# 회원가입
"""
)

access_token = st.session_state.get("access")
refresh_token = st.session_state.get("refresh")
if access_token:
    # 만약 액세스 토큰 있으면 채팅 페이지로 이동
    st.switch_page("pages/Chat.py")


with st.form("join_form", enter_to_submit=False):

    # 아이디
    username_col1, username_col2 = st.columns(2, vertical_alignment="bottom")
    is_username_valid = st.session_state.get("is_username_valid", False)
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
        st.session_state["is_username_valid"] = check_username(username)

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
