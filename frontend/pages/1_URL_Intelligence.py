import streamlit as st
import requests
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="TRACE | URL Intelligence",
    page_icon="◈",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000/analyze-url"

# ---------------- DESIGN SYSTEM ----------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

.stApp {
    background: #0B1020;
    color: #EDF2FA;
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

#MainMenu, footer {
    visibility: hidden;
}

h1, h2, h3 {
    color: #EDF2FA !important;
    font-weight: 700 !important;
}

p, label, span {
    font-family: 'DM Sans', sans-serif;
}

.trace-topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #111A2D;
    border: 1px solid #263650;
    border-radius: 14px;
    padding: 14px 22px;
    margin-bottom: 28px;
}

.trace-brand {
    font-size: 17px;
    font-weight: 800;
    letter-spacing: 2px;
    color: #36D6C5;
}

.trace-status {
    color: #6EE7B7;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
}

.trace-hero {
    background: linear-gradient(115deg, #17253B, #142E3A);
    border: 1px solid #29495A;
    border-radius: 20px;
    padding: 34px;
    margin-bottom: 28px;
}

.trace-eyebrow {
    color: #36D6C5;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 3px;
}

.trace-heading {
    font-size: 36px;
    font-weight: 800;
    color: #F4F7FC;
    margin-top: 12px;
    line-height: 1.2;
}

.trace-description {
    color: #A8B8CC;
    font-size: 14px;
    margin-top: 12px;
    max-width: 700px;
    line-height: 1.8;
}

.section-label {
    color: #36D6C5;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

.panel {
    background: #121D30;
    border: 1px solid #263650;
    border-radius: 16px;
    padding: 22px;
    margin-bottom: 18px;
}

.panel-title {
    color: #EDF2FA;
    font-size: 17px;
    font-weight: 700;
    margin-bottom: 5px;
}

.panel-subtitle {
    color: #8295AD;
    font-size: 12px;
    margin-bottom: 18px;
}

div[data-testid="stMetric"] {
    background: #17253A;
    border: 1px solid #2B405B;
    padding: 18px;
    border-radius: 13px;
}

div[data-testid="stMetricLabel"] {
    color: #A8B8CC;
}

div[data-testid="stMetricValue"] {
    color: #36D6C5;
}

div.stButton > button {
    background: linear-gradient(110deg, #36D6C5, #65E1D0);
    color: #081923;
    border: none;
    border-radius: 10px;
    font-weight: 800;
    min-height: 46px;
    transition: 0.2s ease;
}

div.stButton > button:hover {
    background: #65E1D0;
    color: #081923;
    transform: translateY(-2px);
    box-shadow: 0 5px 20px #36D6C533;
}

div[data-baseweb="input"] {
    background: #0D1728;
    border: 1px solid #344963;
    border-radius: 10px;
}

input {
    color: #EDF2FA !important;
}

hr {
    border-color: #263650;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}

.trace-footer {
    text-align: center;
    color: #71839B;
    font-size: 11px;
    letter-spacing: 2px;
    padding: 25px 0 5px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- TOP BAR ----------------

st.markdown("""
<div class="trace-topbar">
    <div class="trace-brand">◈ TRACE</div>
    <div class="trace-status">● INTELLIGENCE SYSTEM ONLINE</div>
</div>
""", unsafe_allow_html=True)


# ---------------- HERO ----------------

st.markdown("""
<div class="trace-hero">
    <div class="trace-eyebrow">THREAT INTELLIGENCE / MODULE 01</div>
    <div class="trace-heading">URL Intelligence</div>
    <div class="trace-description">
        Examine suspicious web addresses, identify potential phishing
        characteristics, and understand the signals behind each
        machine-learning classification.
    </div>
</div>
""", unsafe_allow_html=True)


# ---------------- SCANNER ----------------

st.markdown('<div class="section-label">01 / TARGET INVESTIGATION</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="panel">
    <div class="panel-title">Website Security Scanner</div>
    <div class="panel-subtitle">
        Submit a URL for automated threat analysis.
    </div>
</div>
""", unsafe_allow_html=True)

url = st.text_input(
    "TARGET URL",
    placeholder="https://example.com",
    label_visibility="visible"
)

scan_button = st.button(
    "◈  INITIATE URL ANALYSIS",
    use_container_width=True
)


# ---------------- ANALYSIS ----------------

if scan_button:

    if not url.strip():
        st.warning("Please enter a URL before starting the analysis.")

    else:
        try:
            with st.spinner("TRACE is examining URL characteristics..."):

                response = requests.post(
                    API_URL,
                    json={"url": url.strip()},
                    timeout=30
                )

            if response.status_code == 200:

                result = response.json()
                features = result["features"]
                classification = result["result"]
                confidence = float(result["model_confidence"])

                st.markdown("---")

                st.markdown(
                    '<div class="section-label">02 / INVESTIGATION RESULTS</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    '<div class="panel-title">Threat Assessment</div>',
                    unsafe_allow_html=True
                )

                # RESULT BANNER

                if classification == "PHISHING":
                    st.error("⚠ POTENTIAL PHISHING ACTIVITY DETECTED")
                    status_color = "#FF647C"
                else:
                    st.success("✓ CLASSIFIED AS LEGITIMATE")
                    status_color = "#36D6C5"

                st.caption(f"Target examined: {result['url']}")

                # METRICS

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "CLASSIFICATION",
                        classification
                    )

                with col2:
                    st.metric(
                        "MODEL CONFIDENCE",
                        f"{confidence:.2f}%"
                    )

                with col3:
                    st.metric(
                        "FEATURES EXAMINED",
                        len(features)
                    )

                # GAUGE + SUMMARY

                st.markdown("---")

                left, right = st.columns([1, 1.3])

                with left:

                    st.markdown(
                        '<div class="panel-title">Classification Confidence</div>',
                        unsafe_allow_html=True
                    )

                    gauge = go.Figure(
                        go.Indicator(
                            mode="gauge+number",
                            value=confidence,
                            number={
                                "suffix": "%",
                                "font": {"color": "#EDF2FA", "size": 35}
                            },
                            gauge={
                                "axis": {
                                    "range": [0, 100],
                                    "tickcolor": "#8295AD"
                                },
                                "bar": {"color": status_color},
                                "bgcolor": "#17253A",
                                "borderwidth": 0,
                                "steps": [
                                    {"range": [0, 50], "color": "#24334A"},
                                    {"range": [50, 80], "color": "#304052"},
                                    {"range": [80, 100], "color": "#3B4C5E"}
                                ]
                            }
                        )
                    )

                    gauge.update_layout(
                        height=260,
                        paper_bgcolor="#121D30",
                        font_color="#EDF2FA",
                        margin=dict(t=25, b=10, l=25, r=25)
                    )

                    st.plotly_chart(
                        gauge,
                        use_container_width=True
                    )

                with right:

                    st.markdown(
                        '<div class="panel-title">Investigation Summary</div>',
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        f"""
                        <div class="panel">
                            <div class="section-label">TARGET</div>
                            <p style="color:#EDF2FA;word-break:break-all;">
                                {result['url']}
                            </p>
                            <div class="section-label">DETECTION STATUS</div>
                            <h3 style="color:{status_color};">
                                {classification}
                            </h3>
                            <p style="color:#A8B8CC;font-size:13px;">
                                The machine-learning model classified this
                                URL using its extracted characteristics.
                            </p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                # FEATURE ANALYSIS

                st.markdown("---")

                st.markdown(
                    '<div class="section-label">03 / TECHNICAL BREAKDOWN</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    '<div class="panel-title">URL Characteristics</div>',
                    unsafe_allow_html=True
                )

                feature_df = pd.DataFrame(
                    list(features.items()),
                    columns=["Characteristic", "Value"]
                )

                feature_df["Characteristic"] = (
                    feature_df["Characteristic"]
                    .str.replace("_", " ")
                    .str.title()
                )

                st.dataframe(
                    feature_df,
                    use_container_width=True,
                    hide_index=True
                )

                # FEATURE CHART

                numeric_features = {
                    name: value
                    for name, value in features.items()
                    if isinstance(value, (int, float))
                    and not isinstance(value, bool)
                    and value > 0
                }

                if numeric_features:

                    chart_df = pd.DataFrame(
                        list(numeric_features.items()),
                        columns=["Characteristic", "Value"]
                    )

                    chart_df["Characteristic"] = (
                        chart_df["Characteristic"]
                        .str.replace("_", " ")
                        .str.title()
                    )

                    chart = px.bar(
                        chart_df,
                        x="Value",
                        y="Characteristic",
                        orientation="h",
                        title="Extracted URL Feature Values"
                    )

                    chart.update_layout(
                        paper_bgcolor="#121D30",
                        plot_bgcolor="#121D30",
                        font_color="#EDF2FA",
                        title_font_color="#EDF2FA",
                        xaxis_title="Extracted value",
                        yaxis_title="",
                        height=480,
                        margin=dict(l=10, r=20, t=55, b=20)
                    )

                    chart.update_traces(
                        marker_color="#36D6C5",
                        marker_line_width=0
                    )

                    st.plotly_chart(
                        chart,
                        use_container_width=True
                    )

                st.info(
                    "Model confidence indicates the model's confidence "
                    "in its classification. It does not guarantee that "
                    "a website is safe or malicious."
                )

            else:
                st.error(f"API Error: {response.status_code}")
                st.write(response.text)

        except requests.exceptions.ConnectionError:
            st.error(
                "Cannot connect to TRACE API. "
                "Start the FastAPI server and try again."
            )

        except requests.exceptions.Timeout:
            st.error("The request timed out. Please try again.")

        except Exception as error:
            st.error(f"Unexpected error: {error}")


# ---------------- FOOTER ----------------

st.markdown("""
<div class="trace-footer">
    TRACE · DIGITAL THREAT INTELLIGENCE PLATFORM<br><br>
    INTELLIGENCE MODULE 01
</div>
""", unsafe_allow_html=True)