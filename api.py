import streamlit as st
import requests
import time

# BASE_URL = "http://14.56.184.4:8000/"
BASE_URL = "http://localhost:8000/"


def join(username, email, password, password_check, is_username_valid, email_chk):
    if not username:
        st.error("아이디를 입력하세요.")
        return
    if not is_username_valid:
        st.error("아이디 중복 검사를 다시 진행해 주세요.")
        return
    if not email:
        st.error("이메일을 입력하세요.")
        return
    if not email_chk:
        st.error("이메일 인증을 진행해주세요.")
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
        f"{BASE_URL}api/v1/users/userdata",
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
        f"{BASE_URL}api/v1/users/login",
        data={"username": username, "password": password},
    )
    if response.status_code == 200:
        st.success("로그인 성공!")
        time.sleep(1)
        st.session_state["access"] = response.json()["access"]
        st.session_state["refresh"] = response.json()["refresh"]
        st.switch_page("pages/CreateConversation.py")
    else:
        st.error("로그인 실패. 아이디 혹은 비밀번호를 재확인해주세요.")


def check_username(username):

    response = requests.post(
        f"{BASE_URL}api/v1/users/Idchk",
        data={"username": username},
    )
    if response.json()["response"] != "중복 아이디입니다.":
        is_username_valid = True
        st.success(response.json()["response"], icon="✅")
    else:
        is_username_valid = False
        st.error(response.json()["response"], icon="❌")
    return is_username_valid


def check_email(email, flag, code=""):
    if flag:  # 인증코드 검사
        response = requests.delete(
            f"{BASE_URL}api/v1/users/email",
            data={"email": email, "code": code},
        )
        return response.json()["response"]
    else:  # 인증 코드 보내기
        response = requests.post(
            f"{BASE_URL}api/v1/users/email",
            data={"email": email},
        )
        response_data = response.json()["response"]
        if response_data == "success":
            return True
        elif response_data == "fail":
            return False


def get_my_info():
    response = requests.get(
        f"{BASE_URL}api/v1/users/me",
        data={
            "access": st.session_state.get("access"),
            "refresh": st.session_state.get("refresh"),
        },
        headers={"Authorization": f"Bearer {st.session_state.get('access')}"},
    )
    return response.json(), response.status_code


def put_my_info(email):
    if not email:
        st.error("이메일을 입력하세요.")
        return
    response = requests.put(
        f"{BASE_URL}api/v1/users/me",
        data={
            "access": st.session_state.get("access"),
            "refresh": st.session_state.get("refresh"),
            "email": email,
        },
        headers={"Authorization": f"Bearer {st.session_state.get('access')}"},
    )


def check_password(password):
    if not password:
        st.error("비밀번호를 입력하세요.")
        return
    response = requests.post(
        f"{BASE_URL}api/v1/users/password",
        data={
            "access": st.session_state.get("access"),
            "refresh": st.session_state.get("refresh"),
            "password": password,
        },
        headers={"Authorization": f"Bearer {st.session_state.get('access')}"},
    )
    if response.status_code == 200:
        st.session_state["pwd_checked"] = True
        st.switch_page("pages/Me.py")
    elif response.status_code == 403:
        st.error("비밀번호가 틀렸습니다.")
    elif response.status_code == 400:
        st.error("비밀번호를 입력하세요.")
    else:
        st.error("알 수 없는 에러")


def change_password(old_password, new_password, new_password_check):
    if not old_password:
        st.error("현재 비밀번호를 입력하세요.")
        return
    if not new_password:
        st.error("새 비밀번호를 입력하세요.")
        return
    if not new_password_check:
        st.error("새 비밀번호 확인란을 입력하세요.")
        return
    if new_password != new_password_check:
        st.error("새 비밀번호가 일치하지 않습니다.")
        return
    response = requests.put(
        f"{BASE_URL}api/v1/users/password",
        data={
            "access": st.session_state.get("access"),
            "refresh": st.session_state.get("refresh"),
            "old_password": old_password,
            "new_password": new_password,
        },
        headers={"Authorization": f"Bearer {st.session_state.get('access')}"},
    )
    if response.status_code == 200:
        st.success("비밀번호가 수정되었습니다.")
    elif response.status_code == 403:
        st.error("비밀번호가 틀렸습니다.")
    elif response.status_code == 400:
        st.error("현재 비밀번호 또는 새 비밀번호를 확인해주세요.")
    else:
        st.error("알 수 없는 에러")


def regist_api_key(api_key):
    response = requests.post(
        f"{BASE_URL}api/v1/users/apikey",
        data={
            "access": st.session_state.get("access"),
            "refresh": st.session_state.get("refresh"),
            "api_key": api_key,
        },
        headers={"Authorization": f"Bearer {st.session_state.get('access')}"},
    )
    return response.json(), response.status_code

def check_api():
    response = requests.get(
        f"{BASE_URL}api/v1/users/apikey",
        data={
            "access": st.session_state.get("access"),
            "refresh": st.session_state.get("refresh"),
        },
        headers={"Authorization": f"Bearer {st.session_state.get('access')}"},
    )

    result = response.json()["response"]
    if result == "success":
        return
    elif result == "fail":
        return st.switch_page("pages/Me.py")

def create_conversation(title,pdf,model):
    if not title:
        st.error("제목을 입력하세요.")
        return
    if not pdf:
        st.error("PDF 파일을 업로드하세요.")
        return

    response = requests.post(
        f"{BASE_URL}api/v1/chating/chatingroom",
        data={
            "access": st.session_state.get("access"),
            "refresh": st.session_state.get("refresh"),
            "title": title,
            "model": model,
        },
        headers={"Authorization": f"Bearer {st.session_state.get('access')}"},
        files={"pdf": pdf},
    )
    result = response.json()["response"]
    if result == "fail":
        st.warning("에러가 발생했습니다.")
    elif result == "success":
        st.warning("PDF 분석 완료. 챗봇을 생성합니다.")
    return
