import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

st.title("성적 데이터 시각화 앱")  # 앱 제목

# 1. CSV 파일 업로드
st.header("1. 성적 데이터 업로드")  # 각주: 사용자로부터 CSV 파일을 받음
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])
df = None
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("데이터 업로드 완료!")
    st.dataframe(df)  # 각주: 업로드된 데이터 미리보기

# 2. 그래프 옵션 선택
st.header("2. 시각화 옵션 선택")  # 각주: 4가지 그래프 중 하나 선택
graph_type = st.radio(
    "원하는 그래프를 선택하세요",
    ("히스토그램", "막대그래프", "산점도", "상자그림")
)

# 3. 변수 선택 및 그래프 그리기
if df is not None:
    st.header("3. 변수 선택 및 그래프 그리기")  # 각주: 그래프별 변수 선택
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    all_cols = df.columns.tolist()

    if graph_type == "히스토그램":
        col = st.selectbox("히스토그램을 그릴 변수(숫자형)", numeric_cols)
        if col:
            fig, ax = plt.subplots()
            sns.histplot(df[col], kde=True, ax=ax)
            ax.set_title(f"{col} 히스토그램")
            st.pyplot(fig)  # 각주: 선택한 변수의 히스토그램 출력

    elif graph_type == "막대그래프":
        col = st.selectbox("막대그래프로 볼 변수(범주형)", all_cols)
        if col:
            fig, ax = plt.subplots()
            df[col].value_counts().plot.bar(ax=ax)
            ax.set_title(f"{col} 막대그래프")
            st.pyplot(fig)  # 각주: 선택한 변수의 빈도 막대그래프 출력

    elif graph_type == "산점도":
        x_col = st.selectbox("X축 변수(숫자형)", numeric_cols)
        y_col = st.selectbox("Y축 변수(숫자형)", numeric_cols)
        if x_col and y_col and x_col != y_col:
            fig, ax = plt.subplots()
            sns.scatterplot(x=df[x_col], y=df[y_col], ax=ax)
            ax.set_title(f"{x_col} vs {y_col} 산점도")
            st.pyplot(fig)  # 각주: 두 변수의 산점도 출력

    elif graph_type == "상자그림":
        col = st.selectbox("상자그림을 그릴 변수(숫자형)", numeric_cols)
        group_col = st.selectbox("그룹화할 변수(범주형)", all_cols)
        if col and group_col:
            fig, ax = plt.subplots()
            sns.boxplot(x=df[group_col], y=df[col], ax=ax)
            ax.set_title(f"{group_col}별 {col} 상자그림")
            st.pyplot(fig)  # 각주: 그룹별 상자그림 출력

# 각주: 그래프별로 변수 선택창이 동적으로 나타나고, 선택 시 자동으로 그래프가 그려집니다.
