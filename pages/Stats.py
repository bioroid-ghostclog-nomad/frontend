import streamlit as st
import pandas as pd
import numpy as np

st.markdown(
    """
# 통계
"""
)

# 사용 통계
## 메세지 수
messages_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(messages_data)

## 대화 수
conversation_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(conversation_data)
## 파일 수
files_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(files_data)

# 비용 분석
## 대화 당 사용된 토큰 수
## 대화의 총 비용
