import streamlit as st
from sympy import symbols, parse_expr, simplify, together

# --- Streamlit 앱 설정 ---
st.set_page_config(page_title="➗ 고1 공통수학: 유리식의 연산 학습", layout="centered")

st.title("➗ 유리식의 연산 학습 앱")
st.markdown("두 유리식 $A$와 $B$를 입력하고 원하는 연산을 선택하여 결과를 확인하세요.")
st.markdown("**SymPy** 라이브러리를 사용해 통분, 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 보여줍니다.")

# 'x'를 SymPy 심볼로 정의
x = symbols('x')

# --- 사용자 입력 ---
st.sidebar.header("유리식 입력")

# 유리식 A 입력 (예: (x+1)/(x-2))
expr_A_str = st.sidebar.text_input(
    '유리식 A (예: (x**2 - 1) / (x + 3))',
    value='(x**2 - 1) / (x + 3)'
)

# 유리식 B 입력
expr_B_str = st.sidebar.text_input(
    '유리식 B (예: (x)/(x+2))',
    value='(x + 1) / (x - 3)'
)

# 연산 선택
operation = st.selectbox(
    '수행할 연산을 선택하세요',
    ('덧셈 (A + B)', '뺄셈 (A - B)', '곱셈 (A * B)', '나눗셈 (A / B)')
)

# --- 연산 및 결과 출력 ---

try:
    # 문자열을 SymPy 수식 객체로 변환
    expr_A = parse_expr(expr_A_str, local_dict={'x': x})
    expr_B = parse_expr(expr_B_str, local_dict={'x': x})

    st.markdown("---")
    st.subheader("입력된 유리식")
    st.latex(f"A = {expr_A}")
    st.latex(f"B = {expr_B}")
    st.markdown("---")

    result_expr = None
    operation_symbol = ""
    
    if operation == '덧셈 (A + B)':
        operation_symbol = "+"
        # together: 분모를 통분하여 하나의 분수로 만듦
        result_expr = together(expr_A + expr_B)
    elif operation == '뺄셈 (A - B)':
        operation_symbol = "-"
        result_expr = together(expr_A - expr_B)
    elif operation == '곱셈 (A * B)':
        operation_symbol = "*"
        # simplify: 곱셈 후 약분까지 시도
        result_expr = simplify(expr_A * expr_B)
    elif operation == '나눗셈 (A / B)':
        operation_symbol = "/"
        # simplify: 나눗셈(곱하기 역수) 후 약분까지 시도
        result_expr = simplify(expr_A / expr_B)
        
    # 결과 출력
    if result_expr is not None:
        st.subheader(f"✅ 연산 결과: {operation.split('(')[0].strip()}")
        
        # 1. 연산 과정을 수식으로 보여줌
        st.markdown(f"**{operation.split('(')[1][:-1].replace(' ', '')} 연산:**")
        st.latex(f"{expr_A} {operation_symbol} {expr_B} = {result_expr}")
        
        # 2. 결과 식을 가장 단순화된 형태로 보여줌 (자동 약분)
        simplified_result = simplify(result_expr)
        
        st.markdown("**최종 약분된 형태:**")
        st.latex(simplified_result)
        
        st.caption("SymPy 라이브러리는 통분 및 약분을 자동으로 수행합니다.")

except Exception as e:
    st.error("⚠️ 수식 입력 오류! 입력한 수식이 올바른 형태인지 확인해 주세요.")
    st.caption("예시: $x^2$는 `x**2`, $\frac{x+1}{x-2}$는 `(x+1)/(x-2)`")
    # st.exception(e) # 개발자용 오류 메시지는 숨기고 간단히 표시

st.markdown("---")
st.caption("앱 실행 방법: 터미널에서 `streamlit run rational_expression_app.py` 명령어를 입력하세요.")
