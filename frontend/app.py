import streamlit as st
import plotly.graph_objects as go
import requests

# =====================================================

# TRACE — CYBER INTELLIGENCE CENTRE

# =====================================================

st.set_page_config(
page_title="TRACE | Cyber Intelligence Centre",
page_icon="◈",
layout="wide",
initial_sidebar_state="expanded"
)

API_URL = "http://127.0.0.1:8000"

# =====================================================

# CUSTOM DESIGN

# =====================================================

st.markdown("""

<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');

.stApp {
    background: #0B1020;
    color: #EDF2FA;
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1500px;
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

p {
    color: #A8B8CC;
}

[data-testid="stSidebar"] {
    background: #10192B;
    border-right: 1px solid #263650;
}

[data-testid="stSidebar"] h1 {
    color: #36D6C5 !important;
    letter-spacing: 2px;
}

[data-testid="stSidebar"] p {
    color: #8295AD;
}

.trace-topbar {
    background: #121D30;
    border: 1px solid #263650;
    border-radius: 14px;
    padding: 15px 22px;
    margin-bottom: 28px;
}

.trace-brand {
    color: #36D6C5;
    font-size: 17px;
    font-weight: 800;
    letter-spacing: 3px;
}

.trace-hero {
    background: linear-gradient(115deg, #17253B, #142E3A);
    border: 1px solid #29495A;
    border-radius: 20px;
    padding: 35px;
    margin-bottom: 28px;
}

.trace-eyebrow {
    color: #36D6C5;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 3px;
}

.trace-title {
    color: #F4F7FC;
    font-size: 36px;
    font-weight: 800;
    margin-top: 12px;
}

.trace-description {
    color: #A8B8CC;
    font-size: 14px;
    line-height: 1.8;
    max-width: 750px;
    margin-top: 10px;
}

.section-label {
    color: #36D6C5;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 12px;
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
}

.panel-description {
    color: #8295AD;
    font-size: 12px;
    margin-top: 5px;
}

.module-card {
    background: linear-gradient(145deg, #17253A, #121D30);
    border: 1px solid #2A405B;
    border-radius: 16px;
    padding: 22px;
    min-height: 185px;
    margin-bottom: 12px;
    transition: 0.2s ease;
}

.module-card:hover {
    border-color: #36D6C5;
    transform: translateY(-3px);
}

.module-number {
    color: #36D6C5;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
}

.module-title {
    color: #EDF2FA;
    font-size: 18px;
    font-weight: 700;
    margin-top: 14px;
}

.module-description {
    color: #9AABC0;
    font-size: 12px;
    line-height: 1.7;
    margin-top: 8px;
}

div[data-testid="stMetric"] {
    background: #17253A;
    border: 1px solid #2B405B;
    padding: 19px;
    border-radius: 14px;
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
    border-radius: 9px;
    font-weight: 800;
    min-height: 42px;
}

div.stButton > button:hover {
    background: #65E1D0;
    color: #081923;
}

.trace-empty {
    background: #17253A;
    border: 1px dashed #38516C;
    border-radius: 14px;
    padding: 28px;
    text-align: center;
    color: #8295AD;
    margin-top: 10px;
}

.trace-footer {
    text-align: center;
    color: #71839B;
    font-size: 11px;
    letter-spacing: 2px;
    padding-top: 30px;
}

hr {
    border-color: #263650;
}

</style>

""", unsafe_allow_html=True)

# =====================================================

# SIDEBAR

# =====================================================

st.sidebar.markdown("# ◈ TRACE")
st.sidebar.caption("CYBER INTELLIGENCE CENTRE")

st.sidebar.divider()

st.sidebar.markdown("### NAVIGATION")

st.sidebar.page_link(
"app.py",
label="Dashboard",
icon="🏠"
)

st.sidebar.page_link(
"pages/1_URL_Intelligence.py",
label="URL Intelligence",
icon="🌐"
)

st.sidebar.page_link(
"pages/2_Message_Intelligence.py",
label="Message Intelligence",
icon="💬"
)

st.sidebar.page_link(
"pages/3_File_Intelligence.py",
label="File Intelligence",
icon="📁"
)

st.sidebar.page_link(
"pages/4_Threat_Analytics.py",
label="Threat Analytics",
icon="📊"
)

st.sidebar.page_link(
"pages/5_Scan_History.py",
label="Scan History",
icon="🕘"
)

st.sidebar.page_link(
"pages/6_Reports.py",
label="Reports",
icon="📄"
)

st.sidebar.divider()

st.sidebar.caption("AI-POWERED DIGITAL SECURITY")

# =====================================================

# =====================================================
# API CONNECTION STATUS
# =====================================================

try:
    api_response = requests.get(API_URL, timeout=2)
    api_online = api_response.status_code == 200

except requests.exceptions.RequestException:
    api_online = False

# =====================================================

# TOP BAR

# =====================================================

status_text = "● SYSTEM ONLINE" if api_online else "● API OFFLINE"
status_color = "#6EE7B7" if api_online else "#FFBE69"

st.markdown(f"""

<div class="trace-topbar">
    <div style="display:flex;justify-content:space-between;align-items:center;">
        <div class="trace-brand">◈ TRACE</div>
        <div style="color:{status_color};font-size:11px;font-weight:800;letter-spacing:1px;">
            {status_text}
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================================

# HERO SECTION

# =====================================================

st.markdown("""

<div class="trace-hero">
    <div class="trace-eyebrow">SECURITY OPERATIONS / OVERVIEW</div>
    <div class="trace-title">Cyber Intelligence Centre</div>
    <div class="trace-description">
        Your central workspace for investigating suspicious digital
        activity, identifying potential threats, and monitoring
        security intelligence across multiple analysis modules.
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================================

# SECURITY OVERVIEW

# =====================================================

st.markdown(
'<div class="section-label">01 / SECURITY OVERVIEW</div>',
unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("TOTAL INVESTIGATIONS", "0")
col2.metric("THREATS DETECTED", "0")
col3.metric("LEGITIMATE RESULTS", "0")
col4.metric("DETECTION RATE", "—")

st.caption(
"Investigation statistics will populate when scan history "
"is connected to the dashboard."
)

st.markdown("---")

# =====================================================

# =====================================================
# INTELLIGENCE MODULES
# =====================================================

st.markdown(
    '<div class="section-label">02 / INTELLIGENCE MODULES</div>',
    unsafe_allow_html=True
)

st.markdown("## Investigation Workspace")
st.markdown("Select an intelligence module to begin an investigation.")

module1, module2, module3 = st.columns(3)

with module1:
    st.markdown("""
    <div class="module-card">
        <div class="module-number">MODULE 01</div>
        <div class="module-title">🌐 URL Intelligence</div>
        <div class="module-description">
            Examine suspicious web addresses and identify
            potential phishing characteristics using machine learning.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.page_link(
        "pages/1_URL_Intelligence.py",
        label="Open URL Scanner →",
        use_container_width=True
    )

with module2:
    st.markdown("""
    <div class="module-card">
        <div class="module-number">MODULE 02</div>
        <div class="module-title">💬 Message Intelligence</div>
        <div class="module-description">
            Analyse suspicious messages and identify phishing
            language, deceptive patterns, and suspicious phrases.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.page_link(
        "pages/2_Message_Intelligence.py",
        label="Analyse Messages →",
        use_container_width=True
    )

with module3:
    st.markdown("""
    <div class="module-card">
        <div class="module-number">MODULE 03</div>
        <div class="module-title">📁 File Intelligence</div>
        <div class="module-description">
            Inspect uploaded files through metadata extraction,
            file hashing, and static security analysis.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.page_link(
        "pages/3_File_Intelligence.py",
        label="Inspect Files →",
        use_container_width=True
    )
# THREAT ANALYTICS

# =====================================================

st.markdown("---")

st.markdown(
'<div class="section-label">03 / THREAT MONITORING</div>',
unsafe_allow_html=True
)

left, right = st.columns([1.2, 1])

with left:


 st.markdown("""
<div class="panel">
    <div class="panel-title">Threat Distribution</div>
    <div class="panel-description">
        Classification breakdown from completed investigations.
    </div>
</div>
""", unsafe_allow_html=True)

empty_chart = go.Figure()

empty_chart.add_annotation(
    text="No investigation data available yet",
    x=0.5,
    y=0.5,
    showarrow=False,
    font=dict(
        color="#8295AD",
        size=14
    )
)

empty_chart.update_layout(
    height=280,
    paper_bgcolor="#121D30",
    plot_bgcolor="#121D30",
    font_color="#EDF2FA",
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    margin=dict(l=10, r=10, t=10, b=10)
)

st.plotly_chart(
    empty_chart,
    use_container_width=True
)


with right:

 st.markdown("""
<div class="panel">
    <div class="panel-title">System Status</div>
    <div class="panel-description">
        Current platform connectivity.
    </div>
</div>
""", unsafe_allow_html=True)

if api_online:
    st.success("FastAPI Backend — Connected")
else:
    st.warning("FastAPI Backend — Not Connected")

st.info("URL ML Model — Loaded through the backend")

st.info("Dashboard Database — Scan history integration pending")


# =====================================================

# ADDITIONAL WORKSPACES

# =====================================================

st.markdown("---")

st.markdown(
'<div class="section-label">04 / INVESTIGATION MANAGEMENT</div>',
unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
 st.markdown("### ◈ Threat Analytics")
st.caption("Explore threat patterns and detection statistics.")
st.page_link(
"pages/4_Threat_Analytics.py",
label="Explore Analytics →"
)

with col2:
 st.markdown("### ◈ Scan History")
st.caption("Review previously completed investigations.")
st.page_link(
"pages/5_Scan_History.py",
label="View History →"
)

with col3:
 st.markdown("### ◈ Intelligence Reports")
st.caption("Generate and access investigation reports.")
st.page_link(
"pages/6_Reports.py",
label="Open Reports →"
)

# =====================================================

# FOOTER

# =====================================================

st.markdown("""

<div class="trace-footer">
    TRACE · AI-POWERED DIGITAL THREAT INTELLIGENCE PLATFORM<br><br>
    CYBER INTELLIGENCE CENTRE
</div>
""", unsafe_allow_html=True)
