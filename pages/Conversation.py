import time
import streamlit as st
from langchain.memory import ConversationBufferMemory

from api import get_messages, post_message

st.markdown(
    """
# AI와 대화하기

챗봇과 대화를 시작해보세요!
"""
)

access_token = st.session_state.get("access")
refresh_token = st.session_state.get("refresh")

if not access_token:
    # 만약 액세스 토큰 없으면 로그인 페이지로 이동
    st.switch_page("pages/Login.py")

conversation_id = st.session_state.get("conversation_id")

st.query_params["conversation_id"] = conversation_id

response = get_messages(conversation_id)
messages = response
for msg in messages:
    with st.chat_message(msg["speaker"]):
        st.markdown(msg["chat"])


def stream_data(ai_message):
    for word in ai_message.split(" "):
        yield word + " "
        time.sleep(0.02)


chat = st.chat_input("채팅할 내용을 입력하세요")
if chat:
    with st.chat_message("human"):
        st.markdown(chat)

    response = post_message(conversation_id, chat)
    if response.status_code == 200:
        with st.chat_message("ai"):
            ai_message = response.json()["ai_message"]
            stream = stream_data(ai_message)
            st.write_stream(stream)
    else:
        st.error("채팅을 저장하는데 실패했습니다.")
