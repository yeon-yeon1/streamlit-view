import streamlit as st

# 페이지 설정
st.set_page_config(page_title="성향에 맞는 공부법 찾기", page_icon=":books:", layout="wide")

def main() :

    # 상단 헤더 섹션
    st.markdown("<h1 style='text-align: center; font-size: 20px; border-bottom: 1px solid #9b6cc3; color: #9b6cc3;'>성향에 맞는 공부법 찾기</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; font-size: 20px; padding-top: 50px; padding-bottom: 0; padding-left: 10vw; opacity: 0.6; color: #9b6cc3;'>feat MBTI</h2>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; line-height: 0; font-size: 48px;'>성공법</h1>", unsafe_allow_html=True)

    # MBTI 버튼 섹션
    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        if st.button("MBTI 검사"):
            st.session_state['page'] = 'start'
            st.experimental_rerun()

    with col3:
        st.button("공부법")

    # 페이지 이동 처리
    if 'page' in st.session_state and st.session_state['page'] == 'start':
        st.experimental_rerun()

    # MBTI 타입 섹션
    st.subheader("특징 및 성향")
    mbti_types = [
        ["ESFP", "ENFP", "ISFP", "INFP"],
        ["ESFJ", "ENFJ", "ISFJ", "INFJ"],
        ["ESTP", "ENTP", "ISTP", "INTP"],
        ["ESTJ", "ENTJ", "ISTJ", "INTJ"]
    ]

    for row in mbti_types:
        cols = st.columns(4)
        for i, col in enumerate(cols):
            col.button(row[i])

def mbti_start() :
    # 중앙에 텍스트와 버튼 배치
    st.markdown("<h2 style='text-align: center; padding-top: 200px;'>MBTI 검사를 시작합니다</h2>", unsafe_allow_html=True)

    # 버튼을 중앙에 배치
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button('START'):
            st.session_state['page'] = 'test'
            st.experimental_rerun()

    # 버튼 스타일
    st.markdown(
        """
        <style>
        div.stButton > button {
            background-color: #9b6cc3;
            color: white;
            width: 100%;
            height: 50px;
            font-size: 20px;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 페이지 이동 처리
    if 'page' in st.session_state and st.session_state['page'] == 'test':
        st.experimental_rerun()

def show_mbti_test():
    # 상단 헤더 섹션
    st.markdown("<h1 style='text-align: center; color: #9b6cc3;'>MBTI 검사</h1>", unsafe_allow_html=True)

    # 홈 버튼
    if st.button('홈'):
        st.session_state['page'] = 'home'
        st.experimental_rerun()

    # 폼 섹션
    with st.form(key='mbti_form'):
        st.markdown("##### 쉬는 시간이 생겼을 때")
        score1 = st.radio("", ("집에 혼자 있는 걸 좋아한다.", "나가서 사람들과 어울리는 걸 좋아한다."), index=0, key='question1')

        st.markdown("##### 엘리베이터를 탔을 때")
        score2 = st.radio("", ("엘리베이터는 이동수단일 뿐, 중간에 서지 않고 빨리만 올라갔으면 좋겠다.", "사고가 나면 어떻게 탈출을 해야 하지?"), index=0, key='question2')

        st.markdown("##### 친구가 차사고가 났다고 연락이 왔을 때")
        score3 = st.radio("", ("보험은 들었어?", "어떡해! 다친 데는 없어?"), index=0, key='question3')

        st.markdown("##### 친구들과 함께 간 여행, 숙소에서 짐을 풀고 나가자! 했을 때")
        score4 = st.radio("", ("어디 가게?", "일단 나가서 생각하자!!"), index=0, key='question4')

        submit_button = st.form_submit_button(label='제출')

    if submit_button:
        submit_mbti(score1, score2, score3, score4)
        st.session_state['page'] = 'result'
        st.experimental_rerun()

def submit_mbti(score1, score2, score3, score4):
    result = ""
    if (score1 == '집에 혼자 있는 걸 좋아한다.') :
        result += "I"
    else:
        result += "E"
    if (score2 == '엘리베이터는 이동수단일 뿐, 중간에 서지 않고 빨리만 올라갔으면 좋겠다.') :
        result += "S"
    else:
        result += "N"
    if (score3 == '보험은 들었어?') :
        result += "T"
    else:
        result += "F"
    if (score4 == '어디 가게?') :
        result += "J"
    else:
        result += "P"
    
    # 결과를 세션 상태에 저장
    st.session_state['mbti_result'] = result

def show_result():
    # 상단 헤더 섹션
    st.markdown("<h1 style='text-align: center; color: #9b6cc3;'>MBTI 결과</h1>", unsafe_allow_html=True)

    # 저장된 결과 불러오기
    if 'mbti_result' in st.session_state:
        result_html = f"""
            <div style='text-align: center; font-size: 35px;'>
                당신의 MBTI 유형은: <br> <span style='font-size: 70px; font-weight: bold;'>{st.session_state['mbti_result']}</span>
            </div>
            """
        st.markdown(result_html, unsafe_allow_html=True)
    else:
        st.write("아직 결과가 저장되지 않았습니다. 먼저 MBTI 검사를 완료하세요.")
    
    # 두 버튼을 가로로 배치하고 스타일 적용
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button('다시 검사하기', key='reset'):
            st.session_state['page'] = 'test'
            st.experimental_rerun()

    with col2:
        if st.button(f"{st.session_state['mbti_result']}의 특징 및 성향 확인하기", key='details'):
            st.session_state['page'] = 'details'
            st.experimental_rerun()

    # 스타일 적용을 위한 CSS 추가
    st.markdown(
        """
        <style>
        div.stButton > button {
            width: 100%;
            height: 50px;
            font-size: 20px;
            border-radius: 5px;
            background-color: #9b6cc3;
            color: white;
            margin-top: 30px
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 홈 버튼
    if st.button('홈'):
        st.session_state['page'] = 'home'
        st.experimental_rerun()

def mbti_details():
    if True:
        veiw = [1]
        veiw

# 애플리케이션의 현재 페이지 상태 확인 및 설정
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

# 페이지 상태에 따라 다른 콘텐츠 렌더링
if st.session_state['page'] == 'test':
    show_mbti_test()
elif st.session_state['page'] == 'result':
    show_result()
elif st.session_state['page'] == 'home':
    main()
elif st.session_state['page'] == 'start':
    mbti_start()
elif st.session_state['page'] == 'details':
    mbti_details()