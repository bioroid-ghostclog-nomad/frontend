import time
import streamlit as st
from langchain.memory import ConversationBufferMemory

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

llm_answer = """
Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""


def stream_data():
    for word in llm_answer.split(" "):
        yield word + " "
        time.sleep(0.02)


def save_message(message, role):
    st.session_state["messages"].append({"message": message, "role": role})


def send_message(message, role, save=True):
    with st.chat_message(role):
        st.markdown(message)
    if save:
        save_message(message, role)


def paint_history():
    for message in st.session_state["messages"]:
        send_message(
            message["message"],
            message["role"],
            save=False,
        )


def format_docs(docs):
    return "\n\n".join(document.page_content for document in docs)


def get_history(input):
    return memory.load_memory_variables({})["history"]


if "memory" not in st.session_state:
    memory = ConversationBufferMemory(return_messages=True)
    st.session_state["memory"] = memory
else:
    memory = st.session_state["memory"]

chat = st.chat_input("채팅할 내용을 입력하세요")
if chat:
    with st.chat_message("human"):
        st.markdown(chat)
    time.sleep(1)
    with st.chat_message("ai"):
        st.write_stream(stream_data)
