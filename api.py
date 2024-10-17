import streamlit as st
import requests
import time

# BASE_URL = "http://14.56.184.4:8000/"
BASE_URL = "http://localhost:8000/"


def join(username, email, password, password_check, is_username_valid):
    if not username:
        st.error("아이디를 입력하세요.")
        return
    if not is_username_valid:
        st.error("아이디 중복 검사를 다시 진행해 주세요.")
        return
    if not email:
        st.error("이메일을 입력하세요.")
        return
    if not password:
        st.error("비밀번호를 입력하세요.")
        return
    if not password_check:
        st.error("비밀번호 확인란을 입력하세요.")
        return
    if password != password_check:
        st.error("비밀번호가 일치하지 않습니다.")
        return

    response = requests.post(
        f"{BASE_URL}api/v1/users/userdata/",
        data={"username": username, "password": password, "email": email},
    )
    if response.status_code == 201:
        st.success("회원 가입 성공! 로그인 화면으로 이동합니다.")
        time.sleep(1)
        st.switch_page("pages/Login.py")
    else:
        st.error("회원 가입에 실패했습니다. 다시 시도해주세요.")


def login(username, password):
    if not username:
        st.error("아이디를 입력하세요.")
        return
    if not password:
        st.error("비밀번호를 입력하세요.")
        return

    response = requests.post(
        f"{BASE_URL}api/v1/users/login/",
        data={"username": username, "password": password},
    )
    if response.status_code == 200:
        st.success("로그인 성공!")
        print(response.json())
        time.sleep(1)
        st.session_state["access"] = response.json()["access"]
        st.session_state["refresh"] = response.json()["refresh"]
        st.switch_page("pages/Chat.py")
    else:
        st.error("로그인 실패. 아이디 혹은 비밀번호를 재확인해주세요.")


def check_username(username):

    response = requests.post(
        f"{BASE_URL}api/v1/users/Idchk/",
        data={"username": username},
    )
    if response.json()["response"] != "중복 아이디입니다.":
        is_username_valid = True
        st.success(response.json()["response"], icon="✅")
    else:
        is_username_valid = False
        st.error(response.json()["response"], icon="❌")
    return is_username_valid


def get_user_info(user_id):
    response = requests.get(f"{BASE_URL}api/v1/users/{user_id}")
    return response.json(), response.status_code
