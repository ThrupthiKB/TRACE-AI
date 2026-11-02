import streamlit as st
import requests
import plotly.graph_objects as go

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Message Intelligence | TRACE",
    page_icon="💬",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000/analyze-message"


# =====================================================
# CUSTOM STYLING
# =====================================================

st.markdown("""
<style>

.stApp {
    background-color: #0B1020;
    color: #E8EDF7;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}

.page-header {
    background: linear-gradient(120deg, #16243A, #172C3B);
    padding: 30px;
    border-radius: 18px;
    border: 1px solid #263B50;
    margin-bottom: 28px;
}

.eyebrow {
    color: #36D6C5;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
}

.page-title {
    color: #F1F5FC;
    font-size: 34px;
    font-weight: 750;
    margin-top: 8px;
}

.page-subtitle {
    color: #A5B3C7;
    font-size: 15px;
    margin-top: 8px;
}

.result-card {
    padding: 24px;
    border-radius: 16px;
    margin-top: 20px;
    border: 1px solid #34445A;
    background-color: #121D30;
}

.result-label {
    font-size: 12px;
    letter-spacing: 2px;
    color: #A5B3C7;
    font-weight: 700;
}

.result-value {
    font-size: 30px;
    font-weight: 800;
    margin-top: 10px;
}

.metric-card {
    background-color: #121D30;
    border: 1px solid #263B50;
    border-radius: 14px;
    padding: 20px;
}

.metric-label {
    color: #94A3B8;
    font-size: 13px;
}

.metric-value {
    color: #F1F5FC;
    font-size: 25px;
    font-weight: 750;
    margin-top: 8px;
}

div.stButton > button {
    background-color: #36D6C5;
    color: #07151B;
    border: none;
    border-radius: 9px;
    padding: 10px 25px;
    font-weight: 750;
    width: 100%;
}

div.stButton > button:hover {
    background-color: #62E5D7;
    color: #07151B;
}

textarea {
    background-color: #121D30 !important;
    color: #F1F5FC !important;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# PAGE HEADER
# =====================================================

st.markdown("""
<div class="page-header">
    <div class="eyebrow">TRACE / INTELLIGENCE MODULE 02</div>
    <div class="page-title">Message Intelligence</div>
    <div class="page-subtitle">
        Analyse suspicious SMS messages and identify spam-like
        patterns using machine learning.
    </div>
</div>
""", unsafe_allow_html=True)


# =====================================================
# MESSAGE INPUT
# =====================================================

st.markdown("### Message Analysis")
st.write("Paste the message you want TRACE to investigate.")

message = st.text_area(
    "Message Input",
    placeholder="Paste or type a suspicious message here...",
    height=180,
    label_visibility="collapsed"
)

st.caption("The message will be analysed by the trained TRACE Message Intelligence model.")

analyse_button = st.button("🔍 Analyse Message", use_container_width=True)


# =====================================================
# ANALYSIS
# =====================================================

if analyse_button:

    if not message.strip():

        st.warning("Please enter a message before starting the analysis.")

    else:

        with st.spinner("TRACE is analysing the message..."):

            try:

                response = requests.post(
                    API_URL,
                    json={"message": message},
                    timeout=30
                )

                if response.status_code == 200:

                    data = response.json()

                    result = data["result"]
                    confidence = data["model_confidence"]
                    prediction = data["prediction"]

                    st.markdown("---")
                    st.markdown("## Analysis Results")

                    # Result classification
                    if result == "SUSPICIOUS":

                        result_color = "#FF7373"
                        st.error("⚠️ Suspicious message detected")

                    else:

                        result_color = "#36D6C5"
                        st.success("✓ No spam pattern detected")

                    st.markdown(f"""
                    <div class="result-card">
                        <div class="result-label">MESSAGE CLASSIFICATION</div>
                        <div class="result-value" style="color:{result_color};">
                            {result}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    # Metrics
                    metric1, metric2, metric3 = st.columns(3)

                    with metric1:
                        st.markdown(f"""
                        <div class="metric-card">
                            <div class="metric-label">MODEL CONFIDENCE</div>
                            <div class="metric-value">{confidence}%</div>
                        </div>
                        """, unsafe_allow_html=True)

                    with metric2:
                        st.markdown(f"""
                        <div class="metric-card">
                            <div class="metric-label">MODEL PREDICTION</div>
                            <div class="metric-value">{prediction.upper()}</div>
                        </div>
                        """, unsafe_allow_html=True)

                    with metric3:
                        st.markdown(f"""
                        <div class="metric-card">
                            <div class="metric-label">MESSAGE LENGTH</div>
                            <div class="metric-value">{len(message)} chars</div>
                        </div>
                        """, unsafe_allow_html=True)

                    # Confidence chart
                    st.markdown("### Model Confidence")

                    fig = go.Figure(
                        go.Indicator(
                            mode="gauge+number",
                            value=confidence,
                            number={"suffix": "%"},
                            title={"text": "Classification Confidence"},
                            gauge={
                                "axis": {"range": [0, 100]},
                                "bar": {"color": "#36D6C5"},
                                "bgcolor": "#121D30",
                                "borderwidth": 1,
                                "bordercolor": "#34445A",
                                "steps": [
                                    {
                                        "range": [0, 50],
                                        "color": "#263449"
                                    },
                                    {
                                        "range": [50, 100],
                                        "color": "#1C3542"
                                    }
                                ]
                            }
                        )
                    )

                    fig.update_layout(
                        paper_bgcolor="#0B1020",
                        font={"color": "#E8EDF7"},
                        height=300,
                        margin=dict(l=30, r=30, t=60, b=20)
                    )

                    st.plotly_chart(fig, use_container_width=True)

                    # Investigation summary
                    st.markdown("### Investigation Summary")

                    if result == "SUSPICIOUS":

                        st.write(
                            "The machine learning model identified this "
                            "message as spam based on patterns learned "
                            "from its training dataset."
                        )

                        st.warning(
                            "Avoid clicking links or sharing personal "
                            "information until the message has been "
                            "independently verified."
                        )

                    else:

                        st.write(
                            "The machine learning model classified this "
                            "message as legitimate based on patterns "
                            "learned from its training dataset."
                        )

                        st.info(
                            "A legitimate classification does not guarantee "
                            "that a message is safe. Verify unexpected "
                            "requests independently."
                        )

                    st.caption(
                        "Note: This model detects SMS spam-like patterns. "
                        "Its confidence score is not a guarantee of safety "
                        "or a verified probability of phishing."
                    )

                else:

                    st.error(
                        f"API Error ({response.status_code}): "
                        f"{response.text}"
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "Could not connect to TRACE API. "
                    "Make sure the FastAPI server is running."
                )

            except requests.exceptions.RequestException as error:

                st.error(f"Request failed: {error}")