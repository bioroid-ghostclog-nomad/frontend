import json
import streamlit as st
import pandas as pd
import numpy as np

from api import get_stats

st.markdown(
    """
# 통계
"""
)
datas = get_stats()
conversations_num = len(datas)
st.markdown(
    f"""
### 대화 수: {conversations_num}
"""
)

inputs = []
outputs = []
totals = []
titles = []
data_list = []


for data in datas:
    # 사용 통계
    ## 메세지 수
    messages_num = data["messages_num"]
    title = data["title"]
    tokens = data["tokens"]
    input_tokens = tokens["input_tokens__sum"]
    output_tokens = tokens["output_tokens__sum"]
    total_tokens = tokens["total_tokens__sum"]

    inputs.append(input_tokens)
    outputs.append(output_tokens)
    totals.append(total_tokens)
    titles.append(title)
    data_list.append([messages_num, input_tokens, output_tokens, total_tokens])

    tokens_data = pd.DataFrame(
        [input_tokens, output_tokens, total_tokens],
        index=[
            "input",
            "output",
            "total",
        ],
    )
    st.bar_chart(tokens_data, x_label=data["title"], y_label="토큰 수")

df = pd.DataFrame(
    data_list,
    index=titles,
    columns=["메세지 수", "입력(프롬프트) 토큰 수", "출력 토큰 수", "총 토큰 수"],
)
st.table(df)
