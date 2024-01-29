import streamlit as st
import os
import requests
###################################
# streamlit run home.py 로 실행
###################################
def main():
    # Set page config
    st.set_page_config(
        page_title="학생 플랫폼",
        layout="wide",
    )

    st.title("학생들을 위한 종합 플랫폼")

    st.markdown("")

    # Add some sections or features
    
    st.header("지원 사항")
    st.markdown("### 초등학생 일기 검사")
    st.markdown("### 심리 상담")
    st.markdown("### 연애 편지 작성")
    st.markdown("### PDF기반 문제 생성")
    st.markdown("### 프롬프트 기반 그림동화 생성")
    st.markdown("### 직업 추천")
    st.markdown("### 자료 분석체험")
    st.markdown("---")
    st.caption("Made by MSAISCHOOL 3rd 2team")
    # Open ai key
    st.markdown("---")
    st.markdown("## 오픈 AI API key를 입력해주세요.")
    openai_key = st.text_input('OPEN_AI_API_KEY',type="password")
    return openai_key
    
def is_openai_key_valid(openai_key):
    url = "https://api.openai.com/v1/models/gpt-3.5-turbo-instruct"

    headers = {
        "Authorization": f"Bearer {openai_key}"
    }

    response = requests.get(url, headers=headers)

    data = response.json()
    if "error" in data:
        return False
    else:
        return True

openai_key = main()

#처음에 들어올 때 유효하지 않은 키 저장
os.environ['OPENAI_KEY'] = '1'
if openai_key:
    # Check the validity of the API key
    is_valid = is_openai_key_valid(openai_key=openai_key)
    if is_valid == True:
        st.write("오픈 AI API 키 인증 완료")
        os.environ['OPENAI_KEY'] = openai_key
    else:
        st.write("잘못된 API 키입니다")
        os.environ['OPENAI_KEY'] = '1'



        
