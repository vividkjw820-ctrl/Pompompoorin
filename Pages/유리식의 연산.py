import streamlit as st

# --- Streamlit 앱 설정 ---
st.set_page_config(page_title="➗ 유리식 연산 (SymPy 없음)", layout="centered")

st.title("➗ 유리식 연산 학습 (수동 계산)")
st.markdown("SymPy 없이 파이썬 기본 기능만 사용합니다. **결과 계산은 직접 하셔야 합니다.**")

# --- 사용자 입력 ---
st.sidebar.header("유리식 입력")

# 유리식 A 입력
expr_A_str = st.sidebar.text_input(
    '유리식 A (예: (x+1)/(x-2))',
    value='\\frac{x+1}{x-2}'  # LaTeX 형식으로 기본값 설정
)

# 유리식 B 입력
expr_B_str = st.sidebar.text_input(
    '유리식 B (예: (x)/(x+2))',
    value='\\frac{x}{x+2}'    # LaTeX 형식으로 기본값 설정
)

# 연산 선택
operation_option = st.selectbox(
    '수행할 연산을 선택하세요',
    ('덧셈 (A + B)', '뺄셈 (A - B)', '곱셈 (A * B)', '나눗셈 (A / B)')
)

# --- 연산 표시 ---

st.markdown("---")
st.subheader("입력된 유리식")
st.latex(f"A = {expr_A_str}")
st.latex(f"B = {expr_B_str}")
st.markdown("---")


# 선택된 연산에 따라 수식 기호 설정
if operation_option == '덧셈 (A + B)':
    op_symbol = '+'
    result_title = "덧셈"
elif operation_option == '뺄셈 (A - B)':
    op_symbol = '-'
    result_title = "뺄셈"
elif operation_option == '곱셈 (A * B)':
    op_symbol = '\\times' # LaTeX 곱셈 기호
    result_title = "곱셈"
elif operation_option == '나눗셈 (A / B)':
    op_symbol = '\\div'   # LaTeX 나눗셈 기호
    result_title = "나눗셈"
else:
    op_symbol = ''
    result_title = ''

# 결과 출력 섹션
st.subheader(f"✅ 연산 과정 시각화: {result_title}")

# 연산 전체를 LaTeX 수식으로 표시 (SymPy 없이 문자열 조합)
st.latex(f"{expr_A_str} {op_symbol} {expr_B_str} = \quad \text{{직접 계산하세요}}")

st.info("이 앱은 입력된 수식을 기반으로 연산 형태만 보여줍니다. **통분, 계산, 약분 과정은 학습자가 직접 수행**해야 합니다.")

# --- 추가 학습 가이드 ---
if operation_option in ('덧셈 (A + B)', '뺄셈 (A - B)'):
    st.markdown("#### 💡 덧셈/뺄셈 학습 가이드")
    st.markdown("1. 두 유리식의 **분모를 통분**합니다.")
    st.markdown("2. 통분된 분모를 바탕으로 **분자끼리 덧셈/뺄셈**을 수행합니다.")
    st.markdown("3. 최종 결과를 **인수분해하여 약분**할 수 있는지 확인합니다.")

elif operation_option in ('곱셈 (A * B)', '나눗셈 (A / B)'):
    st.markdown("#### 💡 곱셈/나눗셈 학습 가이드")
    if operation_option == '나눗셈 (A / B)':
        st.markdown("1. 나눗셈은 **역수를 곱하는 것**으로 바꿉니다.")
    st.markdown("2. 분자는 분자끼리, 분모는 분모끼리 **곱셈**합니다.")
    st.markdown("3. 최종 결과를 **인수분해하여 약분**할 수 있는지 확인합니다.")


st.markdown("---")
st.caption("앱 실행 방법: 터미널에서 `streamlit run rational_no_sympy_app.py` 명령어를 입력하세요.")
