import os
from textwrap import dedent

import pandas as pd
import requests
import streamlit as st

# =========================================================
# MULTILINGUA AI | CAMPUS INTELLIGENCE CONSOLE
# =========================================================

st.set_page_config(
    page_title="MultiLingua AI | Campus Intelligence",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded",
)

API_URL = os.getenv("API_URL", "")

if not API_URL:
    try:
        API_URL = st.secrets["API_URL"]
    except Exception:
        API_URL = "http://127.0.0.1:8000"

API_URL = API_URL.rstrip("/")

# Palette: Midnight / Porcelain / Teal / Copper
NAVY = "#17263C"
NAVY_SOFT = "#223650"
TEAL = "#00E5D0"
TEAL_LIGHT = "#DDF2ED"
COPPER = "#B879F8"
PAPER = "#F5F3EE"
WHITE = "#FFFFFF"
INK = "#263548"
MUTED = "#788594"
BORDER = "#E3E6E8"


# Always dedent HTML before passing it to Streamlit.
# This prevents indented HTML from being rendered as a Markdown code block.
def render_html(markup):
    st.markdown(dedent(markup).strip(), unsafe_allow_html=True)


# =========================================================
# GLOBAL STYLING
# =========================================================

# ============================================================
# MIDNIGHT AURORA - GLOBAL THEME
# ============================================================

render_html("""

<style>
:root {
    --bg: #071522;
    --sidebar: #0D2038;
    --card: #0D2234;
    --border: #19465A;
    --teal: #00E5D0;
    --teal-dark: #00BFAF;
    --violet: #B879F8;
    --text: #F1F7FC;
    --muted: #A6B9CB;
}

html, body, [data-testid="stAppViewContainer"] {
    background: #071522 !important;
}

.stApp {
    min-height: 100vh;
    background-color: #071522 !important;
    background-image:
        url("data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%201600%201000%22%20preserveAspectRatio=%22none%22%3E%0A%3Cdefs%3E%0A%20%20%3ClinearGradient%20id=%22teal%22%20x1=%220%22%20y1=%220%22%20x2=%221%22%20y2=%220%22%3E%0A%20%20%20%20%3Cstop%20offset=%220%22%20stop-color=%22%2300E5D0%22%20stop-opacity=%220%22/%3E%0A%20%20%20%20%3Cstop%20offset=%22.25%22%20stop-color=%22%2300E5D0%22%20stop-opacity=%22.55%22/%3E%0A%20%20%20%20%3Cstop%20offset=%22.65%22%20stop-color=%22%2342F5DF%22%20stop-opacity=%22.72%22/%3E%0A%20%20%20%20%3Cstop%20offset=%221%22%20stop-color=%22%2300E5D0%22%20stop-opacity=%220%22/%3E%0A%20%20%3C/linearGradient%3E%0A%20%20%3ClinearGradient%20id=%22violet%22%20x1=%220%22%20y1=%220%22%20x2=%221%22%20y2=%220%22%3E%0A%20%20%20%20%3Cstop%20offset=%220%22%20stop-color=%22%238B5CF6%22%20stop-opacity=%220%22/%3E%0A%20%20%20%20%3Cstop%20offset=%22.4%22%20stop-color=%22%23A78BFA%22%20stop-opacity=%22.55%22/%3E%0A%20%20%20%20%3Cstop%20offset=%22.75%22%20stop-color=%22%23C4A5FF%22%20stop-opacity=%22.7%22/%3E%0A%20%20%20%20%3Cstop%20offset=%221%22%20stop-color=%22%238B5CF6%22%20stop-opacity=%220%22/%3E%0A%20%20%3C/linearGradient%3E%0A%20%20%3Cfilter%20id=%22glow%22%20x=%22-30%25%22%20y=%22-100%25%22%20width=%22160%25%22%20height=%22300%25%22%3E%0A%20%20%20%20%3CfeGaussianBlur%20stdDeviation=%229%22/%3E%0A%20%20%3C/filter%3E%0A%3C/defs%3E%0A%3C%21--%20Broad,%20soft%20aurora%20ribbons%20--%3E%0A%3Cpath%20d=%22M280%20185%20C520%2040%20720%20255%20960%20145%20S1330%2030%201660%20150%20L1660%20255%20C1320%20135%201190%20285%20950%20250%20S550%20150%20280%20285%20Z%22%0A%20%20%20%20%20%20fill=%22%2300DCCB%22%20opacity=%22.055%22/%3E%0A%3Cpath%20d=%22M250%20205%20C520%2060%20720%20275%20960%20165%20S1330%2050%201660%20170%22%0A%20%20%20%20%20%20fill=%22none%22%20stroke=%22%2300E5D0%22%20stroke-width=%2220%22%20opacity=%22.20%22%20filter=%22url(%23glow)%22/%3E%0A%3Cpath%20d=%22M250%20205%20C520%2060%20720%20275%20960%20165%20S1330%2050%201660%20170%22%0A%20%20%20%20%20%20fill=%22none%22%20stroke=%22url(%23teal)%22%20stroke-width=%223.5%22/%3E%0A%3Cpath%20d=%22M270%20235%20C530%20100%20735%20305%20970%20200%20S1350%2085%201660%20205%22%0A%20%20%20%20%20%20fill=%22none%22%20stroke=%22%2349F5E2%22%20stroke-width=%221.6%22%20opacity=%22.48%22/%3E%0A%3Cpath%20d=%22M-80%20840%20C240%20690%20470%20950%20760%20835%20S1250%20700%201700%20835%22%0A%20%20%20%20%20%20fill=%22none%22%20stroke=%22%23A78BFA%22%20stroke-width=%2222%22%20opacity=%22.15%22%20filter=%22url(%23glow)%22/%3E%0A%3Cpath%20d=%22M-80%20840%20C240%20690%20470%20950%20760%20835%20S1250%20700%201700%20835%22%0A%20%20%20%20%20%20fill=%22none%22%20stroke=%22url(%23violet)%22%20stroke-width=%223.5%22/%3E%0A%3Cpath%20d=%22M-80%20875%20C250%20725%20485%20980%20770%20870%20S1260%20735%201700%20870%22%0A%20%20%20%20%20%20fill=%22none%22%20stroke=%22%23C4A5FF%22%20stroke-width=%221.6%22%20opacity=%22.45%22/%3E%0A%3C%21--%20Fine%20accent%20wave%20through%20the%20lower%20middle%20--%3E%0A%3Cpath%20d=%22M-60%20570%20C240%20465%20410%20650%20700%20560%20S1200%20450%201660%20565%22%0A%20%20%20%20%20%20fill=%22none%22%20stroke=%22%2300BFAF%22%20stroke-width=%221.4%22%20opacity=%22.22%22/%3E%0A%3C/svg%3E"),
        radial-gradient(ellipse at 82% 8%, rgba(0,229,208,.13), transparent 36%),
        radial-gradient(ellipse at 15% 92%, rgba(139,92,246,.12), transparent 38%),
        radial-gradient(rgba(0,229,208,.10) 1px, transparent 1px);
    background-repeat: no-repeat, no-repeat, no-repeat, repeat;
    background-position: center center, center top, left bottom, 0 0;
    background-size: 100% 100%, auto, auto, 28px 28px;
    background-attachment: fixed;
}

[data-testid="stAppViewContainer"] {
    background: transparent !important;
}

[data-testid="stMain"],
[data-testid="stMainBlockContainer"] {
    background: transparent !important;
}

.block-container {
    max-width: 1500px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

[data-testid="stHeader"] {
    background: rgba(7,21,34,.72) !important;
}

h1, h2, h3, h4, h5 {
    color: #F1F7FC !important;
    font-weight: 750 !important;
    letter-spacing: -.45px;
}

p, label, [data-testid="stCaptionContainer"] {
    color: var(--muted);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #10243D 0%, #0B1B30 100%) !important;
    border-right: 1px solid #19465A;
}
[data-testid="stSidebar"] > div { background: transparent !important; }
[data-testid="stSidebar"] * { color: #EAF4FF; }
[data-testid="stSidebar"] hr { border-color: #29445E; }
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p { color: #B6C9DC; }
[data-testid="stSidebar"] [data-testid="stRadio"] label { color: #DCE9F5 !important; }
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover { color: var(--teal) !important; }

/* Metric cards */
[data-testid="stMetric"] {
    background: linear-gradient(145deg, rgba(16,42,64,.96), rgba(11,31,48,.96)) !important;
    border: 1px solid #1B5266;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,.22), inset 0 1px 0 rgba(255,255,255,.04);
    transition: transform .22s ease, border-color .22s ease, box-shadow .22s ease;
}
[data-testid="stMetric"]:hover {
    border-color: var(--teal);
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(0,229,208,.09);
}
[data-testid="stMetricLabel"] { color: #A9BED0 !important; }
[data-testid="stMetricValue"] { color: var(--teal) !important; font-weight: 800 !important; }

/* Inputs */
.stTextInput input, .stTextArea textarea {
    background: #102A40 !important;
    color: #F1F7FC !important;
    border: 1px solid #28516A !important;
    border-radius: 11px !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: var(--teal) !important;
    box-shadow: 0 0 0 1px var(--teal);
}
.stTextInput input::placeholder, .stTextArea textarea::placeholder { color: #8198AC !important; }

/* Select boxes */
.stSelectbox [data-baseweb="select"] > div {
    background: #102A40 !important;
    color: #F1F7FC !important;
    border-color: #28516A !important;
    border-radius: 10px !important;
}
[data-baseweb="popover"] { color: #17263C !important; }

/* Buttons */
.stButton > button, .stFormSubmitButton > button {
    background: linear-gradient(110deg, #00E5D0, #00BFAF) !important;
    color: #061522 !important;
    font-weight: 800 !important;
    border: none !important;
    border-radius: 10px !important;
    min-height: 44px;
    transition: all .2s ease;
}
.stButton > button:hover, .stFormSubmitButton > button:hover {
    background: #29F5DE !important;
    box-shadow: 0 0 20px rgba(0,229,208,.28);
    transform: translateY(-2px);
}

/* Tables and dataframe containers */
[data-testid="stDataFrame"], [data-testid="stTable"] {
    border: 1px solid #19465A;
    border-radius: 12px;
    overflow: hidden;
}
[data-testid="stExpander"] {
    background: rgba(13,34,52,.94);
    border: 1px solid #19465A;
    border-radius: 12px;
}

/* Progress, alerts, download buttons */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #00BFAF, #00E5D0);
}
[data-testid="stAlert"] { border-radius: 12px; }
.stDownloadButton > button {
    background: #142C48 !important;
    color: #EAF4FF !important;
    border: 1px solid #28516A !important;
    border-radius: 10px;
}
.stDownloadButton > button:hover { border-color: var(--teal) !important; }
hr { border-color: #19465A !important; }

/* Scrollbar */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: #071522; }
::-webkit-scrollbar-thumb { background: #28516A; border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: #00BFAF; }

/* Hide Streamlit chrome */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
</style>

""")


# =========================================================
# API HELPERS
# =========================================================

def api_get(endpoint):
    try:
        response = requests.get(f"{API_URL}{endpoint}", timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error:
        return {"_api_error": str(error)}


def api_post(endpoint, payload):
    try:
        response = requests.post(
            f"{API_URL}{endpoint}",
            json=payload,
            timeout=30,
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error:
        st.error(f"API request failed: {error}")
        return None


def extract_records(data):
    if isinstance(data, list):
        return data

    if isinstance(data, dict):
        for key in ("records", "history", "reviews", "data"):
            value = data.get(key)
            if isinstance(value, list):
                return value

    return []


def format_confidence(value):
    try:
        number = float(value)
        return f"{number * 100:.2f}%"
    except (TypeError, ValueError):
        return "N/A"


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    render_html("""
    <div style="padding: 18px 8px 22px; text-align:center;">
        <div style="font-size:38px; margin-bottom:8px;">🌐</div>
        <div style="font-size:21px; font-weight:800; letter-spacing:-0.6px;">
            MultiLingua AI
        </div>
        <div style="font-size:9px; letter-spacing:2px; color:#AFC2D2; margin-top:6px;">
            CAMPUS INTELLIGENCE
        </div>
    </div>
    """)

    st.divider()
    st.markdown("**WORKSPACE**")

    page = st.radio(
        "Navigate",
        ["Overview", "AI Classifier", "Prediction History", "Human Review Center"],
        label_visibility="collapsed",
    )

    st.divider()

    health = api_get("/health")
    if isinstance(health, dict) and health.get("model_loaded"):
        st.success("● AI engine online")
    elif isinstance(health, dict) and not health.get("_api_error"):
        st.warning("● API reachable")
    else:
        st.error("● Backend offline")

    render_html("""
    <div style="
        margin-top:18px;
        padding:14px;
        border:1px solid rgba(255,255,255,0.15);
        border-radius:12px;
        background:rgba(255,255,255,0.06);">
        <div style="font-size:10px; font-weight:800; letter-spacing:1.2px; color:#B8C9D8;">
            SUPPORTED LANGUAGES
        </div>
        <div style="font-size:13px; line-height:2.1; margin-top:8px; color:#F2F5F7;">
            🇬🇧 English<br>
            🇮🇳 Hindi<br>
            💬 Hinglish<br>
            🟠 Punjabi
        </div>
    </div>
    <div style="text-align:center; margin-top:28px; color:#AFC2D2; font-size:10px; line-height:1.7;">
        MULTILINGUA AI · V1.0<br>
        CLASSICAL MACHINE LEARNING
    </div>
    """)


# =========================================================
# LOAD DATA
# =========================================================

history_data = api_get("/history")
reviews_data = api_get("/reviews")

all_records = extract_records(history_data)
pending_records = extract_records(reviews_data)
df = pd.DataFrame(all_records)


# =========================================================
# GLOBAL PAGE HEADER
# =========================================================

render_html("""
<div style="
    padding: 5px 0 22px;
    border-bottom: 1px solid #19465A;
    margin-bottom: 24px;">
    <div style="
        color:#D58B58;
        font-size:10px;
        font-weight:800;
        letter-spacing:2.5px;">
        MULTILINGUAL INTELLIGENCE PLATFORM
    </div>
    <div style="
        color:#F1F7FC;
        font-size:34px;
        line-height:1.2;
        font-weight:850;
        letter-spacing:-1.2px;
        margin-top:7px;">
        MultiLingua AI
    </div>
    <div style="color:#A6B9CB; font-size:14px; margin-top:7px;">
        One platform. Four languages. Smarter campus support.
    </div>
</div>
""")


# =========================================================
# OVERVIEW
# =========================================================

if page == "Overview":
    st.markdown("### Platform overview")
    st.caption("A live snapshot of campus requests and routing activity.")

    total = len(all_records)
    auto_routed = sum(
        record.get("status") == "AUTO_ROUTED" for record in all_records
    )
    reviewed = sum(
        record.get("status") == "REVIEWED" for record in all_records
    )
    pending = len(pending_records)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total predictions", total)
    c2.metric("Auto routed", auto_routed)
    c3.metric("Pending reviews", pending)
    c4.metric("Human reviewed", reviewed)

    st.write("")
    left, right = st.columns([1.35, 1], gap="large")

    with left:
        st.markdown("#### Recent predictions")
        if not df.empty:
            preferred = [
                "id", "prediction_id", "language",
                "predicted_department", "confidence", "status"
            ]
            columns = [column for column in preferred if column in df.columns]
            st.dataframe(
                df[columns].head(7) if columns else df.head(7),
                use_container_width=True,
                hide_index=True,
            )
        else:
            st.info("No predictions have been recorded yet.")

    with right:
        st.markdown("#### Language distribution")
        if not df.empty and "language" in df.columns:
            counts = (
                df["language"].value_counts()
                .rename_axis("Language")
                .reset_index(name="Messages")
            )
            st.bar_chart(counts, x="Language", y="Messages", color=TEAL)
        else:
            st.info("Language statistics will appear here.")

    st.write("")
    st.markdown("#### Department distribution")

    if not df.empty and "predicted_department" in df.columns:
        department_counts = (
            df["predicted_department"].value_counts()
            .rename_axis("Department")
            .reset_index(name="Messages")
        )
        st.bar_chart(
            department_counts,
            x="Department",
            y="Messages",
            color=COPPER,
        )
    else:
        st.info("Department statistics will appear here.")


# =========================================================
# AI CLASSIFIER
# =========================================================

elif page == "AI Classifier":
    st.markdown("### Intelligent message classification")

    render_html("""
    <div style="
        background:linear-gradient(115deg,#17263C 0%,#263F58 72%,#2A9D8F 150%);
        padding:26px 28px;
        border-radius:17px;
        margin:8px 0 22px;
        border:1px solid rgba(255,255,255,0.08);">
        <div style="
            color:#A8DCD3;
            font-size:10px;
            font-weight:800;
            letter-spacing:2px;">
            AI-POWERED CAMPUS SUPPORT
        </div>
        <div style="
            color:#FFFFFF;
            font-size:26px;
            font-weight:800;
            margin-top:9px;">
            How can we help you today?
        </div>
        <div style="
            color:#D4DEE7;
            font-size:14px;
            margin-top:7px;">
            Submit a campus query in English, Hindi, Hinglish or Punjabi.
            The model will identify the relevant department.
        </div>
    </div>
    """)

    with st.form("prediction_form", clear_on_submit=False):
        language = st.selectbox(
            "SELECT LANGUAGE",
            ["English", "Hindi", "Hinglish", "Punjabi"],
        )
        message = st.text_area(
            "YOUR MESSAGE",
            placeholder="Example: Mera hostel ka Wi-Fi kaam nahi kar raha...",
            height=150,
        )
        submitted = st.form_submit_button(
            "✦  ANALYZE MESSAGE",
            use_container_width=True,
        )

    if submitted:
        if len(message.strip()) < 2:
            st.warning("Please enter a message containing at least two characters.")
        else:
            with st.spinner("Analyzing your message..."):
                result = api_post(
                    "/predict",
                    {"message": message.strip(), "language": language},
                )

            if isinstance(result, dict):
                st.session_state["last_result"] = result

    result = st.session_state.get("last_result")

    if isinstance(result, dict):
        st.divider()
        st.markdown("### Analysis results")

        department = result.get("predicted_department", "Not available")
        confidence = result.get("confidence", 0)
        prediction_id = result.get("prediction_id", "N/A")
        status = result.get("status", "UNKNOWN")

        r1, r2, r3 = st.columns(3)
        r1.metric("Predicted department", department)
        r2.metric("Model confidence", format_confidence(confidence))
        r3.metric("Prediction ID", prediction_id)

        try:
            confidence_value = min(max(float(confidence), 0.0), 1.0)
            st.caption("Confidence score")
            st.progress(confidence_value)
        except (TypeError, ValueError):
            st.caption("Confidence score unavailable.")

        if status == "AUTO_ROUTED":
            st.success("Your message has been automatically routed.")
        else:
            st.warning("Your message has been sent for human review.")

        st.caption(
            "The confidence score is a model estimate and does not guarantee correctness."
        )


# =========================================================
# PREDICTION HISTORY
# =========================================================

elif page == "Prediction History":
    st.markdown("### Prediction history")
    st.caption("Search and review requests processed by the MultiLingua AI engine.")

    if not df.empty:
        search = st.text_input(
            "Search messages or departments",
            placeholder="Type a keyword, language or department...",
        )

        filtered = df.copy()

        if search:
            mask = filtered.astype(str).apply(
                lambda column: column.str.contains(
                    search,
                    case=False,
                    na=False,
                    regex=False,
                )
            ).any(axis=1)
            filtered = filtered[mask]

        st.markdown(f"**{len(filtered)} records found**")
        st.dataframe(
            filtered,
            use_container_width=True,
            hide_index=True,
        )

        csv_data = filtered.to_csv(index=False).encode("utf-8")
        st.download_button(
            "↓  Download prediction report",
            data=csv_data,
            file_name="multilingua_prediction_history.csv",
            mime="text/csv",
        )
    else:
        st.info("No prediction history is available yet.")


# =========================================================
# HUMAN REVIEW CENTER
# =========================================================

elif page == "Human Review Center":
    st.markdown("### Human review center")
    st.caption("Review uncertain predictions and assign the correct department.")

    st.metric("Pending review requests", len(pending_records))

    departments = ["IT", "Accounts", "Examination", "Hostel", "General"]

    if pending_records:
        for record in pending_records:
            prediction_id = record.get("id", record.get("prediction_id"))
            if prediction_id is None:
                continue

            with st.container(border=True):
                st.markdown(f"#### Ticket #{prediction_id}")
                st.markdown(f"**Message:** {record.get('message', 'N/A')}")

                a, b, c = st.columns(3)
                a.caption("Language")
                a.write(record.get("language", "N/A"))

                b.caption("Predicted department")
                current_department = record.get("predicted_department", "N/A")
                b.write(current_department)

                c.caption("Confidence")
                c.write(format_confidence(record.get("confidence")))

                default_index = (
                    departments.index(current_department)
                    if current_department in departments else 0
                )

                corrected = st.selectbox(
                    "Assign correct department",
                    departments,
                    index=default_index,
                    key=f"department_{prediction_id}",
                )

                if st.button(
                    "✓  Submit review",
                    key=f"submit_{prediction_id}",
                ):
                    review_result = api_post(
                        "/review",
                        {
                            "prediction_id": prediction_id,
                            "corrected_department": corrected,
                        },
                    )

                    if review_result is not None:
                        st.success("Review submitted successfully.")
                        st.rerun()
    else:
        st.success("All clear! There are no pending review requests.")


# =========================================================
# FOOTER
# =========================================================

st.divider()
footer_left, footer_right = st.columns(2)

with footer_left:
    st.caption("© 2026 MultiLingua AI · Intelligent Campus Support")

with footer_right:
    st.caption("TF-IDF · Linear SVM · FastAPI · Human-in-the-loop")
