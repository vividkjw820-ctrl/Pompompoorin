import streamlit as st
import random

def generate_lotto_numbers(num_sets):
    """
    지정된 횟수만큼 로또 번호 (1부터 45 중 중복 없이 6개)를 생성합니다.
    """
    lotto_results = []
    for _ in range(num_sets):
        # 1부터 45까지의 숫자 리스트에서 중복 없이 6개의 숫자를 무작위로 선택
        numbers = sorted(random.sample(range(1, 46), 6))
        lotto_results.append(numbers)
    return lotto_results

# Streamlit 앱의 제목 설정
st.title('로또 번호 생성기 🎰')
st.markdown('1부터 45 사이의 숫자 중 6개의 숫자를 무작위로 생성합니다.')

# 사용자로부터 몇 세트의 로또 번호를 생성할지 입력받음
num_set
