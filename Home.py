import streamlit as st

st.set_page_config(
    page_title="PDF Chatbot",
    page_icon="🤖",
)

pages = {
    "계정": [
        st.Page("pages/Login.py", title="로그인"),
        st.Page("pages/Join.py", title="회원가입"),
        st.Page("pages/Me.py", title="내 정보"),
        st.Page("pages/PasswordCheck.py", title="비밀번호 확인"),
        st.Page("pages/Logout.py", title="로그아웃"),
    ],
    "채팅": [
        st.Page("pages/CreateConversation.py", title="대화 생성"),
        st.Page("pages/Conversations.py", title="대화 목록"),
        st.Page("pages/Conversation.py", title="대화"),
    ],
}


def set_conversation_id(conversation_id):
    st.session_state["conversation_id"] = conversation_id
    st.switch_page("pages/Conversation.py")


if "access" in st.session_state:
    # 로그인 시

    with st.sidebar:
        new_conversation = st.button("새 대화 생성")

        # 대화 목록
        conversations = [
            {"title": "대화 1" * 100, "id": "1"},
            {"title": "대화 2", "id": "2"},
            {"title": "대화 3", "id": "3"},
        ]

        for conversation in conversations:
            button = st.button(
                (
                    conversation["title"]
                    if len(conversation["title"]) < 20
                    else conversation["title"][:20] + "..."
                ),
                key=conversation["id"],
            )
            if button:
                set_conversation_id(conversation["id"])

pg = st.navigation(pages)
pg.run()
