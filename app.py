# ============================================================
# Customer Churn Intelligence Platform
# Streamlit Application
# ============================================================

import streamlit as st
import requests


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Customer Churn Intelligence Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500;600&display=swap');

    /* -------------------------------------------------------
       Design tokens
       Ink        -- sidebar / dark surface
       Paper      -- app background
       Panel      -- card surface
       Signal     -- primary accent (the "read" on a customer)
       Low/Med/High -- semantic risk colors
    ------------------------------------------------------- */

    :root {
        --ink: #0B1220;
        --ink-line: #22304A;
        --paper: #EEF1F7;
        --panel: #FFFFFF;
        --line: #E2E7F0;
        --text: #0F172A;
        --text-muted: #5B6577;
        --signal: #0891B2;
        --signal-dark: #0E7490;
        --signal-soft: #E0F7FA;
        --low: #10B981;
        --low-bg: #ECFDF5;
        --med: #F59E0B;
        --med-bg: #FFFBEB;
        --high: #EF4444;
        --high-bg: #FEF2F2;
    }

    /* -------------------------------------------------------
       Global
    ------------------------------------------------------- */

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(ellipse 900px 500px at 100% 0%, rgba(8,145,178,0.06), transparent),
            var(--paper);
    }

    .main .block-container {
        padding-top: 2.25rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* -------------------------------------------------------
       Main headings
    ------------------------------------------------------- */

    h1, h2, h3, h4 {
        font-family: 'Space Grotesk', sans-serif !important;
        color: var(--text) !important;
        font-weight: 700 !important;
        letter-spacing: -0.01em;
    }

    h1 {
        font-size: 2.1rem !important;
    }

    h2 {
        margin-top: 0.5rem !important;
        padding-top: 0.75rem;
        border-top: 1px solid var(--line);
    }

    p, label, span {
        color: var(--text);
    }

    .eyebrow {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: var(--signal-dark);
        margin-bottom: 0.25rem;
    }

    .subtitle {
        color: var(--text-muted);
        font-size: 1.02rem;
        margin-top: -0.4rem;
        margin-bottom: 0.5rem;
    }

    /* -------------------------------------------------------
       Sidebar
    ------------------------------------------------------- */

    section[data-testid="stSidebar"] {
        background-color: var(--ink);
        border-right: 1px solid var(--ink-line);
    }

    section[data-testid="stSidebar"] * {
        color: #E7ECF7 !important;
    }

    section[data-testid="stSidebar"] h3 {
        font-family: 'Space Grotesk', sans-serif !important;
    }

    .sidebar-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.3rem;
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 0.25rem;
    }

    .sidebar-title .dot {
        width: 9px;
        height: 9px;
        border-radius: 50%;
        background: var(--signal);
        box-shadow: 0 0 10px 2px rgba(8,145,178,0.7);
        display: inline-block;
    }

    .sidebar-divider {
        border-top: 1px solid var(--ink-line);
        margin: 1.5rem 0;
    }

    .sidebar-small {
        color: #8C99B5 !important;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        letter-spacing: 0.06em;
        text-transform: uppercase;
    }

    /* -------------------------------------------------------
       Input labels
    ------------------------------------------------------- */

    div[data-testid="stWidgetLabel"] label {
        color: var(--text) !important;
        font-weight: 600 !important;
        font-size: 0.88rem !important;
    }

    /* -------------------------------------------------------
       Select boxes / number inputs
    ------------------------------------------------------- */

    div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        border: 1px solid var(--line) !important;
        border-radius: 8px !important;
    }

    div[data-baseweb="select"] * {
        color: var(--text) !important;
    }

    div[data-baseweb="select"] > div:focus-within {
        border-color: var(--signal) !important;
        box-shadow: 0 0 0 3px rgba(8,145,178,0.15) !important;
    }

    div[data-testid="stNumberInput"] input {
        background-color: #FFFFFF !important;
        color: var(--text) !important;
        border-radius: 8px !important;
        border: 1px solid var(--line) !important;
    }

    /* -------------------------------------------------------
       Button
    ------------------------------------------------------- */

    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, var(--signal) 0%, var(--signal-dark) 100%);
        color: white !important;
        border: none;
        border-radius: 10px;
        padding: 0.8rem 1rem;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.02rem;
        font-weight: 600;
        letter-spacing: 0.01em;
        box-shadow: 0 4px 14px rgba(8,145,178,0.28);
        transition: transform 0.12s ease, box-shadow 0.12s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, var(--signal-dark) 0%, var(--signal) 100%);
        color: white !important;
        transform: translateY(-1px);
        box-shadow: 0 6px 18px rgba(8,145,178,0.36);
    }

    .stButton > button:active {
        transform: translateY(0);
    }

    /* -------------------------------------------------------
       Result cards
    ------------------------------------------------------- */

    .result-card {
        background-color: var(--panel);
        border-radius: 12px;
        padding: 1.4rem 1.5rem;
        border: 1px solid var(--line);
        box-shadow: 0 1px 2px rgba(15,23,42,0.04);
        min-height: 150px;
        transition: box-shadow 0.15s ease, transform 0.15s ease;
    }

    .result-card:hover {
        box-shadow: 0 8px 20px rgba(15,23,42,0.07);
        transform: translateY(-2px);
    }

    .result-card-title {
        font-family: 'JetBrains Mono', monospace;
        color: var(--text-muted) !important;
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-bottom: 0.65rem;
    }

    .result-value {
        color: var(--text) !important;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.6rem;
        font-weight: 700;
    }

    .result-subtitle {
        color: var(--text-muted) !important;
        font-size: 0.88rem;
        margin-top: 0.35rem;
        line-height: 1.6;
    }

    /* -------------------------------------------------------
       Main probability card + signal gauge
    ------------------------------------------------------- */

    .probability-card {
        background-color: var(--panel);
        border-radius: 16px;
        padding: 1.9rem 2rem;
        border: 1px solid var(--line);
        box-shadow: 0 1px 3px rgba(15,23,42,0.05);
        margin-top: 1rem;
        margin-bottom: 1.5rem;
    }

    .probability-title {
        font-family: 'JetBrains Mono', monospace;
        color: var(--text-muted) !important;
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 0.1em;
        text-transform: uppercase;
    }

    .probability-value {
        color: var(--text) !important;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 3rem;
        font-weight: 700;
        margin-top: 0.15rem;
        line-height: 1.1;
    }

    /* Signature element: the signal gauge -- a zoned meter with a
       floating marker, so the reader sees not just the number but
       exactly where it falls relative to the Low/Medium/High cutoffs. */

    .signal-gauge {
        margin-top: 1.6rem;
        position: relative;
    }

    .signal-gauge .track {
        display: flex;
        width: 100%;
        height: 14px;
        border-radius: 999px;
        overflow: hidden;
        box-shadow: inset 0 1px 2px rgba(15,23,42,0.15);
    }

    .signal-gauge .zone-low   { width: 30%; background: linear-gradient(90deg, #A7F3D0, var(--low)); }
    .signal-gauge .zone-med   { width: 30%; background: linear-gradient(90deg, var(--low), var(--med)); }
    .signal-gauge .zone-high  { width: 40%; background: linear-gradient(90deg, var(--med), var(--high)); }

    .signal-gauge .marker {
        position: absolute;
        top: -9px;
        width: 4px;
        height: 32px;
        background: var(--ink);
        border-radius: 3px;
        transform: translateX(-50%);
        box-shadow: 0 0 0 3px rgba(15,23,42,0.08);
    }

    .signal-gauge .marker::after {
        content: attr(data-label);
        position: absolute;
        top: -28px;
        left: 50%;
        transform: translateX(-50%);
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        font-weight: 600;
        color: var(--ink);
        white-space: nowrap;
    }

    .signal-gauge .ticks {
        display: flex;
        justify-content: space-between;
        margin-top: 0.5rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.7rem;
        color: var(--text-muted);
    }

    /* -------------------------------------------------------
       Risk badge
    ------------------------------------------------------- */

    .risk-low, .risk-medium, .risk-high {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.65rem 1.1rem;
        border-radius: 999px;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        font-size: 0.95rem;
        margin-top: 1.1rem;
    }

    .risk-low {
        background-color: var(--low-bg);
        border: 1px solid #A7F3D0;
        color: #065f46 !important;
    }

    .risk-medium {
        background-color: var(--med-bg);
        border: 1px solid #FDE68A;
        color: #92400e !important;
    }

    .risk-high {
        background-color: var(--high-bg);
        border: 1px solid #FECACA;
        color: #991b1b !important;
    }

    /* Fix Customer Risk result card layout */
    .insight-card.risk-low,
    .insight-card.risk-medium,
    .insight-card.risk-high {
        display: block;
        align-items: initial;
        gap: normal;
        padding: 1.25rem 1.3rem 1.35rem;
        border-radius: 18px;
        margin-top: 0;
        font-family: inherit;
        font-size: inherit;
        font-weight: inherit;
        background-color: #FFFFFF;
        color: #0F172A !important;
        white-space: normal;
    }

    /* -------------------------------------------------------
       Recommendation
    ------------------------------------------------------- */

    .recommendation-card {
        background-color: var(--panel);
        border-radius: 12px;
        padding: 1.5rem 1.7rem;
        border: 1px solid var(--line);
        border-left: 4px solid var(--signal);
        margin-top: 1rem;
    }

    .recommendation-card h3 {
        color: var(--text) !important;
        font-size: 1.1rem !important;
        margin-top: 0 !important;
        padding-top: 0 !important;
        border-top: none !important;
    }

    .recommendation-card p {
        color: var(--text-muted) !important;
        line-height: 1.65;
        margin-bottom: 0;
    }

    /* -------------------------------------------------------
       Streamlit progress bar + metrics
    ------------------------------------------------------- */

    div[data-testid="stProgress"] > div > div {
        background: linear-gradient(90deg, var(--signal), var(--signal-dark)) !important;
    }

    div[data-testid="stMetric"] {
        background-color: var(--panel);
        border: 1px solid var(--line);
        border-radius: 10px;
        padding: 0.9rem 1rem;
    }

    div[data-testid="stMetricValue"] {
        font-family: 'JetBrains Mono', monospace !important;
        color: var(--text) !important;
    }

    /* -------------------------------------------------------
       Section separator
    ------------------------------------------------------- */

    .section-line {
        border-top: 1px solid var(--line);
        margin: 2.25rem 0;
    }



    /* Refined prediction, recommendation and profile components */
    .insight-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 1rem;
        margin: 0.5rem 0 1.2rem 0;
    }
    .insight-card {
        position: relative;
        overflow: hidden;
        background: #FFFFFF;
        border: 1px solid #E1E8F0;
        border-radius: 18px;
        padding: 1.25rem 1.3rem 1.35rem;
        box-shadow: 0 5px 18px rgba(15, 23, 42, 0.045);
        min-height: 164px;
    }
    .insight-card:before {
        content: "";
        position: absolute;
        inset: 0 auto 0 0;
        width: 4px;
        background: var(--signal);
    }
    .insight-card.probability:before { background: #0891B2; }
    .insight-card.prediction:before { background: #6366F1; }
    .insight-card.risk-low:before { background: #10B981; }
    .insight-card.risk-medium:before { background: #F59E0B; }
    .insight-card.risk-high:before { background: #EF4444; }
    .insight-topline {
        display: flex;
        align-items: center;
        gap: 0.55rem;
        color: #64748B;
        font-size: 0.76rem;
        font-weight: 700;
        letter-spacing: 0.07em;
        text-transform: uppercase;
        margin-bottom: 1rem;
    }
    .insight-icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 34px;
        height: 34px;
        border-radius: 10px;
        background: #F1F5F9;
        font-size: 1.05rem;
        letter-spacing: normal;
    }
    .insight-value {
        color: #0F172A;
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(1.25rem, 1.8vw, 1.75rem);
        line-height: 1.25;
        font-weight: 700;
        overflow-wrap: anywhere;
    }
    .insight-caption {
        color: #64748B;
        font-size: 0.86rem;
        line-height: 1.5;
        margin-top: 0.45rem;
    }
    .probability-panel {
        background: linear-gradient(125deg, #0F172A 0%, #172554 58%, #164E63 100%);
        color: #F8FAFC;
        border-radius: 20px;
        padding: 1.5rem 1.6rem;
        margin: 0.7rem 0 1.1rem;
        box-shadow: 0 12px 28px rgba(15, 23, 42, 0.13);
    }
    .probability-panel * { color: inherit; }
    .probability-panel-head {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 1rem;
        flex-wrap: wrap;
    }
    .probability-panel-label {
        color: #CBD5E1;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.09em;
    }
    .probability-panel-value {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2.35rem;
        line-height: 1.2;
        font-weight: 700;
        margin-top: 0.35rem;
    }
    .probability-panel-note {
        color: #CBD5E1;
        font-size: 0.88rem;
        margin-top: 0.3rem;
    }
    .probability-pill {
        display: inline-block;
        border: 1px solid rgba(255,255,255,0.2);
        background: rgba(255,255,255,0.09);
        color: #F8FAFC;
        padding: 0.45rem 0.7rem;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 700;
        white-space: nowrap;
    }
    .recommendation-panel {
        border: 1px solid #DCE7F2;
        border-radius: 18px;
        background: linear-gradient(135deg, #FFFFFF 0%, #F8FAFC 100%);
        padding: 1.4rem 1.5rem;
        box-shadow: 0 5px 18px rgba(15,23,42,0.04);
        margin: 0.45rem 0 1.2rem;
    }
    .recommendation-head {
        display: flex;
        gap: 0.8rem;
        align-items: flex-start;
        margin-bottom: 0.7rem;
    }
    .recommendation-icon {
        display: flex;
        flex: 0 0 42px;
        width: 42px;
        height: 42px;
        align-items: center;
        justify-content: center;
        background: #E0F2FE;
        border-radius: 12px;
        font-size: 1.25rem;
    }
    .recommendation-title {
        color: #0F172A;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.1rem;
        font-weight: 700;
        margin: 0.1rem 0 0.25rem;
    }
    .recommendation-subtitle { color: #64748B; font-size: 0.86rem; line-height: 1.5; }
    .recommendation-copy { color: #334155; line-height: 1.7; margin: 0.8rem 0 0; }
    .profile-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 1rem;
        margin-top: 0.4rem;
    }
    .profile-card {
        background: #FFFFFF;
        border: 1px solid #E1E8F0;
        border-radius: 18px;
        padding: 1.25rem;
        box-shadow: 0 5px 18px rgba(15,23,42,0.04);
    }
    .profile-card-head {
        display: flex;
        align-items: center;
        gap: 0.7rem;
        padding-bottom: 1rem;
        margin-bottom: 0.25rem;
        border-bottom: 1px solid #EDF2F7;
    }
    .profile-card-icon {
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #ECFEFF;
        border-radius: 12px;
        font-size: 1.15rem;
    }
    .profile-card-title {
        color: #0F172A;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1rem;
        font-weight: 700;
    }
    .profile-card-description { color: #64748B; font-size: 0.8rem; margin-top: 0.15rem; }
    .profile-row {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 1rem;
        padding: 0.72rem 0;
        border-bottom: 1px solid #F1F5F9;
    }
    .profile-row:last-child { border-bottom: none; padding-bottom: 0.1rem; }
    .profile-label { color: #64748B; font-size: 0.85rem; }
    .profile-value { color: #0F172A; font-size: 0.87rem; font-weight: 600; text-align: right; overflow-wrap: anywhere; }
    @media (max-width: 800px) {
        .insight-grid, .profile-grid { grid-template-columns: 1fr; }
        .insight-card { min-height: auto; }
        .probability-panel { padding: 1.2rem; }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FASTAPI CONFIGURATION
# ============================================================

API_URL = "https://customer-churn-api-v4kk.onrender.com/predict"


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title"><span class="dot"></span>Churn Intelligence</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-divider"></div>',
        unsafe_allow_html=True
    )

    st.markdown("### About the Platform")

    st.markdown(
        """
        This application uses a trained **Logistic Regression**
        machine learning model to estimate the probability
        that a customer will churn.
        """
    )

    st.markdown(
        '<div class="sidebar-divider"></div>',
        unsafe_allow_html=True
    )

    st.markdown("### Workflow")

    st.markdown(
        """
        **1.** Enter customer information

        **2.** Enter service information

        **3.** Preprocess the customer profile

        **4.** Generate churn probability

        **5.** Determine customer risk

        **6.** Provide retention recommendations
        """
    )

    st.markdown(
        '<div class="sidebar-divider"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-small">Machine Learning Model</div>',
        unsafe_allow_html=True
    )

    st.markdown("### Logistic Regression")

    st.markdown(
        '<div class="sidebar-small">Customer Churn Prediction</div>',
        unsafe_allow_html=True
    )


# ============================================================
# TITLE
# ============================================================

st.markdown('<div class="eyebrow">Retention Analytics</div>', unsafe_allow_html=True)
st.title("Customer Churn Intelligence Platform")

st.markdown(
    '<div class="subtitle">Predict customer churn probability and '
    'identify customers who may require retention strategies.</div>',
    unsafe_allow_html=True
)


# ============================================================
# CUSTOMER INFORMATION
# ============================================================

st.markdown("## 👤 Customer Information")


col1, col2, col3 = st.columns(3)


with col1:

    country = st.selectbox(
        "Country",
        ["United States"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

    latitude = st.number_input(
        "Latitude",
        value=34.0522,
        format="%.6f"
    )


with col2:

    state = st.selectbox(
        "State",
        ["California"]
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

    longitude = st.number_input(
        "Longitude",
        value=-118.2437,
        format="%.6f"
    )


with col3:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )

    tenure_months = st.number_input(
        "Tenure Months",
        min_value=0,
        max_value=100,
        value=12,
        step=1
    )


# ============================================================
# SERVICE INFORMATION
# ============================================================

st.markdown("## 📱 Service Information")


col1, col2, col3 = st.columns(3)


with col1:

    phone_service = st.selectbox(
        "Phone Service",
        ["No", "Yes"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["No", "Yes", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["No", "Yes", "No internet service"]
    )

    contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )


with col2:

    multiple_lines = st.selectbox(
        "Multiple Lines",
        [
            "No",
            "Yes",
            "No phone service"
        ]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["No", "Yes", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["No", "Yes", "No internet service"]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["No", "Yes"]
    )


with col3:

    internet_service = st.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )

    device_protection = st.selectbox(
        "Device Protection",
        ["No", "Yes", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["No", "Yes", "No internet service"]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Bank transfer (automatic)",
            "Credit card (automatic)",
            "Electronic check",
            "Mailed check"
        ]
    )


# ============================================================
# BILLING INFORMATION
# ============================================================

st.markdown("## 💳 Billing Information")


col1, col2 = st.columns(2)


with col1:

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.00,
        step=1.0,
        format="%.2f"
    )


with col2:

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=840.00,
        step=1.0,
        format="%.2f"
    )


# ============================================================
# SEPARATOR
# ============================================================

st.markdown(
    '<div class="section-line"></div>',
    unsafe_allow_html=True
)


# ============================================================
# ANALYSIS SECTION
# ============================================================

st.markdown("## 🔍 Customer Churn Analysis")


analyze = st.button(
    "🚀 Analyze Customer Churn",
    use_container_width=True
)


# ============================================================
# PREDICTION
# ============================================================

if analyze:

    # --------------------------------------------------------
    # Send customer information to FastAPI
    # --------------------------------------------------------

    customer_payload = {
        "Country": country,
        "State": state,
        "Latitude": latitude,
        "Longitude": longitude,
        "Gender": gender,
        "Senior_Citizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "Tenure_Months": int(tenure_months),
        "Phone_Service": phone_service,
        "Multiple_Lines": multiple_lines,
        "Internet_Service": internet_service,
        "Online_Security": online_security,
        "Online_Backup": online_backup,
        "Device_Protection": device_protection,
        "Tech_Support": tech_support,
        "Streaming_TV": streaming_tv,
        "Streaming_Movies": streaming_movies,
        "Contract": contract,
        "Paperless_Billing": paperless_billing,
        "Payment_Method": payment_method,
        "Monthly_Charges": monthly_charges,
        "Total_Charges": total_charges
    }

    try:
        response = requests.post(
            API_URL,
            json=customer_payload,
            timeout=30
        )
        response.raise_for_status()
        api_result = response.json()

        prediction = int(api_result["prediction"])
        probability = float(api_result["churn_probability"])
        churn_probability = probability * 100

    except requests.exceptions.HTTPError as e:
        st.error(f"API Error: {e.response.status_code}")

        try:
            error_details = e.response.json()
            st.json(error_details)
        except ValueError:
            st.error(e.response.text)

        st.stop()

    except requests.exceptions.Timeout:
        st.error("The FastAPI request timed out. Please try again.")
        st.stop()

    except requests.exceptions.HTTPError:
        st.error("FastAPI returned an error while processing this customer.")
        st.code(response.text)
        st.stop()

    except (KeyError, TypeError, ValueError) as e:
        st.error("FastAPI returned an unexpected response.")
        st.code(str(e))
        st.stop()


    # --------------------------------------------------------
    # Determine risk
    # --------------------------------------------------------

    if churn_probability < 30:

        risk = "Low Risk"
        risk_class = "risk-low"

    elif churn_probability < 60:

        risk = "Medium Risk"
        risk_class = "risk-medium"

    else:

        risk = "High Risk"
        risk_class = "risk-high"


    # --------------------------------------------------------
    # Prediction label
    # --------------------------------------------------------

    if prediction == 1:

        prediction_label = "Likely to Churn"

    else:

        prediction_label = "Likely to Stay"


    # ========================================================
    # RESULTS
    # ========================================================

    st.markdown("## 📊 Prediction Results")

    if risk_class == "risk-high":
        risk_icon = "🔴"
        risk_short = "High risk"
    elif risk_class == "risk-medium":
        risk_icon = "🟠"
        risk_short = "Moderate risk"
    else:
        risk_icon = "🟢"
        risk_short = "Low risk"

    prediction_icon = "↗️" if prediction == 1 else "✓"
    prediction_caption = (
        "The model identifies this customer as at risk of leaving."
        if prediction == 1
        else "The model does not currently flag this customer as likely to leave."
    )

    st.markdown(
        f'<div class="insight-grid">'
        f'<div class="insight-card probability">'
        f'<div class="insight-topline"><span class="insight-icon">📈</span> Churn probability</div>'
        f'<div class="insight-value">{churn_probability:.2f}%</div>'
        f'<div class="insight-caption">Estimated likelihood that this customer will churn.</div>'
        f'</div>'
        f'<div class="insight-card prediction">'
        f'<div class="insight-topline"><span class="insight-icon">{prediction_icon}</span> Model prediction</div>'
        f'<div class="insight-value">{prediction_label}</div>'
        f'<div class="insight-caption">{prediction_caption}</div>'
        f'</div>'
        f'<div class="insight-card {risk_class}">'
        f'<div class="insight-topline"><span class="insight-icon">{risk_icon}</span> Customer risk</div>'
        f'<div class="insight-value">{risk}</div>'
        f'<div class="insight-caption">Risk band based on the estimated probability.</div>'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="probability-panel">'
        f'<div class="probability-panel-head">'
        f'<div><div class="probability-panel-label">Churn likelihood score</div>'
        f'<div class="probability-panel-value">{churn_probability:.2f}%</div>'
        f'<div class="probability-panel-note">A higher score indicates a greater estimated chance of churn.</div></div>'
        f'<div class="probability-pill">{risk_icon} {risk_short}</div>'
        f'</div></div>',
        unsafe_allow_html=True
    )

    marker_position = min(max(churn_probability, 0.0), 100.0)
    st.markdown(
        f'<div class="signal-gauge">'
        f'<div class="marker" data-label="{churn_probability:.1f}%" style="left: {marker_position}%;"></div>'
        f'<div class="track"><div class="zone-low"></div><div class="zone-med"></div><div class="zone-high"></div></div>'
        f'<div class="ticks"><span>0%</span><span>30% · low</span><span>60% · high</span><span>100%</span></div>'
        f'</div>',
        unsafe_allow_html=True
    )

    # ========================================================
    # RECOMMENDED ACTION
    # ========================================================

    st.markdown("## 💡 Recommended Actions")

    if risk == "High Risk":
        recommendation_title = "Prioritise retention outreach"
        recommendation_subtitle = "High churn probability — take a proactive approach."
        recommendation_icon = "🎯"
        recommendation_items = [
            "Contact the customer proactively to understand their concerns.",
            "Review service issues, especially internet reliability and technical support.",
            "Offer a relevant retention incentive or a suitable longer-term plan.",
        ]
    elif risk == "Medium Risk":
        recommendation_title = "Strengthen customer engagement"
        recommendation_subtitle = "Moderate churn probability — reduce friction before it grows."
        recommendation_icon = "🤝"
        recommendation_items = [
            "Send a personalised check-in and ask about service satisfaction.",
            "Review the customer's plan and usage for potential value improvements.",
            "Monitor support interactions and follow up on unresolved issues.",
        ]
    else:
        recommendation_title = "Maintain a positive customer experience"
        recommendation_subtitle = "Low churn probability — focus on loyalty and consistency."
        recommendation_icon = "🌱"
        recommendation_items = [
            "Continue providing reliable service and responsive support.",
            "Recognise loyalty with relevant benefits rather than unnecessary discounts.",
            "Reassess risk periodically as tenure, billing and service usage change.",
        ]

    recommendation_html = ''.join(
        f'<div class="profile-row"><span class="profile-label">Action {i}</span>'
        f'<span class="profile-value" style="max-width:78%;font-weight:500">{item}</span></div>'
        for i, item in enumerate(recommendation_items, start=1)
    )
    st.markdown(
        f'<div class="recommendation-panel">'
        f'<div class="recommendation-head"><div class="recommendation-icon">{recommendation_icon}</div>'
        f'<div><div class="recommendation-title">{recommendation_title}</div>'
        f'<div class="recommendation-subtitle">{recommendation_subtitle}</div></div></div>'
        f'<div class="recommendation-copy">Suggested next steps for this customer:</div>'
        f'{recommendation_html}</div>',
        unsafe_allow_html=True
    )

    # ========================================================
    # CUSTOMER PROFILE SUMMARY
    # ========================================================

    st.markdown("## 👤 Customer Profile Summary")
    st.markdown(
        '<div class="subtitle">A quick view of the customer attributes used for this assessment.</div>',
        unsafe_allow_html=True
    )

    customer_rows = [
        ("Country", country),
        ("State", state),
        ("Gender", gender),
        ("Senior citizen", senior_citizen),
        ("Partner", partner),
        ("Dependents", dependents),
        ("Latitude", f"{latitude:.4f}"),
        ("Longitude", f"{longitude:.4f}"),
    ]
    service_rows = [
        ("Tenure", f"{tenure_months} months"),
        ("Phone service", phone_service),
        ("Multiple lines", multiple_lines),
        ("Internet service", internet_service),
        ("Online security", online_security),
        ("Online backup", online_backup),
        ("Device protection", device_protection),
        ("Tech support", tech_support),
        ("Streaming TV", streaming_tv),
        ("Streaming movies", streaming_movies),
        ("Contract", contract),
        ("Paperless billing", paperless_billing),
        ("Payment method", payment_method),
        ("Monthly charges", f"${monthly_charges:,.2f}"),
        ("Total charges", f"${total_charges:,.2f}"),
    ]

    def profile_rows_html(rows):
        return ''.join(
            f'<div class="profile-row"><span class="profile-label">{label}</span>'
            f'<span class="profile-value">{value}</span></div>'
            for label, value in rows
        )

    profile_col1, profile_col2 = st.columns(2, gap="large")
    with profile_col1:
        st.markdown(
            f'<div class="profile-card"><div class="profile-card-head">'
            f'<div class="profile-card-icon">👤</div><div><div class="profile-card-title">Customer details</div>'
            f'<div class="profile-card-description">Identity and location</div></div></div>'
            f'{profile_rows_html(customer_rows)}</div>',
            unsafe_allow_html=True
        )
    with profile_col2:
        st.markdown(
            f'<div class="profile-card"><div class="profile-card-head">'
            f'<div class="profile-card-icon">📡</div><div><div class="profile-card-title">Services & billing</div>'
            f'<div class="profile-card-description">Subscriptions, contract and charges</div></div></div>'
            f'{profile_rows_html(service_rows)}</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # TECHNICAL INFORMATION
    # ========================================================

    st.markdown("## ⚙️ Model Information")


    technical_col1, technical_col2, technical_col3 = st.columns(3)


    with technical_col1:

        st.metric(
            "Model",
            "Logistic Regression"
        )


    with technical_col2:

        st.metric(
            "Input Features",
            len(customer_payload)
        )


    with technical_col3:

        st.metric(
            "Prediction Engine",
            "FastAPI"
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    '<div class="section-line"></div>',
    unsafe_allow_html=True
)

st.caption(
    "Customer Churn Intelligence Platform • Machine Learning Powered Customer Retention Analysis"
)