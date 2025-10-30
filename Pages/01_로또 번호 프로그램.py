# lotto_app.py
import streamlit as st
import random
import requests
from bs4 import BeautifulSoup

def fetch_latest_numbers():
    """최근 회차 당첨번호를 크롤링하거나 API로 가져오기 (간단히 웹스크래핑)"""
    try:
        url = "https://www.lotteryextreme.com/southkorea/lotto645/results"
        resp = requests.get(url)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        # 웹페이지 구조에 따라 파싱 — 예시는 최근 회차 첫번째 데이터 가져오기
        # 여기서는 간단히 숫자 6개만 리스트로 가져오고 보너스는 제외
        # 실제 구조에 맞춰 조정 필요
        results = soup.select_one("div.latest‐results")  # 구조 예시
        # (아래는 예시 코드)
        nums = [int(x.text) for x in results.select("span.number")[:6]]
        return nums
    except Exception as e:
        st.error(f"최신 당첨번호를 가져오는 데 실패했습니다: {e}")
        return None

def generate_sets(num_sets: int):
    sets = []
    for _ in range(num_sets):
        s = sorted(random.sample(range(1, 46), 6))
        sets.append(s)
    return sets

def compare_with_latest(generated_sets, latest_nums):
    comparison = []
    set_latest = set(latest_nums)
    for s in generated_sets:
        matched = set(s) & set_latest
        comparison.append({"set": s, "match_count": len(matched), "matched_nums": sorted(matched)})
    return comparison

def main():
    st.title("로또 번호 추천 및 비교 앱")
    st.write("1부터 45까지 중 6개의 숫자로 구성된 로또 번호를 추천해주고, 최근 당첨번호와 비교해줍니다.")

    num_sets = st.number_input("몇 세트 생성할까요?", min_value=1, max_value=20, value=1, step=1)
    if st.button("생성"):
        generated = generate_sets(num_sets)
        st.write("추천 번호:")
        for idx, s in enumerate(generated, start=1):
            st.write(f"세트 {idx}: {s}")

        latest = fetch_latest_numbers()
        if latest:
            st.write(f"최근 당첨번호: {latest}")
            comparison = compare_with_latest(generated, latest)
            st.write("비교 결과:")
            for idx, comp in enumerate(comparison, start=1):
                st.write(
                    f"세트 {idx}: {comp['set']} → 맞춘 개수 {comp['match_count']} 개, 맞춘 숫자: {comp['matched_nums']}"
                )
        else:
            st.write("최근 당첨번호를 가져올 수 없어 비교를 생략합니다.")

if __name__ == "__main__":
    main()
