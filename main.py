import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.title('AI BLOG')

content = st.text_input('주제를 제시하면 AI가 글을 씁니다.')

if st.button('작성 요청'):
    with st.spinner('작성 중...'):
        result = chat_model.predict(content + "을 주제로 기사를 써")
        st.write(result)
