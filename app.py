import streamlit as st
import pandas as pd
import plotly.express as px


# ------------------------------------------
# 기본 설정
# ------------------------------------------

st.set_page_config(
    page_title="종합일간지 익명표현 분석",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ------------------------------------------
# 스타일
# ------------------------------------------

st.markdown("""
<style>

.block-container {
    max-width: 1200px;
    padding-top: 2.5rem;
    padding-bottom: 4rem;
}

h1 {
    font-size: 2.6rem !important;
    font-weight: 750 !important;
}

h2 {
    margin-top: 2.5rem !important;
}

[data-testid="stMetric"] {
    background-color: #fafafa;
    border: 1px solid #e8e8e8;
    border-radius: 12px;
    padding: 18px;
}

.insight-box {
    padding: 18px 22px;
    border-radius: 12px;
    background-color: #f8f9fa;
    border: 1px solid #e9ecef;
    margin-top: 10px;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)


# ------------------------------------------
# 사이드바
# ------------------------------------------

with st.sidebar:

    st.title("Anonymous Expression Analysis")

    page = st.radio(
        "페이지",
        [
            "Overview",
            "Methodology",
            "Results",
            "Conclusion"
        ]
    )

    st.divider()

    st.caption("Text Data Analysis Portfolio")

    st.markdown("""
    **Tools**

    Python  
    Selenium  
    Pandas  
    Web Crawling  
    Rule-based Filtering
    """)


# ------------------------------------------
# Overview
# ------------------------------------------

if page == "Overview":

    st.title("10대 종합일간지 익명표현 사용 실태 분석")

    st.markdown(
        """
        ### 언론사에 따라 익명표현 사용 방식에는 차이가 있을까?

        2026년 6월 **10대 종합일간지의 지면기사 전체를 수집**하여  
        기사 속 익명표현을 분류하고 언론사별 사용 양상을 비교한 프로젝트입니다.
        """
    )

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("수집 기사", "18,289건")

    with c2:
        st.metric("분석 언론사", "10곳")

    with c3:
        st.metric("익명표현 기사", "7,951건")

    with c4:
        st.metric("익명표현 사용률", "43.5%")

    st.header("프로젝트 배경")

    left, right = st.columns(2)

    with left:

        st.subheader("Why")

        st.write(
            """
            기사에서는 취재원을 보호하거나 정보를 전달하기 위해
            다양한 익명표현이 사용됩니다.

            하지만 이러한 표현이 실제 기사에서 얼마나 자주 사용되는지,
            그리고 언론사마다 사용 방식에 차이가 있는지를
            정량적으로 비교하기는 쉽지 않습니다.

            이를 확인하기 위해 10대 종합일간지의
            한 달치 지면기사를 전수 수집해 분석했습니다.
            """
        )

    with right:

        st.subheader("Research Question")

        st.markdown(
            """
            - 전체 기사 중 익명표현은 얼마나 자주 사용되는가?
            - 언론사별 익명표현 사용 비율에는 차이가 있는가?
            - 익명표현은 어떤 유형으로 구분할 수 있는가?
            - 대규모 기사 데이터에서 익명표현을 어떻게 정량화할 수 있는가?
            """
        )

    st.header("프로젝트 흐름")

    pipeline = pd.DataFrame(
        {
            "단계": [
                "01 데이터 수집",
                "02 사전 구축",
                "03 데이터 필터링",
                "04 이상치 제거",
                "05 비교 분석"
            ],
            "내용": [
                "10대 종합일간지 지면기사 크롤링",
                "기사 전수조사를 통한 익명표현 통합 사전 구축",
                "통합 사전 기반 익명표현 탐지",
                "규칙 기반 오탐 및 이상치 제거",
                "언론사별 익명표현 사용 비율 비교"
            ]
        }
    )

    st.dataframe(
        pipeline,
        hide_index=True,
        use_container_width=True
    )

    st.markdown(
        """
        <div class="insight-box">
        <b>프로젝트 특징</b><br><br>
        단순히 주어진 사전을 사용한 것이 아니라,
        실제 기사 전수조사를 통해 분석 목적에 맞는
        익명표현 분류 기준과 통합 사전을 직접 구축했습니다.
        </div>
        """,
        unsafe_allow_html=True
    )


# ------------------------------------------
# Methodology
# ------------------------------------------

elif page == "Methodology":

    st.title("분석 방법")

    st.header("1. 기사 데이터 수집")

    st.write(
        """
        Selenium 기반 웹 크롤링을 이용해
        10대 종합일간지의 **2026년 6월 지면기사 18,289건**을 수집했습니다.
        """
    )

    st.success(
        "10개 언론사 → 2026년 6월 지면기사 → 18,289건"
    )

    st.header("2. 익명표현 통합 사전 구축")

    st.write(
        """
        일부 기사만 표본으로 확인하는 대신 실제 기사들을 직접 조사하여
        익명표현을 유형화하고 분석에 사용할 통합 사전을 구축했습니다.
        """
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.subheader("완전 익명")
        st.write(
            """
            신원 정보를 직접적으로
            확인하기 어려운 형태의 표현
            """
        )

    with c2:
        st.subheader("부분 익명")
        st.write(
            """
            일부 신원 정보만 제공되는
            형태의 표현
            """
        )

    with c3:
        st.subheader("보조 유형")
        st.write(
            """
            분석 과정에서 함께 고려해야 하는
            보조적인 익명 표현 유형
            """
        )

    st.header("3. 데이터 전처리")

    st.markdown(
        """
        통합 사전을 이용해 기사에서 후보 표현을 탐지한 뒤,

        1. 익명표현 후보 추출  
        2. 데이터 필터링  
        3. 규칙 기반 오탐 제거  
        4. 이상치 검토  
        5. 기사별 익명표현 사용 여부 판정  

        과정을 거쳐 최종 분석 데이터를 구성했습니다.
        """
    )

    st.markdown(
        """
        <div class="insight-box">
        <b>핵심 역량</b><br><br>
        대규모 텍스트 데이터를 단순 검색하는 것에서 그치지 않고,
        직접 정의한 분석 기준을 실제 데이터에 적용하고
        오탐을 제거하는 전처리 과정을 수행했습니다.
        </div>
        """,
        unsafe_allow_html=True
    )


# ------------------------------------------
# Results
# ------------------------------------------

elif page == "Results":

    st.title("분석 결과")

    st.subheader("전체 기사 중 익명표현 사용 비율")

    usage_df = pd.DataFrame(
        {
            "구분": [
                "익명표현 사용",
                "익명표현 미사용"
            ],
            "기사 수": [
                7951,
                18289 - 7951
            ]
        }
    )

    fig = px.pie(
        usage_df,
        names="구분",
        values="기사 수",
        hole=0.55
    )

    fig.update_traces(
        textinfo="percent+label"
    )

    fig.update_layout(
        height=450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "전체 기사",
            "18,289건"
        )

    with c2:
        st.metric(
            "익명표현 사용",
            "7,951건"
        )

    with c3:
        st.metric(
            "사용 비율",
            "43.5%"
        )

    st.markdown(
        """
        <div class="insight-box">
        전체 기사 18,289건 가운데 <b>7,951건</b>에서
        익명표현이 확인되었습니다.<br><br>

        전체 기사의 약 <b>43.5%</b>에서
        한 가지 이상의 익명표현이 사용된 것으로 나타났습니다.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.header("언론사별 차이")

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "가장 낮은 사용 비율",
            "31.3%"
        )

    with c2:

        st.metric(
            "가장 높은 사용 비율",
            "53.6%"
        )

    st.write(
        """
        언론사별 익명표현 사용 비율은 **31.3%에서 53.6%**까지 나타나,
        동일한 기간의 지면기사를 대상으로 하더라도
        언론사에 따라 익명표현 사용 양상에 차이가 있음을 확인했습니다.
        """
    )

    st.info(
        "언론사별 개별 수치를 추가하면 이 영역에 10개 언론사의 비교 그래프를 넣을 수 있습니다."
    )


# ------------------------------------------
# Conclusion
# ------------------------------------------

elif page == "Conclusion":

    st.title("Conclusion")

    st.subheader("프로젝트에서 확인한 내용")

    st.markdown(
        """
        ### 01. 익명표현은 기사에서 빈번하게 사용된다

        전체 18,289건의 기사 가운데  
        **43.5%인 7,951건**에서 익명표현이 확인되었습니다.

        ---

        ### 02. 언론사마다 사용 양상이 다르다

        언론사별 익명표현 사용 비율은  
        **31.3% ~ 53.6%**의 범위를 보였습니다.

        따라서 익명표현의 사용 빈도는
        매체에 따라 동일하지 않은 것으로 나타났습니다.

        ---

        ### 03. 텍스트 분석에서는 분류 기준이 중요하다

        실제 기사 전수조사를 통해
        익명표현 사전을 직접 구축하고,
        규칙 기반 전처리를 적용했습니다.

        같은 텍스트 데이터라도
        어떤 기준으로 분류하는지에 따라
        최종 분석 결과가 달라질 수 있음을 경험했습니다.
        """
    )

    st.divider()

    st.subheader("My Role")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("01", "크롤링")

    with c2:
        st.metric("02", "데이터 전처리")

    with c3:
        st.metric("03", "시각화")

    st.subheader("What I Learned")

    st.write(
        """
        프로젝트를 통해 대규모 기사 데이터를 직접 수집하고,
        분석 기준을 정의한 뒤 이를 코드로 구현하여
        정량적인 결과로 연결하는 전 과정을 경험했습니다.

        또한 데이터 분석 결과를 현직 기자에게 발표하면서
        분석 결과를 단순한 수치가 아닌
        실제 현상과 연결해 설명하는 경험도 쌓았습니다.
        """
    )

    st.success(
        "Web Crawling → Dictionary Construction → Preprocessing → Analysis → Interpretation"
    )
