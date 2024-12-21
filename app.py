import streamlit as st
import openai

# OpenAI API 키 설정
openai.api_key = "your_openai_api_key"

# 스트림릿 웹 앱 구성
st.title("ChatGPT 기반 네임 컬러 테라피 상담 앱")
st.write("사용자의 질문에 대해 응답하는 GPT 기반 상담 서비스입니다.")

# 사용자 입력창
user_input = st.text_area("질문을 입력하세요:", placeholder="질문을 입력하거나 상담 내용을 입력하세요.")

# 버튼 클릭 시 ChatGPT 응답 호출
if st.button("응답 받기"):
    if user_input.strip() == "":
        st.warning("질문을 입력해 주세요!")
    else:
        with st.spinner("응답 생성 중..."):
            try:
                # OpenAI API 호출
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": user_input}
                    ]
                )
                # 응답 표시
                answer = response['choices'][0]['message']['content']
                st.success("응답 생성 완료!")
                st.text_area("GPT 응답:", value=answer, height=200, disabled=True)
            except Exception as e:
                st.error(f"응답 생성 중 오류 발생: {str(e)}")

# 주의 사항 또는 추가 설명
st.info("이 앱은 네임 컬러 테라피에 기반한 상담을 제공합니다. 전문적인 조언이 필요할 경우 전문가에게 문의하세요.")
