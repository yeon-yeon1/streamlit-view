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

def show_details_ESFP():
    st.markdown("<h1 style='text-align: center; color: #FFD700;'>특징 및 성향 확인하기</h1>", unsafe_allow_html=True)

    # 이미지 섹션
    image_path = "file-OhNOUyNt6fAkiM3tM2nU5bT6"
    st.image(image_path, use_column_width=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='display: inline-block; background-color: #FFD700; color: white; padding: 10px 20px; border-radius: 5px;'>INTJ</h2>
            <button style='display: inline-block; margin-left: 20px; padding: 10px 20px; background-color: #FFD700; color: white; border: none; border-radius: 5px;'>공부법 확인하기</button>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li>사교적이고 외향적</li>
                    <ul>
                        <li>사람들과의 상호 작용을 즐기며, 새로운 사람을 만나고 관계를 형성하는 것을 좋아합니다.</li>
                        <li>파티나 사회적 모임에서 에너지를 얻고, 주목받는 것을 즐깁니다.</li>
                    <ul>
                <li>현실적이고 실용적</li>
                    <ul>
                        <li>현재 순간에 집중하며, 현실적이고 실용적인 접근 방식을 선호합니다.</li>
                        <li>구체적이고 실질적인 정보를 다루는 것을 좋아하며, 세부 사항에 주의를 기울입니다.</li>
                    <ul>
                <li>감정적이며 따뜻한</li>
                    <ul>
                        <li>다른 사람들의 감정과 필요에 민감하며, 이를 이해하고 도우려는 성향이 강합니다.</li>
                        <li>공감 능력이 뛰어나며, 다른 사람들과의 관계에서 따뜻함과 이해를 보여줍니다.</li>
                    <ul>
                <li>즉흥적이고 유연한</li>
                    <ul>
                        <li>계획을 세우기보다는 즉흥적으로 행동하며, 변화에 유연하게 대처할 수 있습니다.</li>
                        <li>새로운 경험과 모험을 즐기며, 단조로운 일상보다는 다양한 활동을 선호합니다.</li>
                    <ul>
                <li>즐거움을 추구하는 성향</li>
                    <ul>
                        <li>재미와 즐거움을 중시하며, 삶을 즐기고 긍정적으로 살아가려는 태도를 가집니다.</li>
                        <li>엔터테인먼트, 예술, 스포츠 등 다양한 활동에서 즐거움을 찾습니다.</li>
                    <ul>
                <li>강한 대인 관계 기술</li>
                    <ul>
                        <li>훌륭한 대인 관계 기술을 가지고 있으며, 다른 사람들과의 상호 작용에서 능숙함을 보입니다.</li>
                        <li>협동적이고 팀 플레이어로서의 역할을 잘 수행합니다.</li>
                    <ul>
                <li>리스크 테이커</li>
                    <ul>
                        <li>새로운 도전과 리스크를 두려워하지 않고, 이를 통해 성장하고 배우는 것을 좋아합니다.</li>
                        <li>때로는 충동적인 결정을 내리기도 하지만, 이를 통해 다양한 경험을 쌓습니다.</li>
                    <ul>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 홈 버튼
    if st.button('홈'):
        st.session_state['page'] = 'home'
        st.experimental_rerun()

def mbti_details():
    if True:
        show_details_ESFP()

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