import streamlit as st

st.set_page_config(
    page_title="PDF Chatbot",
    page_icon="🤖",
)

pages = {
    "계정": [
        st.Page("pages/Login.py", title="로그인"),
        st.Page("pages/Join.py", title="회원가입"),
    ]
}

pg = st.navigation(pages)
pg.run()
