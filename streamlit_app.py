import streamlit as st
import pandas as pd
import time

st.title("Streamlit 주요 UI 요소 예시")  # 페이지 제목

st.header("텍스트 요소")  # 텍스트 관련 요소
st.write("이것은 일반 텍스트입니다.")  # 일반 텍스트
st.markdown("**마크다운 텍스트**")  # 마크다운 지원
st.code("print('Hello, Streamlit!')", language='python')  # 코드 블록
st.caption("캡션: 설명이나 부가 텍스트")  # 캡션

st.header("데이터 표시")  # 데이터프레임, 테이블 등
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
st.dataframe(df)  # 동적 데이터프레임
st.table(df)  # 정적 테이블

st.header("입력 위젯")  # 사용자 입력 요소
name = st.text_input("이름을 입력하세요")  # 텍스트 입력
age = st.number_input("나이", min_value=0, max_value=120)  # 숫자 입력
agree = st.checkbox("동의하십니까?")  # 체크박스
gender = st.radio("성별", ["남성", "여성", "기타"])  # 라디오 버튼
hobby = st.multiselect("취미를 선택하세요", ["독서", "운동", "게임", "음악"])  # 다중 선택
color = st.selectbox("좋아하는 색상", ["빨강", "파랑", "초록"])  # 단일 선택
date = st.date_input("날짜를 선택하세요")  # 날짜 입력
time = st.time_input("시간을 선택하세요")  # 시간 입력
file = st.file_uploader("파일 업로드")  # 파일 업로더
st.text_area("자기소개를 입력하세요")  # 여러 줄 텍스트 입력
st.slider("점수", 0, 100, 50)  # 슬라이더

st.header("버튼 및 상호작용")  # 버튼 등
if st.button("버튼을 눌러보세요"):
    st.success("버튼이 눌렸습니다!")  # 버튼 클릭 시 메시지

st.header("미디어 표시")  # 이미지, 오디오, 비디오
st.image("https://static.streamlit.io/examples/dog.jpg", caption="강아지 이미지")  # 이미지 표시
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")  # 오디오 재생
st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # 비디오 재생

st.header("상태 표시")  # 진행률, 스피너 등
st.progress(70)  # 진행률 표시 (0~100)
with st.spinner("로딩 중..."):
    time.sleep(1)
st.success("로딩 완료!")  # 성공 메시지
st.error("에러 메시지")  # 에러 메시지
st.warning("경고 메시지")  # 경고 메시지
st.info("정보 메시지")  # 정보 메시지

st.header("레이아웃")  # 컬럼, 사이드바 등
col1, col2 = st.columns(2)
col1.write("왼쪽 컬럼")
col2.write("오른쪽 컬럼")

st.sidebar.title("사이드바 예시")  # 사이드바에 요소 추가
st.sidebar.button("사이드바 버튼")

# 각주: 각 요소 위에 주석으로 설명을 달았습니다.
