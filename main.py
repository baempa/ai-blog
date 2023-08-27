# 실행 streamlit run main.py
# 필요한 라이브러리를 임포트합니다.
from dotenv import load_dotenv  # 환경 변수 로드를 위한 라이브러리
load_dotenv()
import streamlit as st  # Streamlit을 사용하여 웹 어플리케이션을 만듭니다.
from langchain.chat_models import ChatOpenAI  # 대화 모델을 사용하기 위한 라이브러리
import time  # 시간 지연을 위한 라이브러리

# ChatOpenAI 모델을 초기화합니다.
chat_model = ChatOpenAI()

# 웹 어플리케이션의 제목을 설정합니다.
st.title('AI 블로그 도우미')

# 사용자로부터 주제를 입력받는 입력 상자를 생성합니다.
content = st.text_input('주제를 제시해주세요.')

# "시 작성 요청하기" 버튼을 생성합니다.
if st.button('글 작성 요청하기'):
    with st.spinner('글 작성 중...'):  # 스피너를 표시하여 작업 진행 중임을 알립니다.
        result = chat_model.predict(content + "에 대한 블로그 글을 작성해")  # 모델을 사용하여 시를 생성합니다.
        st.empty()  # 이전 출력을 비웁니다.

        text_element = st.empty()  # 결과를 표시할 빈 공간을 생성합니다.
        for char in result:
            text_element.text(result[:result.index(char)+1])  # 글자가 한 글자씩 추가되도록 텍스트를 업데이트합니다.
            time.sleep(0.05)  # 글자가 한 글자씩 나타나도록 0.05초의 딜레이를 추가합니다.
