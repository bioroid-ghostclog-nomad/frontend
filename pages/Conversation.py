import streamlit as st
import langchain

st.markdown(
    """
# 대화
"""
)

access_token = st.session_state.get("access")
refresh_token = st.session_state.get("refresh")

if not access_token:
    # 만약 액세스 토큰 없으면 로그인 페이지로 이동
    st.switch_page("pages/Login.py")

conversation_id = st.session_state.get("conversation_id")

st.query_params["conversation_id"] = conversation_id

with st.chat_message("ai"):
    st.markdown("안녕하세요! 어떻게 도와드릴까요?")


chat = st.chat_input("채팅할 내용을 입력하세요")
if chat:
    with st.chat_message("human"):
        st.markdown(chat)
