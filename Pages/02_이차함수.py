import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- Streamlit 앱 설정 ---
st.set_page_config(page_title="📐 이차함수의 표준형($y=a(x-p)^2+q$) 그래프 학습", layout="wide")

st.title("Parabola Explorer: 이차함수 표준형 그래프 학습")
st.markdown("슬라이더를 조작하여 이차함수 $y = a(x-p)^2 + q$의 **$a, p, q$ 값**이 그래프에 어떤 영향을 미치는지 확인해 보세요.")

# --- 슬라이더를 이용한 계수 입력 ---
st.sidebar.header("계수(Coefficient) 설정")

# a 값 설정 (그래프의 모양과 폭 결정)
a = st.sidebar.slider(
    'a 값 (그래프의 모양/폭)',
    min_value=-2.0,
    max_value=2.0,
    value=1.0,
    step=0.1
)

# p 값 설정 (x축 평행 이동, 대칭축 결정)
p = st.sidebar.slider(
    'p 값 (x축 평행 이동)',
    min_value=-5.0,
    max_value=5.0,
    value=0.0,
    step=0.1
)

# q 값 설정 (y축 평행 이동, 꼭짓점의 y좌표 결정)
q = st.sidebar.slider(
    'q 값 (y축 평행 이동)',
    min_value=-5.0,
    max_value=5.0,
    value=0.0,
    step=0.1
)

# --- 계산 및 그래프 생성 ---
# x 범위 설정
x = np.linspace(-10, 10, 400)

# 이차함수 표준형 계산: y = a(x-p)^2 + q
y = a * (x - p)**2 + q

# 꼭짓점 좌표
vertex_x = p
vertex_y = q

# 현재 함수식 문자열 생성
function_str = f"$y = {a}(x - {p})^{2} + {q}$"

# --- 결과 출력 ---
col1, col2 = st.columns([3, 2])

with col1:
    st.subheader("그래프 시각화")
    
    # Plotly를 사용하여 그래프 생성
    fig = go.Figure()
    
    # 이차함수 그래프
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode='lines',
        name=f'y = {a}(x - {p})^2 + {q}',
        line=dict(color='royalblue', width=2)
    ))
    
    # 꼭짓점 표시
    fig.add_trace(go.Scatter(
        x=[vertex_x],
        y=[vertex_y],
        mode='markers',
        name=f'꼭짓점 ({vertex_x}, {vertex_y})',
        marker=dict(color='red', size=10)
    ))

    # 대칭축(Symmetry Axis) 표시
    fig.add_trace(go.Scatter(
        x=[vertex_x, vertex_x],
        y=[-10, 10],  # y축 범위에 맞게 조정
        mode='lines',
        name=f'대칭축 (x = {vertex_x})',
        line=dict(color='gray', dash='dash')
    ))

    # 그래프 레이아웃 설정
    fig.update_layout(
        xaxis_title="x",
        yaxis_title="y",
        xaxis=dict(range=[-10, 10]), # x축 범위 고정
        yaxis=dict(range=[-10, 10]), # y축 범위 고정
        height=500,
        title={
            'text': f"이차함수 그래프: {function_str}",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'}
    )
    
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("분석 결과")
    
    # 현재 함수식 표시
    st.markdown(f"**현재 함수식:** {function_str}")
    
    # 꼭짓점 좌표 표시
    st.markdown(f"**꼭짓점 좌표:** $({vertex_x}, {vertex_y})$")
    
    # 대칭축 표시
    st.markdown(f"**대칭축 방정식:** $x = {vertex_x}$")

    st.markdown("---")
    
    # 각 계수의 역할 설명
    st.markdown("#### 계수의 역할")
    
    st.markdown(
        f"""
        1. **$a$ (현재 값: `{a}`):**
           - **부호**는 그래프의 **방향**을 결정합니다 ($a>0$ 아래로 볼록, $a<0$ 위로 볼록).
           - **절댓값**은 그래프의 **폭**을 결정합니다 ($|a|$가 클수록 폭이 좁아집니다).
        2. **$p$ (현재 값: `{p}`):**
           - 그래프를 **x축 방향으로** 평행 이동시킵니다.
           - **대칭축**의 방정식은 $x = p$ 입니다.
        3. **$q$ (현재 값: `{q}`):**
           - 그래프를 **y축 방향으로** 평행 이동시킵니다.
           - 꼭짓점의 **y좌표**와 같습니다.
        """
    )

st.markdown("---")
st.caption("앱 실행 방법: 터미널에서 `streamlit run quadratic_app.py` 명령어를 입력하세요.")
