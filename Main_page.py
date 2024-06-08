import streamlit as st

# 페이지 설정
st.set_page_config(page_title="성향에 맞는 공부법 찾기", page_icon=":books:", layout="wide")

# 상단 헤더 섹션
st.markdown("<h1 style='text-align: center; font-size: 20px; border-bottom: 1px solid #9b6cc3; color: #9b6cc3;'>성향에 맞는 공부법 찾기</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; font-size: 20px; padding-top: 50px; padding-bottom: 0; padding-left: 10vw; opacity: 0.6; color: #9b6cc3;'>feat MBTI</h2>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; line-height: 0; font-size: 48px;'>성공법</h1>", unsafe_allow_html=True)

# MBTI 버튼 섹션
col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    if st.button("MBTI 검사"):
        st.write("MBTI 검사 페이지로 이동합니다.")

with col3:
    if st.button("공부법"):
        st.write("공부법 페이지로 이동합니다.")

# MBTI 타입 섹션
st.subheader("특징 및 성향")
mbti_types = [
    ["ESFP", "ENFP", "ISFP", "INFP"],
    ["ESFJ", "ENFJ", "ISFJ", "INFJ"],
    ["ESTP", "ENTP", "ISTP", "INTP"],
    ["ESTJ", "ENTJ", "ISTJ", "INTJ"]
]

# 4열 레이아웃으로 MBTI 타입 버튼 생성
for row in mbti_types:
    cols = st.columns(4)
    for i, col in enumerate(cols):
        if col.button(row[i]):
            st.write(f"{row[i]} 유형에 대한 정보 페이지로 이동합니다.")

