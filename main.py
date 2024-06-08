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
        if st.button("공부법") :
            st.session_state['page'] = 'study'
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
            if col.button(row[i]):
                st.session_state['mbti_result'] = row[i]
                st.session_state['page'] = 'details'
                st.experimental_rerun()



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

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #FFD700; color: black; padding: 10px; border-radius: 5px;'>ESFP</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li>사교적이고 외향적
                    <ul>
                        <li>사람들과의 상호 작용을 즐기며, 새로운 사람을 만나고 관계를 형성하는 것을 좋아합니다.</li>
                        <li>파티나 사회적 모임에서 에너지를 얻고, 주목받는 것을 즐깁니다.</li>
                    </ul>
                </li>
                <li>현실적이고 실용적
                    <ul>
                        <li>현재 순간에 집중하며, 현실적이고 실용적인 접근 방식을 선호합니다.</li>
                        <li>구체적이고 실질적인 정보를 다루는 것을 좋아하며, 세부 사항에 주의를 기울입니다.</li>
                    </ul>
                </li>
                <li>감정적이며 따뜻한
                    <ul>
                        <li>다른 사람들의 감정과 필요에 민감하며, 이를 이해하고 도우려는 성향이 강합니다.</li>
                        <li>공감 능력이 뛰어나며, 다른 사람들과의 관계에서 따뜻함과 이해를 보여줍니다.</li>
                    </ul>
                </li>
                <li>즉흥적이고 유연한
                    <ul>
                        <li>계획을 세우기보다는 즉흥적으로 행동하며, 변화에 유연하게 대처할 수 있습니다.</li>
                        <li>새로운 경험과 모험을 즐기며, 단조로운 일상보다는 다양한 활동을 선호합니다.</li>
                    </ul>
                </li>
                <li>즐거움을 추구하는 성향
                    <ul>
                        <li>재미와 즐거움을 중시하며, 삶을 즐기고 긍정적으로 살아가려는 태도를 가집니다.</li>
                        <li>엔터테인먼트, 예술, 스포츠 등 다양한 활동에서 즐거움을 찾습니다.</li>
                    </ul>
                </li>
                <li>강한 대인 관계 기술
                    <ul>
                        <li>훌륭한 대인 관계 기술을 가지고 있으며, 다른 사람들과의 상호 작용에서 능숙함을 보입니다.</li>
                        <li>협동적이고 팀 플레이어로서의 역할을 잘 수행합니다.</li>
                    </ul>
                </li>
                <li>리스크 테이커
                    <ul>
                        <li>새로운 도전과 리스크를 두려워하지 않고, 이를 통해 성장하고 배우는 것을 좋아합니다.</li>
                        <li>때로는 충동적인 결정을 내리기도 하지만, 이를 통해 다양한 경험을 쌓습니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    # 두 버튼을 가로로 배치하고 스타일 적용
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button('홈'):
            st.session_state['page'] = 'home'
            st.experimental_rerun()

    with col2:
        if st.button('ESFP에게 맞는 공부법 확인하기'):
            st.session_state['page'] = 'study'
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
            background-color: #FFD700;
            color: black;
            margin-top: 30px
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
def show_details_ESFJ():
    st.markdown("<h1 style='text-align: center; color: #87CEEB;'>특징 및 성향 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #87CEEB; color: black; padding: 10px; border-radius: 5px;'>ESFJ</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li>사교적이고 외향적
                    <ul>
                        <li>사람들과의 상호 작용을 즐기며, 새로운 사람을 만나고 관계를 형성하는 것을 좋아합니다.</li>
                        <li>사회적 모임에서 에너지를 얻고, 다른 사람들과 함께하는 시간을 소중히 여깁니다.</li>
                    </ul>
                </li>
                <li>현실적이고 실용적
                    <ul>
                        <li>현재 순간에 집중하며, 구체적이고 실질적인 정보를 다루는 것을 선호합니다.</li>
                        <li>세부 사항에 주의를 기울이며, 현실적이고 실용적인 접근 방식을 중시합니다.</li>
                    </ul>
                </li>
                <li>감정적이며 따뜻한
                    <ul>
                        <li>다른 사람들의 감정과 필요에 민감하며, 이를 이해하고 도우려는 성향이 강합니다.</li>
                        <li>공감 능력이 뛰어나며, 다른 사람들과의 관계에서 따뜻함과 이해를 보여줍니다.</li>
                    </ul>
                </li>
                <li>조직적이고 계획적
                    <ul>
                        <li>체계적이고 조직적인 생활을 선호하며, 계획을 세워 이를 실행하는 데 능숙합니다.</li>
                        <li>규칙과 절차를 중시하며, 안정적이고 예측 가능한 환경을 좋아합니다.</li>
                    </ul>
                </li>
                <li>책임감 있고 신뢰할 수 있음
                    <ul>
                        <li>맡은 일에 책임감을 가지고 성실하게 임하며, 신뢰할 수 있는 사람으로 평가받습니다.</li>
                        <li>다른 사람들을 돕고 지원하는 데 적극적이며, 사회적 책임을 중요시합니다.</li>
                    </ul>
                </li>
                <li>조화와 협력을 중시
                    <ul>
                        <li>갈등을 피하고 조화를 유지하려 하며, 협력적인 관계를 중시합니다.</li>
                        <li>다른 사람들과의 협력을 통해 공동의 목표를 달성하는 것을 중요하게 생각합니다.</li>
                    </ul>
                </li>
                <li>전통과 규범을 중시
                    <ul>
                        <li>전통적 가치와 사회적 규범을 존중하며, 이를 지키려는 성향이 있습니다.</li>
                        <li>기존의 방식과 절차를 따르는 것을 선호하며, 변화를 두려워하기도 합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    # 두 버튼을 가로로 배치하고 스타일 적용
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button('홈'):
            st.session_state['page'] = 'home'
            st.experimental_rerun()

    with col2:
        if st.button('ESFJ에게 맞는 공부법 확인하기'):
            st.session_state['page'] = 'study'
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
            background-color: #87CEEB;
            color: black;
            margin-top: 30px
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
def show_details_ESTP():
    st.markdown("<h1 style='text-align: center; color: #FFD700;'>특징 및 성향 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #FFD700; color: black; padding: 10px; border-radius: 5px;'>ESTP</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li>사교적이고 외향적
                    <ul>
                        <li>사람들과의 상호 작용을 즐기며, 새로운 사람을 만나고 관계를 형성하는 것을 좋아합니다.</li>
                        <li>사회적 모임에서 에너지를 얻고, 다른 사람들과 함께하는 시간을 소중히 여깁니다.</li>
                    </ul>
                </li>
                <li>현실적이고 실용적
                    <ul>
                        <li>현재 순간에 집중하며, 구체적이고 실질적인 정보를 다루는 것을 선호합니다.</li>
                        <li>세부 사항에 주의를 기울이며, 현실적이고 실용적인 접근 방식을 중시합니다.</li>
                    </ul>
                </li>
                <li>문제 해결 능력
                    <ul>
                        <li>상황을 빠르게 분석하고 결정을 내리는 능력이 뛰어납니다.</li>
                        <li>긴박한 상황에서도 침착하게 대처하고 문제를 해결하는 데 능숙합니다.</li>
                    </ul>
                </li>
                <li>즉흥적이고 유연한
                    <ul>
                        <li>계획을 세우기보다는 즉흥적으로 행동하며, 변화에 유연하게 대처할 수 있습니다.</li>
                        <li>새로운 경험과 모험을 즐기며, 단조로운 일상보다는 다양한 활동을 선호합니다.</li>
                    </ul>
                </li>
                <li>논리적이고 분석적
                    <ul>
                        <li>문제를 논리적으로 분석하고, 객관적인 관점에서 판단을 내립니다.</li>
                        <li>상황을 비판적으로 바라보며, 효율적인 해결책을 찾기 위해 노력합니다.</li>
                    </ul>
                </li>
                <li>위험 감수 성향
                    <ul>
                        <li>새로운 도전과 리스크를 두려워하지 않고, 이를 통해 성장하고 배우는 것을 좋아합니다.</li>
                        <li>모험을 즐기며, 이를 통해 삶을 더 흥미롭게 만듭니다.</li>
                    </ul>
                </li>
                <li>대인 관계 기술
                    <ul>
                        <li>훌륭한 대인 관계 기술을 가지고 있으며, 다른 사람들과의 상호 작용에서 능숙함을 보입니다.</li>
                        <li>협력적이고 팀 플레이어로서의 역할을 잘 수행합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    # 두 버튼을 가로로 배치하고 스타일 적용
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button('홈'):
            st.session_state['page'] = 'home'
            st.experimental_rerun()

    with col2:
        if st.button('ESTP에게 맞는 공부법 확인하기'):
            st.session_state['page'] = 'study'
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
            background-color: #FFD700;
            color: black;
            margin-top: 30px
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
def show_details_ESTJ():
    st.markdown("<h1 style='text-align: center; color: #87CEEB;'>특징 및 성향 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #87CEEB; color: black; padding: 10px; border-radius: 5px;'>ESTJ</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li>사교적이고 외향적
                    <ul>
                        <li>사람들과의 상호 작용을 즐기며, 명확한 규칙과 질서를 중시합니다.</li>
                        <li>조직 내에서 지도자 역할을 맡는 것을 좋아합니다.</li>
                    </ul>
                </li>
                <li>현실적이고 실용적
                    <ul>
                        <li>구체적이고 실질적인 정보를 다루는 것을 선호합니다.</li>
                        <li>현실적인 접근 방식을 중시하며, 효율성과 생산성을 중요시합니다.</li>
                    </ul>
                </li>
                <li>조직적이고 계획적
                    <ul>
                        <li>체계적이고 조직적인 생활을 선호하며, 계획을 세워 이를 실행하는 데 능숙합니다.</li>
                        <li>규칙과 절차를 중시하며, 안정적이고 예측 가능한 환경을 좋아합니다.</li>
                    </ul>
                </li>
                <li>책임감 있고 신뢰할 수 있음
                    <ul>
                        <li>맡은 일에 책임감을 가지고 성실하게 임하며, 신뢰할 수 있는 사람으로 평가받습니다.</li>
                        <li>다른 사람들을 돕고 지원하는 데 적극적이며, 사회적 책임을 중요시합니다.</li>
                    </ul>
                </li>
                <li>리더십 발휘
                    <ul>
                        <li>지도자로서의 역할을 즐기며, 조직을 이끄는 데 능숙합니다.</li>
                        <li>목표 달성을 위해 전략을 세우고, 이를 추진하는 데 능숙합니다.</li>
                    </ul>
                </li>
                <li>결단력 있음
                    <ul>
                        <li>빠르고 단호한 결정을 내리는 능력이 있습니다.</li>
                        <li>위기 상황에서도 침착하게 결정을 내립니다.</li>
                    </ul>
                </li>
                <li>사회적 책임
                    <ul>
                        <li>사회적 규범과 책임을 중시하며, 이를 준수하려고 노력합니다.</li>
                        <li>사회적 문제에 관심을 가지고, 해결 방안을 찾기 위해 노력합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    # 두 버튼을 가로로 배치하고 스타일 적용
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button('홈'):
            st.session_state['page'] = 'home'
            st.experimental_rerun()

    with col2:
        if st.button('ESTJ에게 맞는 공부법 확인하기'):
            st.session_state['page'] = 'study'
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
            background-color: #87CEEB;
            color: black;
            margin-top: 30px
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def show_details_ENFP():
    st.markdown("<h1 style='text-align: center; color: #3CB371;'>특징 및 성향 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #3CB371; color: black; padding: 10px; border-radius: 5px;'>ENFP</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li>사교적이고 외향적
                    <ul>
                        <li>사람들과의 상호 작용을 즐기며, 새로운 아이디어와 가능성을 탐구하는 것을 좋아합니다.</li>
                        <li>다양한 사회적 활동에서 에너지를 얻습니다.</li>
                    </ul>
                </li>
                <li>창의적이고 개방적
                    <ul>
                        <li>창의적이고 개방적인 사고를 가지고 있으며, 새로운 경험을 좋아합니다.</li>
                        <li>기존의 틀을 벗어나 자유롭게 사고하며, 미래지향적인 생각을 합니다.</li>
                    </ul>
                </li>
                <li>감정적이며 따뜻한
                    <ul>
                        <li>다른 사람들의 감정과 필요에 민감하며, 이를 이해하고 도우려는 성향이 강합니다.</li>
                        <li>공감 능력이 뛰어나며, 다른 사람들과의 관계에서 따뜻함과 이해를 보여줍니다.</li>
                    </ul>
                </li>
                <li>유연하고 즉흥적
                    <ul>
                        <li>변화에 유연하게 대처하며, 즉흥적으로 행동하는 것을 좋아합니다.</li>
                        <li>계획보다는 순간의 기회를 포착하는 것을 선호합니다.</li>
                    </ul>
                </li>
                <li>열정적이고 에너지가 넘침
                    <ul>
                        <li>자신의 열정을 다른 사람들과 공유하며, 활기차게 활동합니다.</li>
                        <li>새로운 아이디어와 프로젝트에 열정적으로 참여합니다.</li>
                    </ul>
                </li>
                <li>융통성 있음
                    <ul>
                        <li>변화에 유연하게 대처하며, 다양한 상황에 적응하는 능력이 뛰어납니다.</li>
                        <li>갑작스러운 변화에도 쉽게 적응하며, 문제를 해결합니다.</li>
                    </ul>
                </li>
                <li>미래 지향적
                    <ul>
                        <li>장기적인 목표와 비전에 대해 생각하며, 이를 달성하기 위해 노력합니다.</li>
                        <li>현재의 행동이 미래에 미칠 영향을 고려하여 계획을 세웁니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    # 두 버튼을 가로로 배치하고 스타일 적용
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button('홈'):
            st.session_state['page'] = 'home'
            st.experimental_rerun()

    with col2:
        if st.button('ENFP에게 맞는 공부법 확인하기'):
            st.session_state['page'] = 'study'
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
            background-color: #3CB371;
            color: black;
            margin-top: 30px
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def show_details_ENFJ():
    st.markdown("<h1 style='text-align: center; color: #3CB371;'>특징 및 성향 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #3CB371; color: black; padding: 10px; border-radius: 5px;'>ENFJ</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li>사교적이고 외향적
                    <ul>
                        <li>사람들과의 상호 작용을 즐기며, 다른 사람들에게 영감을 주고자 합니다.</li>
                        <li>파티나 사회적 모임에서 에너지를 얻고, 주목받는 것을 즐깁니다.</li>
                    </ul>
                </li>
                <li>높은 도덕적 기준
                    <ul>
                        <li>도덕적 가치와 윤리를 중시하며, 이를 바탕으로 행동합니다.</li>
                        <li>공정하고 정직한 태도로 사람들과의 관계를 유지합니다.</li>
                    </ul>
                </li>
                <li>감정적이며 따뜻한
                    <ul>
                        <li>다른 사람들의 감정과 필요에 민감하며, 이를 이해하고 도우려는 성향이 강합니다.</li>
                        <li>공감 능력이 뛰어나며, 다른 사람들과의 관계에서 따뜻함과 이해를 보여줍니다.</li>
                    </ul>
                </li>
                <li>조직적이고 계획적
                    <ul>
                        <li>체계적이고 조직적인 생활을 선호하며, 계획을 세워 이를 실행하는 데 능숙합니다.</li>
                        <li>규칙과 절차를 중시하며, 안정적이고 예측 가능한 환경을 좋아합니다.</li>
                    </ul>
                </li>
                <li>책임감 있고 신뢰할 수 있음
                    <ul>
                        <li>맡은 일에 책임감을 가지고 성실하게 임하며, 신뢰할 수 있는 사람으로 평가받습니다.</li>
                        <li>다른 사람들을 돕고 지원하는 데 적극적이며, 사회적 책임을 중요시합니다.</li>
                    </ul>
                </li>
                <li>팀워크 중시
                    <ul>
                        <li>협력적인 환경에서 팀을 이끌고, 팀원들과 함께 일하는 것을 선호합니다.</li>
                        <li>팀의 목표를 달성하기 위해 협력과 조화를 중시합니다.</li>
                    </ul>
                </li>
                <li>영감과 동기 부여
                    <ul>
                        <li>다른 사람들에게 영감을 주고, 동기를 부여하는 능력이 뛰어납니다.</li>
                        <li>자신의 열정과 비전을 통해 주변 사람들에게 긍정적인 영향을 미칩니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    # 두 버튼을 가로로 배치하고 스타일 적용
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button('홈'):
            st.session_state['page'] = 'home'
            st.experimental_rerun()

    with col2:
        if st.button('ENFJ에게 맞는 공부법 확인하기'):
            st.session_state['page'] = 'study'
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
            background-color: #3CB371;
            color: black;
            margin-top: 30px
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def show_details_ENTP():
    st.markdown("<h1 style='text-align: center; color: #9b6cc3;'>특징 및 성향 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #9b6cc3; color: black; padding: 10px; border-radius: 5px;'>ENTP</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li>사교적이고 외향적
                    <ul>
                        <li>사람들과의 상호 작용을 즐기며, 새로운 아이디어와 도전을 좋아합니다.</li>
                        <li>토론과 논쟁을 통해 에너지를 얻고, 지적 자극을 추구합니다.</li>
                    </ul>
                </li>
                <li>창의적이고 혁신적
                    <ul>
                        <li>창의적이고 혁신적인 사고를 가지고 있으며, 기존의 틀을 벗어나 자유롭게 사고합니다.</li>
                        <li>다양한 아이디어를 탐구하며, 문제 해결을 위한 새로운 접근 방식을 찾습니다.</li>
                    </ul>
                </li>
                <li>논리적이고 분석적
                    <ul>
                        <li>문제를 논리적으로 분석하고, 객관적인 관점에서 판단을 내립니다.</li>
                        <li>상황을 비판적으로 바라보며, 효율적인 해결책을 찾기 위해 노력합니다.</li>
                    </ul>
                </li>
                <li>즉흥적이고 유연한
                    <ul>
                        <li>변화에 유연하게 대처하며, 즉흥적으로 행동하는 것을 좋아합니다.</li>
                        <li>계획보다는 순간의 기회를 포착하는 것을 선호합니다.</li>
                    </ul>
                </li>
                <li>도전적 성향
                    <ul>
                        <li>어려운 문제나 도전에 맞서 싸우는 것을 즐깁니다.</li>
                        <li>새로운 기회와 도전을 통해 자신의 능력을 시험하는 것을 좋아합니다.</li>
                    </ul>
                </li>
                <li>창의적인 문제 해결
                    <ul>
                        <li>독창적인 아이디어를 통해 문제를 해결하는 능력이 뛰어납니다.</li>
                        <li>복잡한 문제를 창의적인 접근 방식으로 해결합니다.</li>
                    </ul>
                </li>
                <li>지적 호기심
                    <ul>
                        <li>다양한 주제에 대해 호기심이 많으며, 새로운 지식을 탐구하는 것을 좋아합니다.</li>
                        <li>책, 논문, 강연 등을 통해 지속적으로 학습하고 성장합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    # 두 버튼을 가로로 배치하고 스타일 적용
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button('홈'):
            st.session_state['page'] = 'home'
            st.experimental_rerun()

    with col2:
        if st.button('ENTP에게 맞는 공부법 확인하기'):
            st.session_state['page'] = 'study'
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
            color: black;
            margin-top: 30px
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def show_details_ENTJ():
    st.markdown("<h1 style='text-align: center; color: #9b6cc3;'>특징 및 성향 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #9b6cc3; color: black; padding: 10px; border-radius: 5px;'>ENTJ</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li>사교적이고 외향적
                    <ul>
                        <li>사람들과의 상호 작용을 즐기며, 리더십을 발휘하는 것을 좋아합니다.</li>
                        <li>사회적 모임에서 에너지를 얻고, 다른 사람들과 함께하는 시간을 소중히 여깁니다.</li>
                    </ul>
                </li>
                <li>논리적이고 분석적
                    <ul>
                        <li>문제를 논리적으로 분석하고, 객관적인 관점에서 판단을 내립니다.</li>
                        <li>상황을 비판적으로 바라보며, 효율적인 해결책을 찾기 위해 노력합니다.</li>
                    </ul>
                </li>
                <li>조직적이고 계획적
                    <ul>
                        <li>체계적이고 조직적인 생활을 선호하며, 계획을 세워 이를 실행하는 데 능숙합니다.</li>
                        <li>규칙과 절차를 중시하며, 안정적이고 예측 가능한 환경을 좋아합니다.</li>
                    </ul>
                </li>
                <li>리더십과 통제력
                    <ul>
                        <li>강한 리더십을 발휘하며, 다른 사람들을 이끌고 조직을 통제하는 능력이 뛰어납니다.</li>
                        <li>목표 달성을 위해 전략을 세우고, 이를 추진하는 데 능숙합니다.</li>
                    </ul>
                </li>
                <li>전략적 사고
                    <ul>
                        <li>장기적인 목표를 설정하고, 이를 달성하기 위한 전략을 수립합니다.</li>
                        <li>복잡한 문제를 체계적으로 분석하고, 효과적인 해결책을 찾습니다.</li>
                    </ul>
                </li>
                <li>높은 자신감
                    <ul>
                        <li>자신의 능력과 판단에 대한 강한 자신감을 가지고 있습니다.</li>
                        <li>결정을 내릴 때 확신을 가지고 행동하며, 주저함이 없습니다.</li>
                    </ul>
                </li>
                <li>결과 지향적
                    <ul>
                        <li>목표 달성에 집중하며, 결과를 중시하는 성향이 있습니다.</li>
                        <li>효율성과 생산성을 중요하게 생각하며, 성과를 측정하고 평가합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    # 두 버튼을 가로로 배치하고 스타일 적용
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button('홈'):
            st.session_state['page'] = 'home'
            st.experimental_rerun()

    with col2:
        if st.button('ENTJ에게 맞는 공부법 확인하기'):
            st.session_state['page'] = 'study'
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
            color: black;
            margin-top: 30px
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def show_details_ISFP():
    st.markdown("<h1 style='text-align: center; color: #FFD700;'>특징 및 성향 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #FFD700; color: black; padding: 10px; border-radius: 5px;'>ISFP</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li>내향적이고 조용한
                    <ul>
                        <li>내향적인 성향이 강하며, 혼자만의 시간을 즐깁니다.</li>
                        <li>사람들과의 상호 작용보다는 개인적인 공간에서 에너지를 얻습니다.</li>
                    </ul>
                </li>
                <li>예술적이고 감성적
                    <ul>
                        <li>예술적이고 감성적인 면이 강하며, 감각적인 경험을 중시합니다.</li>
                        <li>창의적인 표현을 통해 자신의 감정을 나타내고자 합니다.</li>
                    </ul>
                </li>
                <li>현실적이고 실용적
                    <ul>
                        <li>현재 순간에 집중하며, 구체적이고 실질적인 정보를 다루는 것을 선호합니다.</li>
                        <li>세부 사항에 주의를 기울이며, 현실적이고 실용적인 접근 방식을 중시합니다.</li>
                    </ul>
                </li>
                <li>유연하고 즉흥적
                    <ul>
                        <li>변화에 유연하게 대처하며, 즉흥적으로 행동하는 것을 좋아합니다.</li>
                        <li>계획보다는 순간의 기회를 포착하는 것을 선호합니다.</li>
                    </ul>
                </li>
                <li>조용한 혁신가
                    <ul>
                        <li>창의적이지만 겸손한 성격으로, 자신의 예술적 표현을 통해 혁신을 이끕니다.</li>
                        <li>새로운 아이디어와 접근 방식을 통해 변화를 만들어 냅니다.</li>
                    </ul>
                </li>
                <li>개인주의 성향
                    <ul>
                        <li>개인의 자유와 자율성을 중시하며, 독립적으로 행동하는 것을 좋아합니다.</li>
                        <li>자신의 가치관과 신념을 중요하게 생각하며, 이를 지키려 합니다.</li>
                    </ul>
                </li>
                <li>감정적으로 예민
                    <ul>
                        <li>감정적으로 예민하며, 자신의 감정을 깊이 이해하고 표현하는 능력이 있습니다.</li>
                        <li>다른 사람들의 감정에 공감하며, 이를 배려하는 태도를 보입니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    # 두 버튼을 가로로 배치하고 스타일 적용
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button('홈'):
            st.session_state['page'] = 'home'
            st.experimental_rerun()

    with col2:
        if st.button('ISFP에게 맞는 공부법 확인하기'):
            st.session_state['page'] = 'study'
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
            background-color: #FFD700;
            color: black;
            margin-top: 30px
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def show_details_ISFJ():
    st.markdown("<h1 style='text-align: center; color: #87CEEB;'>특징 및 성향 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #87CEEB; color: black; padding: 10px; border-radius: 5px; padding-left:12px;'>ISFJ</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li>내향적이고 조용한
                    <ul>
                        <li>내향적인 성향이 강하며, 혼자만의 시간을 즐깁니다.</li>
                        <li>사람들과의 상호 작용보다는 개인적인 공간에서 에너지를 얻습니다.</li>
                    </ul>
                </li>
                <li>현실적이고 실용적
                    <ul>
                        <li>현재 순간에 집중하며, 구체적이고 실질적인 정보를 다루는 것을 선호합니다.</li>
                        <li>세부 사항에 주의를 기울이며, 현실적이고 실용적인 접근 방식을 중시합니다.</li>
                    </ul>
                </li>
                <li>감정적이며 따뜻한
                    <ul>
                        <li>다른 사람들의 감정과 필요에 민감하며, 이를 이해하고 도우려는 성향이 강합니다.</li>
                        <li>공감 능력이 뛰어나며, 다른 사람들과의 관계에서 따뜻함과 이해를 보여줍니다.</li>
                    </ul>
                </li>
                <li>조직적이고 계획적
                    <ul>
                        <li>체계적이고 조직적인 생활을 선호하며, 계획을 세워 이를 실행하는 데 능숙합니다.</li>
                        <li>규칙과 절차를 중시하며, 안정적이고 예측 가능한 환경을 좋아합니다.</li>
                    </ul>
                </li>
                <li>헌신적
                    <ul>
                        <li>타인을 돕기 위해 헌신하며, 다른 사람들의 필요를 충족시키는 것을 중요하게 생각합니다.</li>
                        <li>자신의 시간을 할애하여 다른 사람들을 지원하고 도와줍니다.</li>
                    </ul>
                </li>
                <li>믿음직함
                    <ul>
                        <li>신뢰할 수 있는 사람으로 평가받으며, 약속을 지키는 데 있어서 매우 책임감이 강합니다.</li>
                        <li>다른 사람들이 의지할 수 있는 존재로 인식됩니다.</li>
                    </ul>
                </li>
                <li>전통 중시
                    <ul>
                        <li>전통과 관습을 중요하게 여기며, 이를 지키기 위해 노력합니다.</li>
                        <li>기존의 가치와 규범을 존중하며, 변화보다는 안정성을 선호합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    # 두 버튼을 가로로 배치하고 스타일 적용
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button('홈'):
            st.session_state['page'] = 'home'
            st.experimental_rerun()

    with col2:
        if st.button('ISFJ에게 맞는 공부법 확인하기'):
            st.session_state['page'] = 'study'
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
            background-color: #87CEEB;
            color: black;
            margin-top: 30px
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def show_details_ISTP():
    st.markdown("<h1 style='text-align: center; color: #FFD700;'>특징 및 성향 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #FFD700; color: black; padding: 10px; border-radius: 5px;'>ISTP</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li>내향적이고 조용한
                    <ul>
                        <li>내향적인 성향이 강하며, 혼자만의 시간을 즐깁니다.</li>
                        <li>사람들과의 상호 작용보다는 개인적인 공간에서 에너지를 얻습니다.</li>
                    </ul>
                </li>
                <li>현실적이고 실용적
                    <ul>
                        <li>현재 순간에 집중하며, 구체적이고 실질적인 정보를 다루는 것을 선호합니다.</li>
                        <li>문제 해결을 위한 현실적이고 실용적인 접근 방식을 중시합니다.</li>
                    </ul>
                </li>
                <li>논리적이고 분석적
                    <ul>
                        <li>문제를 논리적으로 분석하고, 객관적인 관점에서 판단을 내립니다.</li>
                        <li>상황을 비판적으로 바라보며, 효율적인 해결책을 찾기 위해 노력합니다.</li>
                    </ul>
                </li>
                <li>유연하고 즉흥적
                    <ul>
                        <li>변화에 유연하게 대처하며, 즉흥적으로 행동하는 것을 좋아합니다.</li>
                        <li>계획보다는 순간의 기회를 포착하는 것을 선호합니다.</li>
                    </ul>
                </li>
                <li>독립적
                    <ul>
                        <li>독립적으로 일하는 것을 선호하며, 자신의 공간과 시간을 중요하게 생각합니다.</li>
                        <li>혼자서 문제를 해결하고, 독자적으로 결정을 내리는 경향이 있습니다.</li>
                    </ul>
                </li>
                <li>위기 대처 능력
                    <ul>
                        <li>위기 상황에서도 침착하게 대처하며, 문제 해결 능력이 뛰어납니다.</li>
                        <li>빠르게 상황을 파악하고, 효율적인 해결책을 찾아냅니다.</li>
                    </ul>
                </li>
                <li>직접적인 커뮤니케이션
                    <ul>
                        <li>솔직하고 직접적으로 의사소통하며, 복잡한 설명을 피하는 경향이 있습니다.</li>
                        <li>간결하고 명확하게 자신의 의견을 전달합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    # 두 버튼을 가로로 배치하고 스타일 적용
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button('홈'):
            st.session_state['page'] = 'home'
            st.experimental_rerun()

    with col2:
        if st.button('ISTP에게 맞는 공부법 확인하기'):
            st.session_state['page'] = 'study'
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
            background-color: #FFD700;
            color: black;
            margin-top: 30px
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def show_details_ISTJ():
    st.markdown("<h1 style='text-align: center; color: #87CEEB;'>특징 및 성향 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #87CEEB; color: black; padding: 10px; border-radius: 5px; padding-left: 12px;'> ISTJ</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li>내향적이고 조용한
                    <ul>
                        <li>내향적인 성향이 강하며, 혼자만의 시간을 즐깁니다.</li>
                        <li>사람들과의 상호 작용보다는 개인적인 공간에서 에너지를 얻습니다.</li>
                    </ul>
                </li>
                <li>현실적이고 실용적
                    <ul>
                        <li>현재 순간에 집중하며, 구체적이고 실질적인 정보를 다루는 것을 선호합니다.</li>
                        <li>세부 사항에 주의를 기울이며, 현실적이고 실용적인 접근 방식을 중시합니다.</li>
                    </ul>
                </li>
                <li>조직적이고 계획적
                    <ul>
                        <li>체계적이고 조직적인 생활을 선호하며, 계획을 세워 이를 실행하는 데 능숙합니다.</li>
                        <li>규칙과 절차를 중시하며, 안정적이고 예측 가능한 환경을 좋아합니다.</li>
                    </ul>
                </li>
                <li>책임감 있고 신뢰할 수 있음
                    <ul>
                        <li>맡은 일에 책임감을 가지고 성실하게 임하며, 신뢰할 수 있는 사람으로 평가받습니다.</li>
                        <li>다른 사람들을 돕고 지원하는 데 적극적이며, 사회적 책임을 중요시합니다.</li>
                    </ul>
                </li>
                <li>전통과 규범을 중시
                    <ul>
                        <li>전통적 가치와 사회적 규범을 존중하며, 이를 지키려는 성향이 있습니다.</li>
                        <li>기존의 방식과 절차를 따르는 것을 선호하며, 변화를 두려워하기도 합니다.</li>
                    </ul>
                </li>
                <li>정밀함
                    <ul>
                        <li>일의 세부 사항에 주의를 기울이며, 정확하고 정밀하게 일을 처리합니다.</li>
                        <li>실수를 최소화하고, 높은 품질의 결과를 추구합니다.</li>
                    </ul>
                </li>
                <li>논리적 사고
                    <ul>
                        <li>문제를 논리적으로 분석하고, 체계적으로 접근합니다.</li>
                        <li>결정을 내릴 때 객관적이고 합리적인 판단을 합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    # 두 버튼을 가로로 배치하고 스타일 적용
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button('홈'):
            st.session_state['page'] = 'home'
            st.experimental_rerun()

    with col2:
        if st.button('ISTJ에게 맞는 공부법 확인하기'):
            st.session_state['page'] = 'study'
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
            background-color: #87CEEB;
            color: black;
            margin-top: 30px
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def show_details_INFP():
    st.markdown("<h1 style='text-align: center; color: #3CB371;'>특징 및 성향 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #3CB371; color: black; padding: 10px; border-radius: 5px;'>INFP</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li>내향적이고 조용한
                    <ul>
                        <li>내향적인 성향이 강하며, 혼자만의 시간을 즐깁니다.</li>
                        <li>사람들과의 상호 작용보다는 개인적인 공간에서 에너지를 얻습니다.</li>
                    </ul>
                </li>
                <li>창의적이고 개방적
                    <ul>
                        <li>창의적이고 개방적인 사고를 가지고 있으며, 새로운 경험을 좋아합니다.</li>
                        <li>기존의 틀을 벗어나 자유롭게 사고하며, 미래지향적인 생각을 합니다.</li>
                    </ul>
                </li>
                <li>감정적이며 따뜻한
                    <ul>
                        <li>다른 사람들의 감정과 필요에 민감하며, 이를 이해하고 도우려는 성향이 강합니다.</li>
                        <li>공감 능력이 뛰어나며, 다른 사람들과의 관계에서 따뜻함과 이해를 보여줍니다.</li>
                    </ul>
                </li>
                <li>유연하고 즉흥적
                    <ul>
                        <li>변화에 유연하게 대처하며, 즉흥적으로 행동하는 것을 좋아합니다.</li>
                        <li>계획보다는 순간의 기회를 포착하는 것을 선호합니다.</li>
                    </ul>
                </li>
                <li>이상주의적
                    <ul>
                        <li>높은 이상과 가치를 추구하며, 세상을 더 나은 곳으로 만들고자 합니다.</li>
                        <li>자신의 신념과 가치를 지키기 위해 노력합니다.</li>
                    </ul>
                </li>
                <li>강한 내적 동기
                    <ul>
                        <li>자신의 내적 신념과 가치에 따라 행동하며, 외부의 압력에 굴복하지 않습니다.</li>
                        <li>자신이 옳다고 믿는 것을 위해 헌신합니다.</li>
                    </ul>
                </li>
                <li>심미적 감각
                    <ul>
                        <li>예술과 아름다움에 대한 높은 감각을 가지고 있으며, 이를 통해 감정을 표현합니다.</li>
                        <li>창작 활동을 통해 자신의 감정을 전달하고자 합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    # 두 버튼을 가로로 배치하고 스타일 적용
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button('홈'):
            st.session_state['page'] = 'home'
            st.experimental_rerun()

    with col2:
        if st.button('INFP에게 맞는 공부법 확인하기'):
            st.session_state['page'] = 'study'
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
            background-color: #3CB371;
            color: black;
            margin-top: 30px
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def show_details_INFJ():
    st.markdown("<h1 style='text-align: center; color: #3CB371;'>특징 및 성향 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #3CB371; color: black; padding: 10px; border-radius: 5px;'>INFJ</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li>내향적이고 조용한
                    <ul>
                        <li>내향적인 성향이 강하며, 혼자만의 시간을 즐깁니다.</li>
                        <li>사람들과의 상호 작용보다는 개인적인 공간에서 에너지를 얻습니다.</li>
                    </ul>
                </li>
                <li>창의적이고 개방적
                    <ul>
                        <li>창의적이고 개방적인 사고를 가지고 있으며, 새로운 경험을 좋아합니다.</li>
                        <li>기존의 틀을 벗어나 자유롭게 사고하며, 미래지향적인 생각을 합니다.</li>
                    </ul>
                </li>
                <li>감정적이며 따뜻한
                    <ul>
                        <li>다른 사람들의 감정과 필요에 민감하며, 이를 이해하고 도우려는 성향이 강합니다.</li>
                        <li>공감 능력이 뛰어나며, 다른 사람들과의 관계에서 따뜻함과 이해를 보여줍니다.</li>
                    </ul>
                </li>
                <li>조직적이고 계획적
                    <ul>
                        <li>체계적이고 조직적인 생활을 선호하며, 계획을 세워 이를 실행하는 데 능숙합니다.</li>
                        <li>규칙과 절차를 중시하며, 안정적이고 예측 가능한 환경을 좋아합니다.</li>
                    </ul>
                </li>
                <li>비전 제시
                    <ul>
                        <li>미래에 대한 명확한 비전을 가지고 있으며, 이를 달성하기 위해 노력합니다.</li>
                        <li>자신의 비전을 통해 다른 사람들에게 영감을 주고, 동기를 부여합니다.</li>
                    </ul>
                </li>
                <li>직관적 통찰력
                    <ul>
                        <li>상황을 직관적으로 이해하고, 문제의 근본 원인을 파악하는 능력이 뛰어납니다.</li>
                        <li>복잡한 문제를 분석하고 해결하는 데 강점을 가지고 있습니다.</li>
                    </ul>
                </li>
                <li>높은 도덕적 기준
                    <ul>
                        <li>도덕적 가치와 윤리를 중시하며, 이를 바탕으로 행동합니다.</li>
                        <li>공정하고 정직한 태도로 사람들과의 관계를 유지합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    # 두 버튼을 가로로 배치하고 스타일 적용
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button('홈'):
            st.session_state['page'] = 'home'
            st.experimental_rerun()

    with col2:
        if st.button('INFJ에게 맞는 공부법 확인하기'):
            st.session_state['page'] = 'study'
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
            background-color: #3CB371;
            color: black;
            margin-top: 30px
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def show_details_INTP():
    st.markdown("<h1 style='text-align: center; color: #9b6cc3;'>특징 및 성향 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #9b6cc3; color: black; padding: 10px; border-radius: 5px;'>INTP</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li>내향적이고 조용한
                    <ul>
                        <li>내향적인 성향이 강하며, 혼자만의 시간을 즐깁니다.</li>
                        <li>사람들과의 상호 작용보다는 개인적인 공간에서 에너지를 얻습니다.</li>
                    </ul>
                </li>
                <li>창의적이고 개방적
                    <ul>
                        <li>창의적이고 개방적인 사고를 가지고 있으며, 새로운 경험을 좋아합니다.</li>
                        <li>기존의 틀을 벗어나 자유롭게 사고하며, 미래지향적인 생각을 합니다.</li>
                    </ul>
                </li>
                <li>논리적이고 분석적
                    <ul>
                        <li>문제를 논리적으로 분석하고, 객관적인 관점에서 판단을 내립니다.</li>
                        <li>상황을 비판적으로 바라보며, 효율적인 해결책을 찾기 위해 노력합니다.</li>
                    </ul>
                </li>
                <li>유연하고 즉흥적
                    <ul>
                        <li>변화에 유연하게 대처하며, 즉흥적으로 행동하는 것을 좋아합니다.</li>
                        <li>계획보다는 순간의 기회를 포착하는 것을 선호합니다.</li>
                    </ul>
                </li>
                <li>지적 호기심
                    <ul>
                        <li>다양한 주제에 대해 호기심이 많으며, 새로운 지식을 탐구하는 것을 좋아합니다.</li>
                        <li>책, 논문, 강연 등을 통해 지속적으로 학습하고 성장합니다.</li>
                    </ul>
                </li>
                <li>추상적 사고
                    <ul>
                        <li>구체적인 사실보다는 추상적이고 이론적인 개념을 다루는 것을 선호합니다.</li>
                        <li>복잡한 이론을 이해하고 설명하는 능력이 뛰어납니다.</li>
                    </ul>
                </li>
                <li>독립적 연구자
                    <ul>
                        <li>독립적으로 연구하고 탐구하는 것을 좋아하며, 자신의 지적 호기심을 충족시킵니다.</li>
                        <li>다른 사람들과의 협력보다는 개인적인 연구를 선호합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    # 두 버튼을 가로로 배치하고 스타일 적용
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button('홈'):
            st.session_state['page'] = 'home'
            st.experimental_rerun()

    with col2:
        if st.button('INTP에게 맞는 공부법 확인하기'):
            st.session_state['page'] = 'study'
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
            color: black;
            margin-top: 30px
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def show_details_INTJ():
    st.markdown("<h1 style='text-align: center; color: #9b6cc3;'>특징 및 성향 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #9b6cc3; color: black; padding: 10px; border-radius: 5px;'>INTJ</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li>내향적이고 조용한
                    <ul>
                        <li>내향적인 성향이 강하며, 혼자만의 시간을 즐깁니다.</li>
                        <li>사람들과의 상호 작용보다는 개인적인 공간에서 에너지를 얻습니다.</li>
                    </ul>
                </li>
                <li>창의적이고 개방적
                    <ul>
                        <li>창의적이고 개방적인 사고를 가지고 있으며, 새로운 경험을 좋아합니다.</li>
                        <li>기존의 틀을 벗어나 자유롭게 사고하며, 미래지향적인 생각을 합니다.</li>
                    </ul>
                </li>
                <li>논리적이고 분석적
                    <ul>
                        <li>문제를 논리적으로 분석하고, 객관적인 관점에서 판단을 내립니다.</li>
                        <li>상황을 비판적으로 바라보며, 효율적인 해결책을 찾기 위해 노력합니다.</li>
                    </ul>
                </li>
                <li>조직적이고 계획적
                    <ul>
                        <li>체계적이고 조직적인 생활을 선호하며, 계획을 세워 이를 실행하는 데 능숙합니다.</li>
                        <li>규칙과 절차를 중시하며, 안정적이고 예측 가능한 환경을 좋아합니다.</li>
                    </ul>
                </li>
                <li>전략적 사고
                    <ul>
                        <li>장기적인 목표를 설정하고, 이를 달성하기 위한 전략을 수립합니다.</li>
                        <li>복잡한 문제를 체계적으로 분석하고, 효과적인 해결책을 찾습니다.</li>
                    </ul>
                </li>
                <li>독립적 연구자
                    <ul>
                        <li>독립적으로 연구하고 탐구하는 것을 좋아하며, 자신의 지적 호기심을 충족시킵니다.</li>
                        <li>다른 사람들과의 협력보다는 개인적인 연구를 선호합니다.</li>
                    </ul>
                </li>
                <li>높은 자신감
                    <ul>
                        <li>자신의 능력과 판단에 대한 강한 자신감을 가지고 있습니다.</li>
                        <li>결정을 내릴 때 확신을 가지고 행동하며, 주저함이 없습니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
        
    # 두 버튼을 가로로 배치하고 스타일 적용
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button('홈'):
            st.session_state['page'] = 'home'
            st.experimental_rerun()

    with col2:
        if st.button('INTJ에게 맞는 공부법 확인하기'):
            st.session_state['page'] = 'study'
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
            color: black;
            margin-top: 30px
        }
        </style>
        """,
        unsafe_allow_html=True
    )


# 공부법
def show_study_ESFP() :
    st.markdown("<h1 style='text-align: center; color: #FFD700;'>공부법 확인하기</h1>", unsafe_allow_html=True)

    # 이미지 섹션

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #FFD700; color: black; padding: 10px; border-radius: 5px;'>ESFP</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li style='font-size:30px; font-weight:bold;'>참여형 학습 방식
                    <ul style='font-size:15px; padding-bottom:30px;'>ESFP들은 활동적이고 사람들과의 상호 작용을 즐기기 때문에, 그룹 스터디나 토론을 통한 학습이 매우 효과적입니다. 이를 통해 적극적으로 참여하고, 자신의 생각을 표현하며, 다른 사람들의 의견을 들으면서 학습 내용을 더욱 깊이 이해할 수 있습니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>스터디 그룹 구성: </span><br> 스터디 그룹을 만들어 정기적으로 모임을 갖습니다. 주제에 대해 토론하고, 서로 질문을 주고받으면서 학습합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>역할극 및 시뮬레이션: </span><br>학습 내용을 실생활에 적용해보는 역할극이나 시뮬레이션을 통해 학습합니다. 이를 통해 이론을 실제 상황에 연결시켜 더 잘 이해할 수 있습니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>게임화된 학습 활동: </span><br>퀴즈, 플래시카드, 학습 게임 등을 통해 재미있게 학습합니다. 게임 요소를 추가하면 학습 동기가 더욱 높아질 수 있습니다.</li>
                    </ul>
                </li>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>실습과 체험을 통한 학습
                    <ul style='font-size:15px;'>ESFP들은 현실적이고 실용적인 접근을 선호하기 때문에, 이론보다는 실제 경험을 통해 배우는 것이 더 효과적입니다. 실습, 프로젝트, 체험 학습을 통해 직접 해보면서 배우는 것이 중요합니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>프로젝트 기반 학습: </span><br>실제 문제를 해결하는 프로젝트를 통해 학습합니다. 이를 통해 실질적인 경험을 쌓고, 문제 해결 능력을 기를 수 있습니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>체험 학습: </span><br>박물관, 전시회, 현장 견학 등 직접 체험할 수 있는 학습 기회를 활용합니다. 이를 통해 학습 내용을 생생하게 이해하고 기억할 수 있습니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>피드백 세션: </span><br>학습한 내용을 다른 사람에게 설명하고 피드백을 받는 시간을 가집니다. 이를 통해 자신의 이해도를 점검하고, 부족한 부분을 보완할 수 있습니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button('홈'):
        st.session_state['page'] = 'home'
        st.experimental_rerun()

def show_study_ESFJ() :
    st.markdown("<h1 style='text-align: center; color: #87CEEB;'>공부법 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #87CEEB; color: black; padding: 10px; border-radius: 5px;'>ESFJ</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li style='font-size:30px; font-weight:bold;'>구조화된 학습 환경
                    <ul style='font-size:15px; padding-bottom:30px;'>ESFJ들은 체계적이고 계획적인 접근 방식을 선호합니다. 따라서 구조화된 학습 계획을 세우고 이를 따르는 것이 매우 효과적입니다. 명확한 일정과 목표를 설정하면 학습 과정에서 더 큰 성취감을 느낄 수 있습니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>학습 계획 작성: </span><br>매주 또는 매일의 학습 목표와 일정을 계획표에 작성합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>타임 테이블 사용: </span><br>시간표를 작성하여 특정 시간대에 어떤 과목이나 주제를 공부할지 명확히 정합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>정기적인 복습: </span><br>일정한 간격으로 배운 내용을 복습하는 시간을 계획에 포함시킵니다.</li>
                    </ul>
                </li>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>협력적 학습 방식
                    <ul style='font-size:15px;'>ESFJ들은 사람들과의 상호 작용을 즐기고, 협력을 통해 학습할 때 더 큰 동기부여를 받습니다. 그룹 스터디나 협동 학습을 통해 다른 사람들과 함께 공부하면 학습 효과를 극대화할 수 있습니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>스터디 그룹 참여: </span><br>비슷한 목표를 가진 친구나 동료와 스터디 그룹을 만들어 정기적으로 모임을 갖습니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>토론과 발표: </span><br>공부한 내용을 그룹 내에서 발표하거나 토론하는 시간을 가지면 이해도를 높일 수 있습니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>상호 피드백: </span><br>학습한 내용을 서로에게 설명하고 피드백을 주고받으면서 학습 내용을 정리하고 강화합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button('홈'):
        st.session_state['page'] = 'home'
        st.experimental_rerun()

def show_study_ESTP() :
    st.markdown("<h1 style='text-align: center; color: #FFD700;'>공부법 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #FFD700; color: black; padding: 10px; border-radius: 5px;'>ESTP</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>실습과 체험을 통한 학습
                    <ul style='font-size:15px;'>ESTP들은 현실적이고 실용적인 접근을 선호하기 때문에, 이론보다는 실제 경험을 통해 배우는 것이 더 효과적입니다. 직접 실습하고 체험하면서 배우는 것이 중요합니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>사례 적용: </span><br>실제 사례를 통해 문제를 해결합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>프로젝트: </span><br>프로젝트 기반 학습을 통해 실질적인 경험을 쌓습니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>현장 학습:  </span><br>현장 학습이나 견학을 통해 직접 보고 느끼며 학습합니다.</li>
                    </ul>
                </li>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>동적이고 활동적인 학습 환경
                    <ul style='font-size:15px;'>ESTP들은 정적인 환경보다는 동적이고 활동적인 환경에서 더 잘 학습합니다. 움직이면서 배우는 활동적인 학습 방법이 효과적입니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>역할극 및 시뮬레이션: </span><br>역할극이나 시뮬레이션을 통해 학습 내용을 실생활에 적용해 봅니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>동적 학습 도구 활용: </span><br>동적 학습 도구를 활용합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>팀 활동: </span><br>팀 활동을 통해 상호작용하며 학습합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button('홈'):
        st.session_state['page'] = 'home'
        st.experimental_rerun()

def show_study_ESTJ() :
    st.markdown("<h1 style='text-align: center; color: #87CEEB;'>공부법 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #87CEEB; color: black; padding: 10px; border-radius: 5px;'>ESTJ</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>구조화된 학습 계획
                    <ul style='font-size:15px;'>ESTJ들은 체계적이고 계획적인 접근 방식을 선호합니다. 명확한 일정과 목표를 설정하고 이를 따르는 것이 효과적입니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>계획 작성: </span><br>매일 또는 매주의 학습 목표와 일정을 계획표에 작성합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>시간표 사용: </span><br>타임 테이블을 사용하여 특정 시간대에 어떤 과목이나 주제를 공부할지 명확히 정합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>정기 복습: </span><br>일정한 간격으로 배운 내용을 복습하는 시간을 계획에 포함시킵니다.</li>
                    </ul>
                </li>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>논리적이고 분석적인 접근
                    <ul style='font-size:15px;'>ESTJ들은 논리적이고 분석적인 접근을 통해 학습 내용을 깊이 이해할 수 있습니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>노트 정리: </span><br>체계적인 노트 필기를 통해 내용을 정리합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>문제 풀이: </span><br>다양한 문제를 풀어보며 문제 해결 능력을 키웁니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>토론: </span><br>학습한 내용을 토론하고 디베이트하며 논리적 사고를 강화합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button('홈'):
        st.session_state['page'] = 'home'
        st.experimental_rerun()

def show_study_ENFP() :
    st.markdown("<h1 style='text-align: center; color: #3CB371;'>공부법 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #3CB371; color: black; padding: 10px; border-radius: 5px;'>ENFP</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>창의적이고 개방적인 학습
                    <ul style='font-size:15px;'>ENFP들은 창의적이고 개방적인 사고를 가지고 있으며, 새로운 경험을 통해 학습하는 것을 좋아합니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>마인드맵: </span><br>마인드맵을 사용하여 학습 내용을 시각적으로 정리하고 연결합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>브레인스토밍: </span><br>브레인스토밍 세션을 통해 새로운 아이디어를 탐구합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>프로젝트: </span><br>프로젝트 기반 학습을 통해 창의적인 프로젝트를 수행합니다.</li>
                    </ul>
                </li>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>협력적 학습 환경
                    <ul style='font-size:15px;'>ENFP들은 사람들과의 상호작용을 즐기며, 협력적인 환경에서 더 잘 학습합니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>스터디 그룹: </span><br>스터디 그룹을 구성하여 정기적으로 모입니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>토론 및 발표: </span><br>학습한 내용을 그룹 내에서 발표하거나 토론합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>피드백: </span><br>서로에게 설명하고 피드백을 주고받는 시간을 가집니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button('홈'):
        st.session_state['page'] = 'home'
        st.experimental_rerun()

def show_study_ENFJ() :
    st.markdown("<h1 style='text-align: center; color: #3CB371;'>공부법 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #3CB371; color: black; padding: 10px; border-radius: 5px;'>ENFJ</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>구조화된 학습 환경
                    <ul style='font-size:15px;'>ENFJ들은 명확한 일정과 목표를 설정하고 이를 따르는 체계적인 학습 방식을 선호합니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>계획 작성: </span><br>학습 계획을 작성하여 계획적으로 학습합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>시간표 사용: </span><br>타임 테이블을 사용하여 특정 과목을 공부할 수 있도록 시간표를 만듭니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>정기 평가: </span><br>자신의 학습 진행 상황을 정기적으로 평가하고 수정합니다.</li>
                    </ul>
                </li>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>협력적 학습 환경
                    <ul style='font-size:15px;'>ENFJ들은 협력적인 환경에서 더 잘 학습하며, 팀워크를 중시합니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>스터디 그룹: </span><br>스터디 그룹을 구성하여 함께 공부합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>토론 및 발표: </span><br>학습 내용을 다른 사람들과 공유하고 토론합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>멘토링: </span><br>멘토나 선생님과 상담하여 학습의 어려운 부분을 해결합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button('홈'):
        st.session_state['page'] = 'home'
        st.experimental_rerun()

def show_study_ENTP() :
    st.markdown("<h1 style='text-align: center; color: #9b6cc3;'>공부법 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #9b6cc3; color: black; padding: 10px; border-radius: 5px;'>ENTP</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>창의적 문제 해결
                    <ul style='font-size:15px;'>ENTP들은 창의적인 접근을 통해 문제를 해결하는 것을 즐기며, 다양한 아이디어를 탐구합니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>브레인스토밍: </span><br>브레인스토밍 세션을 통해 다양한 아이디어를 탐구합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>프로젝트: </span><br>프로젝트 기반 학습을 통해 실제 문제를 해결합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>창의적 접근: </span><br>다양한 접근 방식을 시도하며 창의적인 해결책을 찾습니다.</li>
                    </ul>
                </li>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>논리적이고 분석적인 접근
                    <ul style='font-size:15px;'>ENTP들은 논리적이고 분석적인 접근을 통해 학습 내용을 깊이 이해할 수 있습니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>사례 연구: </span><br>사례 연구를 통해 다양한 상황을 분석하고 해결책을 찾습니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>노트 정리: </span><br>논리적으로 정리된 노트 필기를 통해 내용을 이해합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>토론 및 디베이트: </span><br>토론 및 디베이트를 통해 논리적 사고를 강화합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button('홈'):
        st.session_state['page'] = 'home'
        st.experimental_rerun()

def show_study_ENTJ() :
    st.markdown("<h1 style='text-align: center; color: #9b6cc3;'>공부법 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #9b6cc3; color: black; padding: 10px; border-radius: 5px;'>ENTJ</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>전략적 학습 계획
                    <ul style='font-size:15px;'>ENTJ들은 장기적인 목표를 설정하고 이를 달성하기 위한 전략을 수립하는 것을 선호합니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>목표 설정: </span><br>장기적인 목표를 설정하고 이를 달성하기 위한 전략을 세웁니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>단계별 계획: </span><br>큰 목표를 작은 단계로 나누어 단계별 계획을 세웁니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>성과 평가: </span><br>정기적으로 자신의 성과를 평가하고 필요시 계획을 수정합니다.</li>
                    </ul>
                </li>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>리더십과 협력
                    <ul style='font-size:15px;'>ENTJ들은 리더십을 발휘하며, 협력적인 환경에서 더 잘 학습합니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>팀 프로젝트: </span><br>팀 프로젝트를 구성하여 함께 프로젝트를 수행합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>토론 및 발표: </span><br>학습 내용을 다른 사람들과 공유하고 토론합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>멘토링: </span><br>멘토나 선생님과 상담하여 학습의 어려운 부분을 해결합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button('홈'):
        st.session_state['page'] = 'home'
        st.experimental_rerun()

def show_study_ISFP() :
    st.markdown("<h1 style='text-align: center; color: #FFD700;'>공부법 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #FFD700; color: black; padding: 10px; border-radius: 5px;'>ISFP</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>체험과 실습을 통한 학습
                    <ul style='font-size:15px;'>ISFP들은 현실적이고 실용적인 접근을 선호하며, 직접 체험하고 실습하면서 배우는 것이 효과적입니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>현장 학습: </span><br>박물관, 전시회, 현장 견학 등 직접 체험할 수 있는 학습 기회를 활용합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>실습 및 프로젝트: </span><br>실습과 프로젝트를 통해 실제 문제를 해결합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>예술적 표현: </span><br>예술적 활동을 통해 학습 내용을 창의적으로 표현합니다.</li>
                    </ul>
                </li>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>감각적 학습 환경
                    <ul style='font-size:15px;'>
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>시청각 자료: </span><br>비디오, 오디오 등 다양한 시청각 자료를 활용하여 학습합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>실물 자료: </span><br>실물 자료나 모델을 사용하여 학습 내용을 이해합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>창의적 노트: </span><br>색깔과 그림을 사용하여 노트를 정리합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button('홈'):
        st.session_state['page'] = 'home'
        st.experimental_rerun()

def show_study_ISFJ() :
    st.markdown("<h1 style='text-align: center; color: #87CEEB;'>공부법 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #87CEEB; color: black; padding: 10px; border-radius: 5px;'>ISFJ</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>구조화된 학습 계획
                    <ul style='font-size:15px;'>ISFJ들은 체계적이고 계획적인 접근 방식을 선호하며, 명확한 일정과 목표를 설정하고 이를 따르는 것이 효과적입니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>계획 작성: </span><br>매일 또는 매주의 학습 목표와 일정을 계획표에 작성합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>시간표 사용: </span><br>타임 테이블을 사용하여 특정 시간대에 어떤 과목이나 주제를 공부할지 명확히 정합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>정기 복습: </span><br>일정한 간격으로 배운 내용을 복습하는 시간을 계획에 포함시킵니다.</li>
                    </ul>
                </li>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>조용하고 집중할 수 있는 학습 환경
                    <ul style='font-size:15px;'>ISFJ들은 조용하고 집중할 수 있는 환경에서 더 잘 학습합니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>조용한 공간: </span><br>학습에 집중할 수 있는 조용한 공간을 마련합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>규칙적 휴식: </span><br>규칙적으로 휴식을 취하며 집중력을 유지합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>배경 음악: </span><br>집중을 돕는 잔잔한 음악을 배경으로 활용합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button('홈'):
        st.session_state['page'] = 'home'
        st.experimental_rerun()

def show_study_ISTP() :
    st.markdown("<h1 style='text-align: center; color: #FFD700;'>공부법 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #FFD700; color: black; padding: 10px; border-radius: 5px;'>ISTP</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>실습과 체험을 통한 학습
                    <ul style='font-size:15px;'>ISTP들은 현실적이고 실용적인 접근을 선호하며, 직접 체험하고 실습하면서 배우는 것이 효과적입니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>사례 적용: </span><br>실제 사례를 통해 문제를 해결합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>프로젝트: </span><br>프로젝트 기반 학습을 통해 실질적인 경험을 쌓습니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>현장 학습: </span><br>현장 학습이나 견학을 통해 직접 보고 느끼며 학습합니다.</li>
                    </ul>
                </li>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>독립적인 학습 환경
                    <ul style='font-size:15px;'>ISTP들은 독립적으로 학습하는 것을 선호하며, 자기 주도적으로 학습하는 것이 효과적입니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>자기 주도 학습: </span><br>스스로 학습 목표를 설정하고 독립적으로 학습합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>문제 해결 연습: </span><br>다양한 문제를 풀어보며 문제 해결 능력을 키웁니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>자기 평가: </span><br>학습한 내용을 스스로 평가하고 부족한 부분을 보완합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button('홈'):
        st.session_state['page'] = 'home'
        st.experimental_rerun()

def show_study_ISTJ() :
    st.markdown("<h1 style='text-align: center; color: #87CEEB;'>공부법 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #87CEEB; color: black; padding: 10px; border-radius: 5px;'>ISTJ</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>구조화된 학습 계획
                    <ul style='font-size:15px;'>ISTJ들은 체계적이고 계획적인 접근 방식을 선호하며, 명확한 일정과 목표를 설정하고 이를 따르는 것이 효과적입니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>계획 작성: </span><br>매일 또는 매주의 학습 목표와 일정을 계획표에 작성합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>시간표 사용: </span><br>타임 테이블을 사용하여 특정 시간대에 어떤 과목이나 주제를 공부할지 명확히 정합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>정기 복습: </span><br>일정한 간격으로 배운 내용을 복습하는 시간을 계획에 포함시킵니다.</li>
                    </ul>
                </li>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>논리적이고 분석적인 접근
                    <ul style='font-size:15px;'>ISTJ들은 논리적이고 분석적인 접근을 통해 학습 내용을 깊이 이해할 수 있습니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>노트 정리: </span><br>체계적인 노트 필기를 통해 내용을 정리합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>문제 풀이: </span><br>다양한 문제를 풀어보며 문제 해결 능력을 키웁니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>토론 및 디베이트: </span><br>학습한 내용을 토론하고 디베이트하며 논리적 사고를 강화합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button('홈'):
        st.session_state['page'] = 'home'
        st.experimental_rerun()

def show_study_INFP() :
    st.markdown("<h1 style='text-align: center; color: #3CB371;'>공부법 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #3CB371; color: black; padding: 10px; border-radius: 5px;'>INFP</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>창의적이고 개방적인 학습
                    <ul style='font-size:15px;'>INFP들은 창의적이고 개방적인 사고를 가지고 있으며, 새로운 경험을 통해 학습하는 것을 좋아합니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>마인드맵: </span><br>마인드맵을 사용하여 학습 내용을 시각적으로 정리하고 연결합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>브레인스토밍: </span><br>브레인스토밍 세션을 통해 새로운 아이디어를 탐구합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>프로젝트: </span><br>프로젝트 기반 학습을 통해 창의적인 프로젝트를 수행합니다.</li>
                    </ul>
                </li>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>감성적 학습 환경
                    <ul style='font-size:15px;'>INFP들은 감성적이고 공감 능력이 뛰어나며, 이러한 특성을 활용한 학습이 효과적입니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>감정 표현: </span><br>학습 내용을 예술적 또는 창의적으로 표현합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>저널 작성: </span><br>학습한 내용을 일기나 저널로 작성하여 감정을 기록합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>스토리텔링: </span><br>학습 내용을 이야기 형식으로 구성하여 이해하고 기억합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button('홈'):
        st.session_state['page'] = 'home'
        st.experimental_rerun()

def show_study_INFJ() :
    st.markdown("<h1 style='text-align: center; color: #3CB371;'>공부법 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #3CB371; color: black; padding: 10px; border-radius: 5px;'>INFJ</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>구조화된 학습 계획
                    <ul style='font-size:15px;'>INFJ들은 체계적이고 계획적인 접근 방식을 선호하며, 명확한 일정과 목표를 설정하고 이를 따르는 것이 효과적입니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>계획 작성: </span><br>매일 또는 매주의 학습 목표와 일정을 계획표에 작성합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>시간표 사용: </span><br>타임 테이블을 사용하여 특정 시간대에 어떤 과목이나 주제를 공부할지 명확히 정합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>정기 평가: </span><br>자신의 학습 진행 상황을 정기적으로 평가하고 수정합니다.</li>
                    </ul>
                </li>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>협력적 학습 환경
                    <ul style='font-size:15px;'>INFJ들은 사람들과의 협력을 통해 학습할 때 더 큰 동기부여를 받습니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>스터디 그룹: </span><br> 스터디 그룹을 구성하여 정기적으로 모입니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>토론 및 발표: </span><br>학습한 내용을 그룹 내에서 발표하거나 토론합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>멘토링: </span><br>멘토나 선생님과 상담하여 학습의 어려운 부분을 해결합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button('홈'):
        st.session_state['page'] = 'home'
        st.experimental_rerun()

def show_study_INTP() :
    st.markdown("<h1 style='text-align: center; color: #9b6cc3;'>공부법 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #9b6cc3; color: black; padding: 10px; border-radius: 5px;'>INTP</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>창의적 문제 해결
                    <ul style='font-size:15px;'>INTP들은 창의적인 접근을 통해 문제를 해결하는 것을 즐기며, 다양한 아이디어를 탐구합니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>브레인스토밍: </span><br>브레인스토밍 세션을 통해 다양한 아이디어를 탐구합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>프로젝트: </span><br>프로젝트 기반 학습을 통해 실제 문제를 해결합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>창의적 접근: </span><br>다양한 접근 방식을 시도하며 창의적인 해결책을 찾습니다.</li>
                    </ul>
                </li>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>논리적이고 분석적인 접근
                    <ul style='font-size:15px;'>INTP들은 논리적이고 분석적인 접근을 통해 학습 내용을 깊이 이해할 수 있습니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>사례 연구: </span><br>사례 연구를 통해 다양한 상황을 분석하고 해결책을 찾습니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>노트 정리: </span><br>논리적으로 정리된 노트 필기를 통해 내용을 이해합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>토론 및 디베이트: </span><br>토론 및 디베이트를 통해 논리적 사고를 강화합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button('홈'):
        st.session_state['page'] = 'home'
        st.experimental_rerun()

def show_study_INTJ() :
    st.markdown("<h1 style='text-align: center; color: #9b6cc3;'>공부법 확인하기</h1>", unsafe_allow_html=True)

    # 텍스트와 스타일 섹션
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='width:100px; height:60px; background-color: #9b6cc3; color: black; padding: 10px; border-radius: 5px;'>INTJ</h2>
        </div>
        <div style='margin-top: 30px; font-size: 18px;'>
            <ul>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>전략적 학습 계획
                    <ul style='font-size:15px;'>INTJ들은 장기적인 목표를 설정하고 이를 달성하기 위한 전략을 수립하는 것을 선호합니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>목표 설정: </span><br>장기적인 목표를 설정하고 이를 달성하기 위한 전략을 세웁니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>단계별 계획: </span><br>큰 목표를 작은 단계로 나누어 단계별 계획을 세웁니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>성과 평가: </span><br>정기적으로 자신의 성과를 평가하고 필요시 계획을 수정합니다.</li>
                    </ul>
                </li>
                <li style='font-size:30px; font-weight:bold; margin-top:30px;'>독립적 학습
                    <ul style='font-size:15px;'>INTJ들은 독립적으로 학습하는 것을 선호하며, 자기 주도적으로 학습하는 것이 효과적입니다.
                        <li style='padding-top:30px; font-size:20px;'><span style='font-weight: bold; font-size:22px;'>자기 주도 학습: </span><br>스스로 학습 목표를 설정하고 독립적으로 학습합니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>문제 해결 연습: </span><br>다양한 문제를 풀어보며 문제 해결 능력을 키웁니다.</li>
                        <li style='font-size:20px;'><span style='font-weight: bold; font-size:22px;'>독서와 연구: </span><br>학습한 내용을 독서와 연구를 통해 깊이 탐구합니다.</li>
                    </ul>
                </li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button('홈'):
        st.session_state['page'] = 'home'
        st.experimental_rerun()

def mbti_details():
    # 'mbti_result' 키가 존재하는지 확인하고 기본값을 설정
    mbti_result = st.session_state.get('mbti_result', None)
    
    # 'mbti_result'가 'ESFP'일 때만 show_details_ESFP() 함수 실행
    if mbti_result == 'ESFP':
        show_details_ESFP()
    elif mbti_result == 'ESFJ':
        show_details_ESFJ()
    elif mbti_result == 'ESTP':
        show_details_ESTP()
    elif mbti_result == 'ESTJ':
        show_details_ESTJ()
    elif mbti_result == 'ENFP':
        show_details_ENFP()
    elif mbti_result == 'ENFJ':
        show_details_ENFJ()
    elif mbti_result == 'ENTP':
        show_details_ENTP()
    elif mbti_result == 'ENTJ':
        show_details_ENTJ()
    elif mbti_result == 'ISFP':
        show_details_ISFP()
    elif mbti_result == 'ISFJ':
        show_details_ISFJ()
    elif mbti_result == 'ISTP':
        show_details_ISTP()
    elif mbti_result == 'ISTJ':
        show_details_ISTJ()
    elif mbti_result == 'INFP':
        show_details_INFP()
    elif mbti_result == 'INFJ':
        show_details_INFJ()
    elif mbti_result == 'INTP':
        show_details_INTP()
    elif mbti_result == 'INTJ':
        show_details_INTJ()
        
def mbti_study() :
    # 'mbti_result' 키가 존재하는지 확인하고 기본값을 설정
    mbti_result = st.session_state.get('mbti_result', None)
    
    # 'mbti_result'가 'ESFP'일 때만 show_details_ESFP() 함수 실행
    if mbti_result == 'ESFP':
        show_study_ESFP()
    elif mbti_result == 'ESFJ':
        show_study_ESFJ()
    elif mbti_result == 'ESTP':
        show_study_ESTP()
    elif mbti_result == 'ESTJ':
        show_study_ESTJ()
    elif mbti_result == 'ENFP':
        show_study_ENFP()
    elif mbti_result == 'ENFJ':
        show_study_ENFJ()
    elif mbti_result == 'ENTP':
        show_study_ENTP()
    elif mbti_result == 'ENTJ':
        show_study_ENTJ()
    elif mbti_result == 'ISFP':
        show_study_ISFP()
    elif mbti_result == 'ISFJ':
        show_study_ISFJ()
    elif mbti_result == 'ISTP':
        show_study_ISTP()
    elif mbti_result == 'ISTJ':
        show_study_ISTJ()
    elif mbti_result == 'INFP':
        show_study_INFP()
    elif mbti_result == 'INFJ':
        show_study_INFJ()
    elif mbti_result == 'INTP':
        show_study_INTP()
    elif mbti_result == 'INTJ':
        show_study_INTJ()
    else :
        if st.button('홈'):
            st.session_state['page'] = 'home'
            st.experimental_rerun()
            
        st.write("아직 결과가 저장되지 않았습니다. 먼저 MBTI 검사를 완료하세요.")
        


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
elif st.session_state['page'] == 'study':
    mbti_study()