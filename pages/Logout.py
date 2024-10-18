import streamlit as st


access_token = st.session_state.get("access")
refresh_token = st.session_state.get("refresh")
if access_token:
    del st.session_state["access"]
    del st.session_state["refresh"]

st.switch_page("pages/Login.py")