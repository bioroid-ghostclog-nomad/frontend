import streamlit as st
from api import get_conversations,delete_conversations

st.markdown(
    """
# 대화 목록
"""
)


access_token = st.session_state.get("access")
refresh_token = st.session_state.get("refresh")

if not access_token:
    # 만약 액세스 토큰 없으면 로그인 페이지로 이동
    st.switch_page("pages/Login.py")

if st.button("대화 만들기"):
    st.switch_page("pages/CreateConversation.py")

# 초기 상태 설정
if 'show_modal' not in st.session_state:
    st.session_state.show_modal = False  # 모달 표시 여부

# 모달 창을 열기 위한 함수
def open_modal():
    st.session_state.show_modal = True

# 모달 창을 닫기 위한 함수
def close_modal():
    st.session_state.show_modal = False

if st.button("대화 모두 삭제하기"):
    open_modal()

if st.session_state.show_modal:
    st.write('**정말로 모든 대화들을 삭제하시겠습니까?**')
    
    # 확인 버튼
    if st.button('네, 전부 삭제합니다.'):
        delete_conversations()
        close_modal()
    
    # 취소 버튼
    if st.button('아니요. 다시 생각하겠습니다.'):
        close_modal()
    

chats = get_conversations()
st.write("") # 줄 내림용
if len(chats) == 0:  
    st.warning("생성된 대화가 존재하지 않습니다.")
else:
    st.success("하단에서 대화를 선택하세요.")
    st.write("") # 줄 내림용
    for chat in chats:
        if st.button(chat["title"]):
            st.session_state.conversation_id = chat["id"]
            st.switch_page("pages/Conversation.py")