
import streamlit as st

def initialize_session_state():
    """
    세션 상태를 초기화하는 함수.
    앱이 처음 실행되거나 '다시하기' 버튼을 누를 때 호출됩니다.
    """
    # 각 동물 유형에 대한 점수를 0으로 초기화
    st.session_state.scores = {
        '사자': 0,
        '돌고래': 0,
        '부엉이': 0,
        '강아지': 0
    }
    # 설문 결과 제출 여부를 False로 초기화
    st.session_state.submitted = False
    # 각 문항의 답변을 저장할 리스트 초기화
    st.session_state.answers = [None] * 6

def calculate_result(answers):
    """
    사용자의 답변을 기반으로 각 동물 유형의 점수를 계산하는 함수.
    """
    # 점수 초기화
    scores = {'사자': 0, '돌고래': 0, '부엉이': 0, '강아지': 0}

    # 각 질문에 대한 답변이 어떤 동물 유형에 해당하는지 정의
    # (질문 순서, 답변 선택지) -> 동물 유형
    score_mapping = {
        (0, 'A'): '사자', (0, 'B'): '부엉이',
        (1, 'A'): '돌고래', (1, 'B'): '강아지',
        (2, 'A'): '부엉이', (2, 'B'): '돌고래',
        (3, 'A'): '강아지', (3, 'B'): '사자',
        (4, 'A'): '사자', (4, 'B'): '부엉이',
        (5, 'A'): '강아지', (5, 'B'): '돌고래',
    }

    # 답변 리스트를 순회하며 점수 계산
    for i, answer in enumerate(answers):
        if answer is not None:
            animal = score_mapping.get((i, answer[0])) # 답변은 "A. ..." 형태이므로 첫 글자만 사용
            if animal:
                scores[animal] += 1

    return scores

def display_result(animal_type):
    """
    결과로 나온 동물 유형에 대한 정보와 이미지를 화면에 표시하는 함수.
    """
    animal_info = {
        '사자': {
            'description': "당신은 타고난 리더입니다! 용감하고 자신감이 넘치며, 무리를 이끄는 것을 좋아합니다. 때로는 카리스마로 주변을 압도하기도 하지만, 책임감 강한 모습이 당신의 가장 큰 매력입니다.",
            'image': "https://i.imgur.com/v2V5v1h.png" # 간단한 사자 아이콘 이미지
        },
        '돌고래': {
            'description': "당신은 사교적이고 활발한 모험가입니다! 새로운 친구들을 사귀는 것을 좋아하고, 긍정적인 에너지로 주변을 밝게 만듭니다. 지적인 호기심이 많아 새로운 것을 배우는 데 큰 즐거움을 느낍니다.",
            'image': "https://i.imgur.com/uG2Zt7d.png" # 간단한 돌고래 아이콘 이미지
        },
        '부엉이': {
            'description': "당신은 지혜롭고 통찰력 있는 사색가입니다. 혼자만의 시간을 즐기며 깊이 생각하는 것을 좋아합니다. 신중하고 관찰력이 뛰어나, 다른 사람들이 놓치는 부분을 발견해내곤 합니다.",
            'image': "https://i.imgur.com/qL3a6Q0.png" # 간단한 부엉이 아이콘 이미지
        },
        '강아지': {
            'description': "당신은 따뜻하고 다정한 동반자입니다! 사람들과 깊은 유대감을 형성하는 것을 중요하게 생각하며, 주변 사람들에게 무한한 신뢰와 애정을 줍니다. 함께 있을 때 가장 큰 행복을 느끼는 유형입니다.",
            'image': "https://i.imgur.com/wIY20kS.png" # 간단한 강아지 아이콘 이미지
        }
    }

    info = animal_info[animal_type]
    st.subheader(f"당신과 잘 맞는 동물은... {animal_type}!")
    st.image(info['image'], width=150)
    st.write(info['description'])


# --- 앱 UI 구성 ---

st.title("나와 잘 맞는 동물 찾기")

# 세션 상태가 초기화되지 않았다면 초기화 실행
if 'scores' not in st.session_state:
    initialize_session_state()

# 설문 문항 정의
questions = [
    "1. 주말에 친구들과의 약속이 취소되었다면?",
    "2. 새로운 사람들을 만나는 자리에 가게 된다면?",
    "3. 해결하기 어려운 문제가 생겼을 때, 당신의 첫 반응은?",
    "4. 팀 프로젝트를 할 때 당신이 선호하는 역할은?",
    "5. 휴가를 보낸다면 어떤 방식이 더 좋나요?",
    "6. 당신에게 더 중요한 가치는 무엇인가요?"
]

# 설문 답변 선택지 정의
options = [
    ["A. 아쉬워하며 다른 친구에게 연락해본다.", "B. 잘됐다! 집에서 조용히 시간을 보낸다."],
    ["A. 신난다! 먼저 다가가 말을 건다.", "B. 조금 어색하지만, 누가 말을 걸어주길 기다린다."],
    ["A. 일단 차분히 정보를 수집하고 분석한다.", "B. 다른 사람들과 함께 이야기하며 해결책을 찾는다."],
    ["A. 의견을 조율하고 발표하는 리더 역할", "B. 묵묵히 내게 주어진 일을 처리하는 팀원 역할"],
    ["A. 활동적인 액티비티를 즐기는 여행", "B. 아름다운 경치를 보며 쉬는 힐링 여행"],
    ["A. 다른 사람들과의 깊은 관계와 조화", "B. 새로운 경험과 지적인 탐구"]
]

# 설문 결과가 제출되지 않은 경우에만 질문을 표시
if not st.session_state.submitted:
    with st.form("personality_test_form"):
        # 각 질문에 대해 라디오 버튼 생성
        for i in range(len(questions)):
            st.session_state.answers[i] = st.radio(
                questions[i],
                options[i],
                key=f'q{i}',
                # horizontal=True # 가로 정렬 옵션 (필요 시 주석 해제)
            )
        
        # '제출' 버튼
        submitted = st.form_submit_button("결과 확인하기")

        # 제출 버튼이 눌리면
        if submitted:
            # 모든 질문에 답변했는지 확인
            if None in st.session_state.answers:
                st.warning("모든 질문에 답변해주세요!")
            else:
                # 점수를 계산하고 세션 상태 업데이트
                st.session_state.scores = calculate_result(st.session_state.answers)
                st.session_state.submitted = True
                # 앱을 다시 실행하여 결과 페이지를 표시
                st.rerun()

# 설문 결과가 제출된 경우
else:
    # 가장 높은 점수를 받은 동물 찾기
    # 점수가 동점일 경우, 키(동물 이름) 순서로 첫 번째 동물을 선택
    final_animal = max(st.session_state.scores, key=st.session_state.scores.get)
    
    # 결과 표시
    display_result(final_animal)
    
    # '다시하기' 버튼
    if st.button("다시하기"):
        # 세션 상태를 초기화하고 앱을 다시 실행하여 첫 화면으로 돌아감
        initialize_session_state()
        st.rerun()