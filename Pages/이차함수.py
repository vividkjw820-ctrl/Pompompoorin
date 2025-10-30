import streamlit as st
import random
import pandas as pd

# 로또 번호를 생성하는 함수 (1부터 45까지 중 6개의 고유한 숫자)
def generate_lotto_numbers():
    """1부터 45까지 중 6개의 고유한 로또 번호를 생성하여 정렬된 리스트로 반환"""
    # random.sample(population, k) : 모집단(1~45)에서 6개의 고유한 샘플 추출
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()
    return numbers

# Streamlit 앱 시작
st.set_page_config(page_title="🍀 로또 번호 추첨기", layout="centered")

st.title("🍀 로또 번호 추첨기")
st.markdown("1부터 45까지의 숫자 중 6개의 행운 번호를 생성합니다.")

# --- 사용자 입력 섹션 ---
st.subheader("1. 추첨 설정")
# st.selectbox 대신 st.number_input을 사용하여 사용자에게 세트 수를 입력받습니다.
num_sets = st.number_input(
    '몇 세트의 번호를 생성하시겠습니까?',
    min_value=1, 
    max_value=10, 
    value=5, 
    step=1,
    key='num_sets'
)

# 번호 생성 버튼
generate_button = st.button("✨ 행운 번호 생성하기")

# --- 번호 생성 및 표시 섹션 ---
st.subheader("2. 생성된 행운 번호")

# 버튼을 눌렀을 때만 번호를 생성하고 표시합니다.
if generate_button:
    st.info(f"선택하신 **{num_sets}세트**의 로또 번호를 생성했습니다.")
    
    # 결과를 담을 DataFrame 생성
    results_data = []
    
    for i in range(1, num_sets + 1):
        numbers = generate_lotto_numbers()
        # 번호 리스트를 DataFrame에 넣기 위해 쉼표로 구분된 문자열로 변환
        results_data.append({
            '세트': f'No. {i}',
            '번호': ", ".join(map(str, numbers)),
            '숫자 합': sum(numbers)
        })

    # 결과를 데이터프레임으로 표시
    results_df = pd.DataFrame(results_data)
    st.dataframe(results_df, hide_index=True, use_container_width=True)

# --- 당첨 번호 비교 섹션 ---
st.subheader("3. 최근 당첨 번호 비교 (예시)")

st.warning("주의: Streamlit은 실시간 데이터를 가져오기 어려워 **임의의 최근 당첨 번호**를 예시로 사용했습니다.")

# 사용자 정의 함수: 생성된 번호와 당첨 번호를 비교하여 일치하는 개수를 반환
def compare_numbers(generated, winning):
    # 문자열을 정수 리스트로 변환 (예: "1, 10, 20" -> [1, 10, 20])
    generated_list = list(map(int, generated.split(', ')))
    
    # 두 리스트의 교집합(겹치는 번호)의 개수를 계산
    matches = len(set(generated_list) & set(winning))
    return matches

# 임의의 최근 로또 당첨 번호 (실제 데이터 아님)
# 실제 앱에서는 API 등을 이용해 최신 데이터를 가져와야 합니다.
example_winning_numbers = [5, 12, 18, 25, 33, 40]
example_bonus_number = 7

# 당첨 번호 시각화
st.markdown(f"""
최근 당첨 번호: 
**{example_winning_numbers[0]} {example_winning_numbers[1]} {example_winning_numbers[2]} {example_winning_numbers[3]} {example_winning_numbers[4]} {example_winning_numbers[5]}** 보너스: **{example_bonus_number}**
""")

# 생성 버튼이 눌렸고 결과 DataFrame이 있다면 비교를 수행
if generate_button and 'results_df' in locals():
    
    comparison_data = []
    
    for index, row in results_df.iterrows():
        generated_numbers_str = row['번호']
        
        # 일치하는 번호 개수 확인
        matches = compare_numbers(generated_numbers_str, example_winning_numbers)
        
        # 당첨 여부 메시지
        if matches == 6:
            result_text = "🎉 1등 당첨! 🎉"
        elif matches == 5:
            # 보너스 번호 일치 여부 추가 확인 로직 (옵션)
            generated_list = list(map(int, generated_numbers_str.split(', ')))
            if example_bonus_number in generated_list:
                result_text = "🥈 2등 당첨! (5개 + 보너스)"
            else:
                result_text = "🥉 3등 당첨! (5개 일치)"
        elif matches == 4:
            result_text = "4등 당첨! (4개 일치)"
        elif matches == 3:
            result_text = "5등 당첨! (3개 일치)"
        else:
            result_text = "낙첨 (다음 기회에...)"

        comparison_data.append({
            '세트': row['세트'],
            '생성 번호': generated_numbers_str,
            '일치 개수': matches,
            '결과': result_text
        })
        
    comparison_df = pd.DataFrame(comparison_data)
    st.subheader("당첨 번호 시뮬레이션 결과")
    st.dataframe(comparison_df, hide_index=True, use_container_width=True)

# --- 앱 실행 방법 안내 ---
st.markdown("---")
st.caption("앱 실행 방법: 터미널에서 `streamlit run lotto_app.py` 명령어를 입력하세요.")
