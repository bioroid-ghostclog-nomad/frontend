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

pg = st.navigation(pages)
pg.run()
