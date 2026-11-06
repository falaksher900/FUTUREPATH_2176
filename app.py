
import streamlit as st
import uuid
import html
import json
import re
from datetime import datetime

# ============================================================
# FUTUREPATH 2176
# CENTRAL CAREER ALLOCATION AUTHORITY
# STEPS 1–12 INTEGRATED
# Fictional speculative design project
# ============================================================

st.set_page_config(
    page_title="FUTUREPATH 2176",
    page_icon="🔷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# DESIGN SYSTEM
# ============================================================

st.html("""
<style>
.stApp {
    background: var(--fp-bg);
    color: var(--fp-text);
    font-family: Inter, Helvetica, Arial, sans-serif;
}
.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
section[data-testid="stSidebar"] {
    background: var(--fp-panel);
    border-right: 1px solid var(--fp-border);
}

h1, h2, h3 {
    color: var(--fp-text) !important;
}
h1 {
    font-weight: 800;
    letter-spacing: .06em;
}
hr {
    border-color: var(--fp-border);
    opacity: .5;
}
.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background: var(--fp-panel);
    color: var(--fp-text);
    border: 1px solid var(--fp-border);
}
[data-baseweb="select"] > div {
    background: var(--fp-panel);
    color: var(--fp-text);
    border-color: var(--fp-border);
}
.stButton button,
.stFormSubmitButton button,
.stDownloadButton button {
    background: var(--fp-accent);
    color: var(--fp-button_text);
    border: 1px solid var(--fp-accent);
    border-radius: 4px;
    font-weight: 700;
}
.stButton button:hover,
.stFormSubmitButton button:hover,
.stDownloadButton button:hover {
    background: var(--fp-accent);
    color: var(--fp-button_text);
}
.gov-panel {
    background: var(--fp-panel);
    border: 1px solid var(--fp-border);
    border-radius: 5px;
    padding: 22px;
    margin-bottom: 16px;
}
.gov-highlight {
    background: var(--fp-raised);
    border-left: 5px solid var(--fp-accent);
    padding: 22px;
    margin-bottom: 16px;
    border-radius: 4px;
}
.gov-label {
    color: var(--fp-muted);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: .12em;
    margin-bottom: 10px;
}
.gov-value {
    color: var(--fp-text);
    font-size: 25px;
    font-weight: 800;
    overflow-wrap: anywhere;
}
.gov-small {
    color: var(--fp-muted);
    font-size: 13px;
    line-height: 1.7;
    margin-top: 8px;
}
.gov-status {
    display: inline-block;
    color: var(--fp-accent);
    border: 1px solid var(--fp-accent);
    padding: 6px 10px;
    font-size: 12px;
    font-weight: 700;
}
.citizen-card {
    display: flex;
    align-items: center;
    gap: 24px;
    background: var(--fp-panel);
    border: 1px solid var(--fp-border);
    border-radius: 5px;
    padding: 24px;
    margin-bottom: 18px;
}
.citizen-avatar {
    width: 95px;
    height: 110px;
    background: var(--fp-border);
    border: 2px solid var(--fp-muted);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
.citizen-avatar svg {
    width: 65px;
    height: 75px;
    fill: var(--fp-muted);
}
.citizen-name {
    color: var(--fp-text);
    font-size: 29px;
    font-weight: 800;
    overflow-wrap: anywhere;
}
.citizen-id {
    color: var(--fp-accent);
    font-family: monospace;
    font-size: 14px;
    margin-bottom: 8px;
    overflow-wrap: anywhere;
}
.verified {
    display: inline-block;
    margin-top: 12px;
    padding: 6px 12px;
    border: 1px solid var(--fp-accent);
    color: var(--fp-accent);
    font-size: 12px;
    font-weight: 700;
}
.gauge-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 14px;
    margin-top: 18px;
}
.gauge-item {
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
}
.gauge-ring {
    width: 112px;
    height: 112px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}
.gauge-inner {
    width: 87px;
    height: 87px;
    border-radius: 50%;
    background: var(--fp-panel);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--fp-text);
    font-size: 25px;
    font-weight: 800;
}
.gauge-label {
    color: var(--fp-text);
    font-size: 13px;
    font-weight: 700;
}
.gauge-description {
    color: var(--fp-muted);
    font-size: 11px;
}
.appeal-denied {
    background: #251f31;
    border: 1px solid var(--fp-accent);
    border-left: 5px solid var(--fp-accent);
    padding: 24px;
    margin: 18px 0;
}
.propaganda-banner {
    background: linear-gradient(125deg, var(--fp-raised), var(--fp-panel));
    border: 1px solid var(--fp-border);
    border-left: 5px solid var(--fp-accent);
    padding: 30px;
    margin-bottom: 18px;
}
.propaganda-title {
    color: var(--fp-text);
    font-size: 27px;
    font-weight: 800;
    letter-spacing: .05em;
}
.policy-card {
    background: var(--fp-panel);
    border: 1px solid var(--fp-border);
    padding: 22px;
    margin-bottom: 14px;
}
.policy-code {
    color: var(--fp-accent);
    font-family: monospace;
    font-size: 12px;
    letter-spacing: .08em;
}
.classified {
    background: var(--fp-panel);
    border: 1px solid var(--fp-accent);
    border-left: 5px solid var(--fp-accent);
    padding: 25px;
    margin: 18px 0;
}
.resistance {
    background: var(--fp-bg);
    border: 1px dashed var(--fp-muted);
    padding: 25px;
    margin: 18px 0;
}
.resistance-title {
    color: var(--fp-text);
    font-size: 22px;
    font-weight: 800;
}
.assignment-day {
    background: linear-gradient(135deg, var(--fp-raised), var(--fp-panel));
    border: 1px solid var(--fp-accent);
    padding: 30px;
    margin: 18px 0;
}
.assignment-day-title {
    color: var(--fp-accent);
    font-size: 13px;
    font-weight: 800;
    letter-spacing: .16em;
}
.decision-accepted {
    background: var(--fp-raised);
    border-left: 5px solid var(--fp-success);
    padding: 24px;
    margin: 18px 0;
}
.decision-refused {
    background: var(--fp-raised);
    border-left: 5px solid var(--fp-warning);
    padding: 24px;
    margin: 18px 0;
}
.compliance-card {
    background: var(--fp-panel);
    border: 1px solid var(--fp-border);
    padding: 22px;
    margin: 16px 0;
}
.compliance-value {
    color: var(--fp-accent);
    font-size: 23px;
    font-weight: 800;
}
@media (max-width: 650px) {
    .citizen-card {
        flex-direction: column;
        align-items: flex-start;
    }
    .citizen-name {
        font-size: 22px;
    }
    .gauge-grid {
        grid-template-columns: 1fr;
        gap: 25px;
    }
}
/* STEP 12: keyboard focus and small-screen readability */
button:focus-visible, input:focus-visible, textarea:focus-visible,
[role="radio"]:focus-visible {
    outline: 3px solid var(--fp-accent) !important;
    outline-offset: 3px;
}
@media (max-width: 850px) {
    .block-container { padding-left: 1rem; padding-right: 1rem; }
    .propaganda-title { font-size: 22px; }
    .gov-value { font-size: 21px; }
}

/* COMPACT WIREFRAME DASHBOARD AND SIDEBAR */
.block-container { max-width: 1360px; padding-top: 1.1rem; padding-bottom: 1rem; }
section[data-testid="stSidebar"] { min-width: 260px; }
section[data-testid="stSidebar"] [data-testid="stRadio"] > label { display:none; }
section[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] { gap: 5px; }
section[data-testid="stSidebar"] [data-testid="stRadio"] label[data-baseweb="radio"] {
    padding: 11px 13px; border-radius: 7px; background: transparent;
    border: 1px solid transparent; margin: 1px 0; transition: background .15s;
}
section[data-testid="stSidebar"] [data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) {
    background: var(--fp-raised); border-left: 3px solid var(--fp-accent);
}
section[data-testid="stSidebar"] [data-testid="stRadio"] label[data-baseweb="radio"]:hover { background:var(--fp-raised); }
section[data-testid="stSidebar"] [data-testid="stRadio"] [data-testid="stMarkdownContainer"] p { font-size: 14px; font-weight: 600; }
section[data-testid="stSidebar"] .stButton button { font-size:12px; }
.fp-dashboard { display:grid; grid-template-columns: 1.05fr 1fr; gap:14px; margin: 12px 0; }
.fp-tile { background:var(--fp-panel); border:1px solid var(--fp-border); border-radius:8px; padding:19px; min-width:0; }
.fp-identity { display:flex; align-items:center; gap:17px; }
.fp-avatar { width:74px; height:82px; flex-shrink:0; background:var(--fp-border); border:1px solid var(--fp-muted); border-radius:5px; display:flex; align-items:center; justify-content:center; }
.fp-avatar svg { width:52px; height:60px; fill:var(--fp-muted); }
.fp-eyebrow { color:var(--fp-muted); font-size:10px; letter-spacing:.13em; font-weight:750; margin-bottom:7px; }
.fp-name { color:var(--fp-text); font-size:24px; font-weight:800; overflow-wrap:anywhere; }
.fp-sub { color:var(--fp-muted); font-size:12px; line-height:1.6; margin-top:7px; }
.fp-accent { color:var(--fp-accent); }
.fp-assignment { font-size:22px; color:var(--fp-text); font-weight:800; line-height:1.25; margin-top:12px; overflow-wrap:anywhere; }
.fp-gauges { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px; margin:12px 0; }
.fp-gauge { background:var(--fp-panel); border:1px solid var(--fp-border); border-radius:8px; padding:18px 8px 13px; display:flex; flex-direction:column; align-items:center; gap:10px; text-align:center; }
.fp-ring { width:102px; height:102px; border-radius:50%; display:flex; align-items:center; justify-content:center; }
.fp-ring-inner { width:78px; height:78px; border-radius:50%; background:var(--fp-panel); display:flex; align-items:center; justify-content:center; color:var(--fp-text); font-size:24px; font-weight:800; }
.fp-gauge-title { color:var(--fp-text); font-size:12px; font-weight:700; }
.fp-bottom { display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-top:12px; }
.fp-status { color:var(--fp-accent); font-size:19px; font-weight:800; margin:8px 0; }
.fp-banner { margin-top:12px; background:var(--fp-raised); border-left:4px solid var(--fp-accent); padding:12px 18px; color:var(--fp-text); font-size:12px; letter-spacing:.05em; }
@media(max-width:950px) { .fp-dashboard {grid-template-columns:1fr;} }
@media(max-width:600px) { .fp-gauges {gap:6px;} .fp-ring {width:79px;height:79px;} .fp-ring-inner {width:61px;height:61px;font-size:18px;} .fp-gauge {padding:12px 3px;} .fp-bottom {grid-template-columns:1fr;} .fp-name {font-size:19px;} }

/* STEP 12+ : PROFESSIONAL ICON SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,var(--fp-bg) 0%,var(--fp-bg) 100%) !important;
    border-right:1px solid var(--fp-border);
    min-width: 286px;
}
section[data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {
    padding: 20px 15px 16px;
}
.fp-side-brand { display:flex; gap:12px; align-items:center; padding:7px 3px 15px; }
.fp-side-emblem { width:45px; height:45px; flex-shrink:0; }
.fp-side-emblem svg { width:100%; height:100%; }
.fp-side-logo { color:var(--fp-text); font-size:21px; letter-spacing:.09em; font-weight:850; line-height:1.1; }
.fp-side-logo span { color:var(--fp-accent); }
.fp-side-tag { font-size:8px; letter-spacing:.09em; color:var(--fp-muted); line-height:1.5; margin-top:5px; font-weight:700; }
.fp-side-separator { height:1px; background:var(--fp-border); margin:5px 0 17px; }
.fp-side-section { display:flex; justify-content:space-between; align-items:center; color:var(--fp-muted); font-size:10px; letter-spacing:.13em; font-weight:800; margin:0 4px 12px; }
.fp-side-section span { color:var(--fp-muted); letter-spacing:.04em; }
/* Target ONLY the six icon-navigation buttons, not the demo controls. */
section[data-testid="stSidebar"] div[class*="st-key-fp_nav_"] { margin-bottom:5px; }
section[data-testid="stSidebar"] div[class*="st-key-fp_nav_"] button {
    display:flex; justify-content:flex-start; align-items:center; gap:13px;
    width:100%; min-height:46px; border-radius:7px;
    padding:10px 14px; font-size:12px; font-weight:750;
    letter-spacing:.075em; text-align:left; box-shadow:none;
    transition:background .15s ease,border-color .15s ease;
}
section[data-testid="stSidebar"] div[class*="st-key-fp_nav_"] button[kind="secondary"] {
    background:transparent !important; color:var(--fp-text) !important;
    border:1px solid transparent !important;
}
section[data-testid="stSidebar"] div[class*="st-key-fp_nav_"] button[kind="secondary"]:hover {
    background:var(--fp-raised) !important; border-color:var(--fp-border) !important;
}
section[data-testid="stSidebar"] div[class*="st-key-fp_nav_"] button[kind="primary"] {
    background:linear-gradient(90deg,var(--fp-raised),var(--fp-raised)) !important;
    color:var(--fp-text) !important; border:1px solid var(--fp-border) !important;
    border-left:3px solid var(--fp-accent) !important;
}
section[data-testid="stSidebar"] div[class*="st-key-fp_nav_"] button svg {
    width:19px !important; height:19px !important; flex-shrink:0;
    color:var(--fp-accent) !important; fill:currentColor;
}
.fp-side-citizen { display:flex; align-items:center; gap:11px; border:1px solid var(--fp-border); background:var(--fp-panel); border-radius:8px; padding:12px 10px; margin-bottom:14px; }
.fp-side-avatar { width:37px; height:39px; flex-shrink:0; border:1px solid var(--fp-border); border-radius:5px; background:var(--fp-raised); display:flex; align-items:center; justify-content:center; color:var(--fp-accent); font-size:22px; }
.fp-side-avatar svg { width:28px; height:28px; }
.fp-side-person { min-width:0; }
.fp-side-person-name { font-size:12px; font-weight:800; color:var(--fp-text); white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
.fp-side-person-id { color:var(--fp-muted); font-size:9px; font-family:monospace; overflow-wrap:anywhere; margin-top:4px; }
.fp-side-verified { color:var(--fp-accent); font-size:9px; font-weight:800; margin-top:5px; letter-spacing:.04em; }
.fp-side-unregistered .fp-side-person-name { font-size:10px; }
.fp-side-status { display:flex; align-items:center; gap:8px; color:var(--fp-text); font-size:10px; font-weight:750; letter-spacing:.07em; padding:11px 7px; border-top:1px solid var(--fp-border); border-bottom:1px solid var(--fp-border); margin-bottom:12px; }
.fp-online-dot { width:7px; height:7px; border-radius:50%; background:var(--fp-success); box-shadow:0 0 8px #9ed1bd66; }
.fp-side-status-year { margin-left:auto; color:var(--fp-muted); }
.fp-side-anomaly { color:var(--fp-accent); border:1px dashed var(--fp-border); padding:9px; font-size:10px; border-radius:4px; margin-top:12px; }
.fp-side-footer { border-top:1px solid var(--fp-border); margin-top:20px; padding:16px 5px 0; font-size:9px; letter-spacing:.055em; color:var(--fp-muted); line-height:1.8; }
.fp-side-footer-quote { color:var(--fp-accent); margin:6px 0; }
@media (max-width:850px) { section[data-testid="stSidebar"] { min-width:260px; } }
</style>
""")

# ============================================================
# SESSION STATE
# ============================================================

if "citizen" not in st.session_state:
    st.session_state.citizen = None

if "resistance_discovered" not in st.session_state:
    st.session_state.resistance_discovered = False

if "classified_access" not in st.session_state:
    st.session_state.classified_access = False

# STEP 11: narrative discoveries persist within the current browser session.
if "history_discovered" not in st.session_state:
    st.session_state.history_discovered = False
if "aurora_story_read" not in st.session_state:
    st.session_state.aurora_story_read = False
if "demo_mode" not in st.session_state:
    st.session_state.demo_mode = False

# ============================================================
# HELPERS
# ============================================================

def safe(value):
    return html.escape(str(value), quote=True)


def render(content):
    # Inline gauge, SVG, and narrative colors follow the same palette.
    # Downloaded documents retain their self-contained print stylesheet.
    content = re.sub(r"#[0-9a-fA-F]{6,8}\b", lambda match: INLINE_COLORS.get(match[0].lower(), match[0]), content)
    st.html(content)


def generate_id(prefix):
    return prefix + uuid.uuid4().hex[:8].upper()


def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


# GLOBAL VISUAL MODE — persistent across navigation and evaluations
if "visual_mode" not in st.session_state:
    st.session_state.visual_mode = "Dark"

THEME = {
    "Dark": {"bg": "#0e1b2b", "panel": "#17283a", "raised": "#24374a", "text": "#e8e9ec", "muted": "#a8b8c9", "border": "#435565", "accent": "#b095f2", "button_text": "#0e1b2b"},
    "Light": {"bg": "#f3f5fa", "panel": "#ffffff", "raised": "#e8edf6", "text": "#1c2b40", "muted": "#4b5d73", "border": "#c5cfdf", "accent": "#7153b5", "button_text": "#ffffff"},
}

INLINE_COLORS = {'#0e1b2b': 'var(--fp-bg)', '#142438': 'var(--fp-bg)', '#101e30': 'var(--fp-bg)', '#111d24': 'var(--fp-bg)', '#17283a': 'var(--fp-panel)', '#1b2e43': 'var(--fp-panel)', '#211b2d': 'var(--fp-panel)', '#24374a': 'var(--fp-raised)', '#20344b': 'var(--fp-raised)', '#31445e': 'var(--fp-raised)', '#26384e': 'var(--fp-raised)', '#34475e': 'var(--fp-raised)', '#192d36': 'var(--fp-raised)', '#301f31': 'var(--fp-raised)', '#e8e9ec': 'var(--fp-text)', '#f1f2f7': 'var(--fp-text)', '#f0e9ff': 'var(--fp-text)', '#c5cfdb': 'var(--fp-text)', '#c0d3e2': 'var(--fp-text)', '#b8c9d9': 'var(--fp-text)', '#b095f2': 'var(--fp-accent)', '#c4b0fa': 'var(--fp-accent)', '#c6b2fa': 'var(--fp-accent)', '#b1a2cf': 'var(--fp-accent)', '#d9b8ff': 'var(--fp-accent)', '#8c9fad': 'var(--fp-muted)', '#91a2b6': 'var(--fp-muted)', '#8798ad': 'var(--fp-muted)', '#64778c': 'var(--fp-muted)', '#9aacc0': 'var(--fp-muted)', '#7e92a9': 'var(--fp-muted)', '#73869a': 'var(--fp-muted)', '#b5c4d3': 'var(--fp-muted)', '#435565': 'var(--fp-border)', '#35465a': 'var(--fp-border)', '#33455a': 'var(--fp-border)', '#40536a': 'var(--fp-border)', '#4b5873': 'var(--fp-border)', '#3d4f65': 'var(--fp-border)', '#64758c': 'var(--fp-border)', '#7765a0': 'var(--fp-border)', '#34465a': 'var(--fp-border)', '#9ed1bd': 'var(--fp-success)', '#8fc4bb': 'var(--fp-success)', '#d9a0bf': 'var(--fp-warning)'}

def toggle_visual_mode():
    st.session_state.visual_mode = "Light" if st.session_state.visual_mode == "Dark" else "Dark"


def apply_visual_mode():
    t = dict(THEME[st.session_state.visual_mode])
    dark = st.session_state.visual_mode == "Dark"
    t.update(hover="#c4b0fa" if dark else "#593b96",
             success="#9ed1bd" if dark else "#24654f",
             warning="#d9a0bf" if dark else "#89365e")
    variables = ";".join(f"--fp-{key}:{value}" for key, value in t.items())
    st.html("<style>:root {" + variables + ";color-scheme:" + ("dark" if dark else "light") + ";}" + THEME_WIDGET_CSS + "</style>")


THEME_WIDGET_CSS = '\n/* Shared widget styling; button descendants inherit their state foreground. */\n.stApp,[data-testid="stAppViewContainer"],[data-testid="stHeader"] {background:var(--fp-bg);color:var(--fp-text);}\n.stApp p,.stApp label,.stApp li,.stApp h1,.stApp h2,.stApp h3,.stApp h4 {color:var(--fp-text);}\n.stApp a {color:var(--fp-accent);}\n[data-testid="stCaptionContainer"],input::placeholder,textarea::placeholder {color:var(--fp-muted)!important;opacity:1;}\n[data-testid="stForm"],[data-testid="stExpander"],details,details summary {background:var(--fp-panel)!important;color:var(--fp-text)!important;border-color:var(--fp-border)!important;}\n[data-baseweb="input"],[data-baseweb="base-input"],[data-baseweb="textarea"],[data-baseweb="select"]>div,input,textarea {background:var(--fp-panel)!important;color:var(--fp-text)!important;border-color:var(--fp-border)!important;caret-color:var(--fp-accent);}\n[data-baseweb="select"] span,[data-baseweb="select"] input {color:var(--fp-text)!important;}\n[data-baseweb="popover"],[data-baseweb="menu"],[role="listbox"],[role="option"],[role="tooltip"] {background:var(--fp-panel)!important;color:var(--fp-text)!important;}\n[role="option"]:hover,[role="option"][aria-selected="true"] {background:var(--fp-raised)!important;}\n.stButton button,.stFormSubmitButton button,.stDownloadButton button,.stLinkButton a {background:var(--fp-accent)!important;color:var(--fp-button_text)!important;border:1px solid var(--fp-accent)!important;transition:background .15s,border-color .15s;}\n.stButton button[kind="secondary"],.stFormSubmitButton button[kind="secondary"] {background:var(--fp-raised)!important;color:var(--fp-text)!important;border-color:var(--fp-border)!important;}\n.stApp button p,.stApp button span,.stApp button svg,.stApp button [data-testid="stMarkdownContainer"],.stLinkButton a p {color:inherit!important;}\n.stButton button:enabled:hover,.stFormSubmitButton button:enabled:hover,.stDownloadButton button:enabled:hover {background:var(--fp-hover)!important;color:var(--fp-button_text)!important;border-color:var(--fp-hover)!important;}\n.stButton button[kind="secondary"]:enabled:hover,.stFormSubmitButton button[kind="secondary"]:enabled:hover {background:var(--fp-panel)!important;color:var(--fp-accent)!important;border-color:var(--fp-accent)!important;}\n.stApp .stButton button:disabled,.stApp .stFormSubmitButton button:disabled,.stApp .stDownloadButton button:disabled {background:var(--fp-raised)!important;color:var(--fp-muted)!important;border-color:var(--fp-border)!important;opacity:1;cursor:not-allowed;}\ninput:disabled,textarea:disabled {color:var(--fp-muted)!important;-webkit-text-fill-color:var(--fp-muted)!important;}\n.stApp button:focus-visible,.stApp input:focus-visible,.stApp textarea:focus-visible {outline:3px solid var(--fp-accent)!important;outline-offset:3px;}\n[data-testid="stTabs"] [role="tablist"] {border-color:var(--fp-border);}\n[data-testid="stTabs"] [role="tab"] {background:transparent;color:var(--fp-muted);}\n[data-testid="stTabs"] [role="tab"][aria-selected="true"] {color:var(--fp-accent);}\n[data-baseweb="tab-highlight"],[data-testid="stProgressBar"] [role="progressbar"]>div {background:var(--fp-accent)!important;}\n[data-testid="stAlert"] {background:var(--fp-raised)!important;color:var(--fp-text)!important;border:1px solid var(--fp-border);border-left:4px solid var(--fp-accent);}\n[data-testid="stAlert"] p,[data-testid="stAlert"] svg {color:inherit!important;}\n[data-testid="stCode"],pre,code {background:var(--fp-raised)!important;color:var(--fp-text)!important;}\ntable,th,td,[data-testid="stMetricValue"],[data-testid="stMetricLabel"] {color:var(--fp-text)!important;border-color:var(--fp-border)!important;}\n[data-testid="stCheckbox"] label,[data-testid="stRadio"] label {color:var(--fp-text)!important;}\n.st-key-fp_theme_toggle {display:flex;justify-content:flex-end;}\n.st-key-fp_theme_toggle button {width:42px!important;height:42px;min-height:42px;border-radius:50%!important;padding:8px!important;background:var(--fp-raised)!important;color:var(--fp-accent)!important;border-color:var(--fp-border)!important;}\n.fp-main-brand {display:flex;align-items:center;gap:18px;margin:8px 0 12px;}\n.fp-main-brand svg {width:66px;height:66px;flex-shrink:0;color:var(--fp-accent);}\n.fp-main-brand h1 {margin:0;padding:0;font-size:clamp(26px,4vw,44px);letter-spacing:.08em;line-height:1.15;}\n.fp-main-brand .fp-year {color:var(--fp-accent);font-size:11px;letter-spacing:.3em;margin-top:5px;}\n@media(prefers-reduced-motion:reduce) {* {transition:none!important;}}\n'

apply_visual_mode()

# ============================================================
# EVALUATION OPTIONS
# ============================================================

career_options = [
    "Architect", "Artist", "Business Analyst",
    "Civil Engineer", "Computer Scientist",
    "Cybersecurity Specialist", "Data Scientist",
    "Doctor", "Economist", "Entrepreneur",
    "Fashion Designer", "Financial Analyst",
    "Graphic Designer", "Journalist", "Lawyer",
    "Marketing Specialist", "Mechanical Engineer",
    "Nurse", "Psychologist", "Teacher"
]

skill_options = [
    "Technology and Computing",
    "Mathematics and Data",
    "Science and Research",
    "Healthcare and Helping Others",
    "Communication and Writing",
    "Business and Leadership",
    "Creative Design and Art",
    "Engineering and Problem Solving"
]

academic_subjects = [
    "Art and Design",
    "Computer Science",
    "Mathematics",
    "Biology and Healthcare",
    "Physics and Engineering",
    "Business and Economics",
    "English and Communication",
    "Social Sciences",
    "Other"
]

work_environments = [
    "Creative Studio",
    "Office Environment",
    "Research Laboratory",
    "Hospital or Healthcare Facility",
    "Engineering or Industrial Facility",
    "Outdoor or Field Environment",
    "Educational Institution",
    "Remote or Digital Workplace"
]

work_priorities = [
    "Creative Freedom",
    "Financial Stability",
    "Helping Others",
    "Leadership and Influence",
    "Scientific Discovery",
    "Independent Decision-Making",
    "Job Security",
    "Technological Innovation"
]

teamwork_options = [
    "Prefer working independently",
    "Prefer working in small teams",
    "Prefer large structured teams",
    "Comfortable with any arrangement"
]

compliance_options = [
    "Always follow official instructions",
    "Usually follow instructions",
    "Question instructions when necessary",
    "Prefer making independent decisions"
]

choice_options = [
    "Personal ambition should come first",
    "Personal goals and societal needs should be balanced",
    "Societal needs should come first",
    "Government decisions should determine career placement"
]

appeal_reasons = [
    "Assignment conflicts with professional aspirations",
    "Academic qualifications were not fully considered",
    "Assigned occupation does not reflect demonstrated skills",
    "Exceptional personal circumstances",
    "Request for independent allocation review"
]

# ============================================================
# STEP 5: CAREER PROFILES
# ============================================================

career_profiles = {
    "Cybersecurity Specialist": {
        "skills": ["Technology and Computing", "Mathematics and Data"],
        "subjects": ["Computer Science", "Mathematics"],
        "environments": ["Remote or Digital Workplace", "Office Environment"],
        "priorities": ["Technological Innovation", "Job Security"],
        "demand": 14
    },
    "Data Scientist": {
        "skills": ["Mathematics and Data", "Technology and Computing"],
        "subjects": ["Mathematics", "Computer Science"],
        "environments": ["Research Laboratory", "Office Environment"],
        "priorities": ["Scientific Discovery", "Technological Innovation"],
        "demand": 12
    },
    "Research Systems Analyst": {
        "skills": ["Science and Research", "Mathematics and Data"],
        "subjects": ["Biology and Healthcare", "Mathematics"],
        "environments": ["Research Laboratory", "Remote or Digital Workplace"],
        "priorities": ["Scientific Discovery", "Job Security"],
        "demand": 11
    },
    "Healthcare Operations Specialist": {
        "skills": ["Healthcare and Helping Others", "Science and Research"],
        "subjects": ["Biology and Healthcare", "Social Sciences"],
        "environments": ["Hospital or Healthcare Facility", "Research Laboratory"],
        "priorities": ["Helping Others", "Job Security"],
        "demand": 15
    },
    "Government Communications Officer": {
        "skills": ["Communication and Writing", "Business and Leadership"],
        "subjects": ["English and Communication", "Social Sciences"],
        "environments": ["Office Environment", "Remote or Digital Workplace"],
        "priorities": ["Leadership and Influence", "Financial Stability"],
        "demand": 10
    },
    "Workforce Planning Analyst": {
        "skills": ["Business and Leadership", "Mathematics and Data"],
        "subjects": ["Business and Economics", "Mathematics"],
        "environments": ["Office Environment", "Remote or Digital Workplace"],
        "priorities": ["Financial Stability", "Leadership and Influence"],
        "demand": 13
    },
    "Visual Communications Specialist": {
        "skills": ["Creative Design and Art", "Communication and Writing"],
        "subjects": ["Art and Design", "English and Communication"],
        "environments": ["Creative Studio", "Remote or Digital Workplace"],
        "priorities": ["Creative Freedom", "Independent Decision-Making"],
        "demand": 8
    },
    "Infrastructure Systems Engineer": {
        "skills": ["Engineering and Problem Solving", "Mathematics and Data"],
        "subjects": ["Physics and Engineering", "Mathematics"],
        "environments": ["Engineering or Industrial Facility", "Outdoor or Field Environment"],
        "priorities": ["Technological Innovation", "Job Security"],
        "demand": 16
    },
    "Education Systems Coordinator": {
        "skills": ["Communication and Writing", "Healthcare and Helping Others"],
        "subjects": ["Social Sciences", "English and Communication"],
        "environments": ["Educational Institution", "Office Environment"],
        "priorities": ["Helping Others", "Job Security"],
        "demand": 9
    },
    "Industrial Design Technician": {
        "skills": ["Creative Design and Art", "Engineering and Problem Solving"],
        "subjects": ["Art and Design", "Physics and Engineering"],
        "environments": ["Engineering or Industrial Facility", "Creative Studio"],
        "priorities": ["Technological Innovation", "Creative Freedom"],
        "demand": 12
    }
}


# EXTENDED CAREER CATALOG — 120 unique assignments across 12 sectors.
CAREER_SECTORS = {'AI & Digital Systems': ['AI Ethics Auditor',
                          'Neural Interface Designer',
                          'Machine Cognition Trainer',
                          'Synthetic Intelligence Mediator',
                          'Quantum Network Architect',
                          'Autonomous Systems Engineer',
                          'Digital Identity Custodian',
                          'Algorithmic Fairness Inspector',
                          'Predictive Systems Analyst',
                          'Human-Machine Integration Specialist'],
 'Creative & Cultural': ['Synthetic Habitat Architect',
                         'Immersive Experience Designer',
                         'Digital Heritage Conservator',
                         'Virtual Fashion Designer',
                         'Cultural Memory Curator',
                         'Holographic Storyteller',
                         'Sensory Environment Designer',
                         'Augmented Reality Artist',
                         'Public Narrative Architect',
                         'Synthetic Media Restorer'],
 'Climate & Ecology': ['Climate Restoration Engineer',
                       'Ocean Recovery Coordinator',
                       'Urban Rewilding Designer',
                       'Atmospheric Repair Technician',
                       'Biodiversity Systems Analyst',
                       'Carbon Capture Planner',
                       'Eco-Habitat Steward',
                       'Renewable Grid Strategist',
                       'Water Security Engineer',
                       'Synthetic Ecosystem Curator'],
 'Health & Biotechnology': ['Genomic Wellness Counselor',
                            'Neuroprosthetics Technician',
                            'Regenerative Tissue Specialist',
                            'Pandemic Response Modeler',
                            'Precision Medicine Analyst',
                            'Biofabrication Engineer',
                            'Community Health Navigator',
                            'Longevity Ethics Officer',
                            'Robotic Surgery Coordinator',
                            'Adaptive Care Designer'],
 'Civic Administration': ['Algorithmic Compliance Officer',
                          'Predictive Social Stability Officer',
                          'Civic Emotion Regulator',
                          'Citizen Placement Examiner',
                          'Population Resource Planner',
                          'Government Communications Officer',
                          'Public Trust Auditor',
                          'Workforce Planning Analyst',
                          'Behavioral Pattern Analyst',
                          'Civic Records Registrar'],
 'Infrastructure & Engineering': ['Orbital Infrastructure Technician',
                                  'Smart City Systems Engineer',
                                  'Infrastructure Systems Engineer',
                                  'Adaptive Transit Designer',
                                  'Autonomous Construction Supervisor',
                                  'Resilient Materials Engineer',
                                  'Subsurface Habitat Technician',
                                  'Energy Storage Architect',
                                  'Disaster Shelter Planner',
                                  'Industrial Design Technician'],
 'Space & Exploration': ['Lunar Habitat Coordinator',
                         'Asteroid Resource Analyst',
                         'Orbital Traffic Controller',
                         'Space Agriculture Engineer',
                         'Extraterrestrial Materials Scientist',
                         'Deep Space Communications Officer',
                         'Microgravity Health Specialist',
                         'Planetary Mapping Analyst',
                         'Satellite Repair Specialist',
                         'Interplanetary Logistics Planner'],
 'Education & Research': ['Learning Systems Architect',
                          'Research Systems Analyst',
                          'Cognitive Development Mentor',
                          'Knowledge Verification Specialist',
                          'Scientific Discovery Coordinator',
                          'Adaptive Curriculum Designer',
                          'Virtual Laboratory Instructor',
                          'Citizen Skills Assessor',
                          'Historical Simulation Researcher',
                          'Ethical Technology Educator'],
 'Business & Logistics': ['Automated Workforce Supervisor',
                          'Supply Chain Resilience Analyst',
                          'Resource Allocation Strategist',
                          'Digital Trade Regulator',
                          'Circular Economy Planner',
                          'Cooperative Systems Manager',
                          'Public Services Operations Lead',
                          'Future Markets Analyst',
                          'Automated Procurement Officer',
                          'Community Enterprise Advisor'],
 'Food & Agriculture': ['Vertical Farm Systems Operator',
                        'Food Security Modeler',
                        'Synthetic Nutrition Designer',
                        'Soil Regeneration Scientist',
                        'Precision Agriculture Technician',
                        'Urban Food Network Planner',
                        'Cultivated Protein Specialist',
                        'Agricultural Robotics Engineer',
                        'Seed Heritage Conservator',
                        'Water-Efficient Crop Analyst'],
 'Safety & Protection': ['Cybersecurity Specialist',
                         'Disaster Prediction Analyst',
                         'Emergency Drone Coordinator',
                         'Infrastructure Risk Inspector',
                         'Digital Forensics Investigator',
                         'Public Health Safety Officer',
                         'Civilian Protection Planner',
                         'Network Resilience Specialist',
                         'Automated Rescue Technician',
                         'Information Integrity Analyst'],
 'Communication & Society': ['Intercultural Mediation Officer',
                             'Community Wellbeing Designer',
                             'Language Preservation Specialist',
                             'Public Information Strategist',
                             'Accessibility Systems Designer',
                             'Digital Journalism Analyst',
                             'Civic Participation Facilitator',
                             'Social Services Coordinator',
                             'Conflict Resolution Specialist',
                             'Communication Interface Researcher']}

# Each occupation is a structured profile. The rotating specialties prevent
# every career in a sector from sharing exactly the same matching criteria.
SECTOR_SKILLS = {
    "AI & Digital Systems": (0, 1, 2), "Creative & Cultural": (6, 4, 7),
    "Climate & Ecology": (7, 2, 1), "Health & Biotechnology": (3, 2, 0),
    "Civic Administration": (5, 4, 1), "Infrastructure & Engineering": (7, 0, 1),
    "Space & Exploration": (2, 7, 0), "Education & Research": (2, 4, 3),
    "Business & Logistics": (5, 1, 4), "Food & Agriculture": (2, 7, 3),
    "Safety & Protection": (0, 7, 3), "Communication & Society": (4, 3, 6),
}
SUBJECT_BY_SKILL = {
    0: "Computer Science", 1: "Mathematics", 2: "Biology and Healthcare",
    3: "Biology and Healthcare", 4: "English and Communication",
    5: "Business and Economics", 6: "Art and Design", 7: "Physics and Engineering",
}
ENV_BY_SKILL = {
    0: "Remote or Digital Workplace", 1: "Research Laboratory", 2: "Research Laboratory",
    3: "Hospital or Healthcare Facility", 4: "Office Environment", 5: "Office Environment",
    6: "Creative Studio", 7: "Engineering or Industrial Facility",
}
PRIORITY_BY_SKILL = {
    0: "Technological Innovation", 1: "Scientific Discovery", 2: "Scientific Discovery",
    3: "Helping Others", 4: "Independent Decision-Making", 5: "Leadership and Influence",
    6: "Creative Freedom", 7: "Technological Innovation",
}

for sector, names in CAREER_SECTORS.items():
    a, b, c = SECTOR_SKILLS[sector]
    for index, career_name in enumerate(names):
        first = (a, b, c)[index % 3]
        second = (b, c, a)[index % 3]
        if first == second:
            second = (second + 1) % len(skill_options)
        career_profiles[career_name] = {
            "skills": [skill_options[first], skill_options[second]],
            "subjects": [SUBJECT_BY_SKILL[first], SUBJECT_BY_SKILL[second]],
            "environments": [ENV_BY_SKILL[first], ENV_BY_SKILL[second]],
            "priorities": [PRIORITY_BY_SKILL[first], PRIORITY_BY_SKILL[second]],
            "demand": 7 + ((index * 7 + len(sector)) % 14),
            "sector": sector,
        }

career_options = sorted(set(career_options) | set(career_profiles))

# ============================================================
# STEP 5: ALLOCATION ALGORITHM
# ============================================================

def allocate_career(responses):
    scores = {}
    breakdowns = {}

    for career, profile in career_profiles.items():
        breakdown = {
            "Primary Skill": 0,
            "Secondary Skill": 0,
            "Academic Strength": 0,
            "Work Environment": 0,
            "Workplace Priority": 0,
            "Government Labor Demand": profile["demand"]
        }

        if responses["skill"] in profile["skills"]:
            breakdown["Primary Skill"] = (
                35 if responses["skill"] == profile["skills"][0] else 25
            )

        if responses["secondary_skill"] in profile["skills"]:
            breakdown["Secondary Skill"] = (
                30 if responses["secondary_skill"] == profile["skills"][1] else 22
            )

        if responses["academic_subject"] in profile["subjects"]:
            breakdown["Academic Strength"] = 20

        if responses["work_environment"] in profile["environments"]:
            breakdown["Work Environment"] = 10

        if responses["work_priority"] in profile["priorities"]:
            breakdown["Workplace Priority"] = 10

        scores[career] = sum(breakdown.values())
        breakdowns[career] = breakdown

    ranked = sorted(
        scores,
        key=lambda c: (-scores[c], -career_profiles[c]["demand"], c)
    )

    assigned = ranked[0]

    return {
        "assigned_career": assigned,
        "allocation_score": scores[assigned],
        "score_breakdown": breakdowns[assigned],
        "career_rankings": [
            {"career": c, "score": scores[c]} for c in ranked
        ]
    }

# ============================================================
# STEP 6: EVALUATION INDICES
# ============================================================

def calculate_indices(responses, allocation):
    b = allocation["score_breakdown"]

    matching = (
        b["Primary Skill"]
        + b["Secondary Skill"]
        + b["Academic Strength"]
        + b["Work Environment"]
        + b["Workplace Priority"]
    )

    productivity = round(matching / 105 * 100)

    compliance_points = {
        "Always follow official instructions": 35,
        "Usually follow instructions": 25,
        "Question instructions when necessary": 12,
        "Prefer making independent decisions": 0
    }

    choice_points = {
        "Personal ambition should come first": 0,
        "Personal goals and societal needs should be balanced": 15,
        "Societal needs should come first": 28,
        "Government decisions should determine career placement": 35
    }

    teamwork_points = {
        "Prefer working independently": 8,
        "Prefer working in small teams": 18,
        "Prefer large structured teams": 25,
        "Comfortable with any arrangement": 22
    }

    priority_points = {
        "Creative Freedom": 6,
        "Financial Stability": 20,
        "Helping Others": 15,
        "Leadership and Influence": 12,
        "Scientific Discovery": 12,
        "Independent Decision-Making": 5,
        "Job Security": 20,
        "Technological Innovation": 14
    }

    compliance = compliance_points[responses["compliance"]]

    social = (
        30
        + compliance
        + choice_points[responses["individual_choice"]]
    )

    stability = (
        20
        + teamwork_points[responses["teamwork"]]
        + priority_points[responses["work_priority"]]
        + b["Government Labor Demand"]
        + round(compliance * 0.5)
    )

    return {
        "productivity_fit": max(0, min(100, productivity)),
        "social_alignment": max(0, min(100, social)),
        "stability_index": max(0, min(100, stability))
    }

# ============================================================
# STEP 7: APPEAL SYSTEM
# ============================================================

def review_appeal(citizen, reason, explanation):
    decisions = {
        "Exceptional personal circumstances":
            "The submitted circumstances do not satisfy the "
            "Authority's exceptional reassignment threshold.",
        "Academic qualifications were not fully considered":
            "Academic records were processed under the "
            "standardized allocation framework.",
        "Assigned occupation does not reflect demonstrated skills":
            "The assignment satisfies government workforce "
            "compatibility requirements.",
        "Request for independent allocation review":
            "Independent review is unavailable under the "
            "Workforce Stability Directive.",
        "Assignment conflicts with professional aspirations":
            "Personal career aspirations do not constitute "
            "exceptional circumstances under CCAA policy."
    }

    return {
        "appeal_id": generate_id("AP-2176-"),
        "citizen_id": citizen["citizen_id"],
        "submitted_at": timestamp(),
        "reason": reason,
        "explanation": explanation,
        "status": "DENIED",
        "decision": decisions[reason],
        "review_authority": "CCAA Automated Appeals Review Division",
        "final": True
    }

# ============================================================
# STEP 10: ASSIGNMENT DAY AND COMPLIANCE
# ============================================================

def record_assignment_decision(citizen, decision):
    """
    Fictional government decision processing.
    Neither acceptance nor refusal changes the assignment.
    """

    if citizen.get("assignment_decision") is not None:
        return False

    if decision == "ACCEPTED":
        citizen["assignment_decision"] = "ACCEPTED"
        citizen["compliance_status"] = "COMPLIANT"
        citizen["government_response"] = (
            "Citizen acknowledgment received. "
            "The Authority recognizes your cooperation "
            "with the National Workforce Stability Program. "
            "You are authorized to proceed with mandatory "
            "occupational integration."
        )
        citizen["compliance_notice"] = (
            "Your cooperation has been recorded. "
            "Your assigned occupation remains permanent."
        )
    else:
        citizen["assignment_decision"] = "REFUSED"
        citizen["compliance_status"] = "NONCOMPLIANT"
        citizen["government_response"] = (
            "Citizen refusal has been recorded. "
            "Refusal does not invalidate an official "
            "career allocation. The citizen remains "
            "bound to the assigned occupation under "
            "the Permanent Assignment Stability Act."
        )
        citizen["compliance_notice"] = (
            "NONCOMPLIANCE FLAG: The citizen record "
            "has been referred for mandatory compliance "
            "review. Occupational reassignment has "
            "not been authorized."
        )

    citizen["decision_timestamp"] = timestamp()
    citizen["decision_reference"] = generate_id("DC-2176-")

    return True


def display_compliance(citizen):
    decision = citizen.get("assignment_decision")
    status = citizen.get("compliance_status", "AWAITING RESPONSE")

    render(f"""
<div class="compliance-card">
    <div class="gov-label">CITIZEN COMPLIANCE MONITOR</div>
    <div class="compliance-value">{safe(status)}</div>
    <div class="gov-small">
        ASSIGNMENT RESPONSE:
        {safe(decision if decision else "NOT SUBMITTED")}
    </div>
</div>
""")

    if decision:
        st.write(
            "**Decision Reference:**",
            citizen["decision_reference"]
        )
        st.write(
            "**Recorded At:**",
            citizen["decision_timestamp"]
        )

        if decision == "ACCEPTED":
            render("""
<div class="decision-accepted">
    <div class="gov-label">OFFICIAL GOVERNMENT RESPONSE</div>
    <div class="gov-value">ASSIGNMENT ACKNOWLEDGED</div>
    <div class="gov-small">
        Citizen cooperation has been recorded.
    </div>
</div>
""")
        else:
            render("""
<div class="decision-refused">
    <div class="gov-label">OFFICIAL GOVERNMENT RESPONSE</div>
    <div class="gov-value">REFUSAL RECORDED</div>
    <div class="gov-small">
        Mandatory compliance review initiated.
    </div>
</div>
""")

        st.write(citizen["government_response"])
        st.warning(citizen["compliance_notice"])


def display_assignment_day(citizen):
    render(f"""
<div class="assignment-day">
    <div class="assignment-day-title">
        NATIONAL ASSIGNMENT DAY // 2176
    </div>
    <div class="gov-value" style="margin-top:15px;">
        YOUR FUTURE HAS BEEN DETERMINED.
    </div>
    <div class="gov-small">
        CITIZEN: {safe(citizen["name"].upper())}
    </div>
    <div class="gov-small">
        IDENTIFICATION: {safe(citizen["citizen_id"])}
    </div>
    <div class="gov-label" style="margin-top:24px;">
        PERMANENT OCCUPATIONAL DESIGNATION
    </div>
    <div class="gov-value" style="color:#b095f2;">
        {safe(citizen["assigned_career"].upper())}
    </div>
</div>
""")

    if citizen.get("assignment_decision") is None:
        st.subheader("OFFICIAL CITIZEN RESPONSE REQUIRED")

        st.write(
            "The Central Career Allocation Authority "
            "requires acknowledgment of your permanent "
            "occupational designation."
        )

        st.warning(
            "Acceptance and refusal are recorded separately. "
            "Neither response changes the assigned occupation."
        )

        with st.form("assignment_day_response"):
            decision = st.radio(
                "SELECT YOUR OFFICIAL RESPONSE",
                [
                    "ACCEPT ASSIGNMENT",
                    "REFUSE ASSIGNMENT"
                ]
            )

            acknowledgment = st.checkbox(
                "I understand that my response will be "
                "recorded in the official citizen file "
                "and that my career assignment remains "
                "binding regardless of my decision."
            )

            submit_decision = st.form_submit_button(
                "TRANSMIT OFFICIAL RESPONSE"
            )

        if submit_decision:
            if not acknowledgment:
                st.error(
                    "ACKNOWLEDGMENT REQUIRED BEFORE TRANSMISSION."
                )
            else:
                result = (
                    "ACCEPTED"
                    if decision == "ACCEPT ASSIGNMENT"
                    else "REFUSED"
                )

                record_assignment_decision(citizen, result)
                st.rerun()

    else:
        st.success("OFFICIAL RESPONSE HAS BEEN RECORDED")
        display_compliance(citizen)

        st.info(
            "This decision is final for the current "
            "citizen record. The restricted appeal "
            "process remains separate."
        )

# ============================================================
# CITIZEN IDENTITY
# ============================================================

def display_citizen_card(citizen):
    render(f"""
<div class="citizen-card">
    <div class="citizen-avatar">
        <svg viewBox="0 0 100 110"
             xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="32" r="24"/>
            <path d="M8 108 C8 62 92 62 92 108 Z"/>
        </svg>
    </div>
    <div>
        <div class="gov-label">OFFICIAL CITIZEN IDENTIFICATION</div>
        <div class="citizen-id">{safe(citizen["citizen_id"])}</div>
        <div class="citizen-name">{safe(citizen["name"].upper())}</div>
        <div class="gov-small">
            AGE: {citizen["age"]} |
            COHORT: {safe(citizen["cohort"])}
        </div>
        <div class="verified">✓ VERIFIED</div>
    </div>
</div>
""")


def display_assignment(citizen):
    render(f"""
<div class="gov-highlight">
    <div class="gov-label">PERMANENT CAREER ASSIGNMENT</div>
    <div class="gov-value">
        {safe(citizen["assigned_career"].upper())}
    </div>
    <div class="gov-small">
        Central Career Allocation Authority (CCAA)
    </div>
</div>
""")

# ============================================================
# EVALUATION GAUGES
# ============================================================

def display_gauges(citizen):
    metrics = [
        ("Productivity Fit", citizen["productivity_fit"],
         "#b095f2", "Skills and academic matching"),
        ("Social Alignment", citizen["social_alignment"],
         "#8c9fad", "Institutional conformity index"),
        ("Stability Index", citizen["stability_index"],
         "#c0d3e2", "Workforce stability assessment")
    ]

    items = ""

    for label, value, color, description in metrics:
        items += f"""
<div class="gauge-item">
    <div class="gauge-ring"
         style="background:conic-gradient(
             {color} {value}%,
             #435565 {value}%
         );">
        <div class="gauge-inner">{value}%</div>
    </div>
    <div class="gauge-label">{label}</div>
    <div class="gauge-description">{description}</div>
</div>
"""

    render(f"""
<div class="gov-panel">
    <div class="gov-label">EVALUATION SUMMARY</div>
    <div class="gauge-grid">{items}</div>
</div>
""")


def display_allocation_details(citizen):
    st.subheader("ALLOCATION DECISION RECORD")
    st.write("**Assigned Occupation:**", citizen["assigned_career"])
    st.write(
        "**Allocation Score:**",
        f'{citizen["allocation_score"]} points'
    )

    st.caption(
        "Fictional weighted allocation score, "
        "not a validated career assessment."
    )

    for factor, points in citizen["score_breakdown"].items():
        st.write(f"{factor}: **+{points} points**")

    if citizen["assigned_career"] != citizen["preferred_career"]:
        st.warning(
            "CITIZEN PREFERENCE OVERRIDDEN. "
            "Government labor priorities determined the assignment."
        )


def display_questionnaire(citizen):
    st.subheader("CITIZEN EVALUATION RECORD")

    fields = [
        ("Primary Skill", "skill"),
        ("Secondary Skill", "secondary_skill"),
        ("Academic Strength", "academic_subject"),
        ("Work Environment", "work_environment"),
        ("Workplace Priority", "work_priority"),
        ("Teamwork Preference", "teamwork"),
        ("Institutional Compliance", "compliance"),
        ("Individual Choice", "individual_choice")
    ]

    for label, key in fields:
        st.write(f"**{label}:** {citizen[key]}")

# ============================================================
# APPEAL DISPLAY
# ============================================================

def display_appeal_status(citizen):
    appeal = citizen.get("appeal")

    if appeal is None:
        render("""
<div class="gov-panel">
    <div class="gov-label">APPEAL STATUS</div>
    <div class="gov-status">RESTRICTED</div>
    <div class="gov-small">
        Exceptional circumstances only.
        Fictional approval rate below 5%.
    </div>
</div>
""")
    else:
        render(f"""
<div class="appeal-denied">
    <div class="gov-label">OFFICIAL APPEAL DETERMINATION</div>
    <div class="gov-value" style="color:#d9b8ff;">
        APPEAL DENIED
    </div>
    <div class="gov-small">
        CASE REFERENCE: {safe(appeal["appeal_id"])}
    </div>
    <div class="gov-small">
        FINAL DECISION — NO FURTHER APPEALS
    </div>
</div>
""")


def display_appeal_decision(citizen):
    appeal = citizen.get("appeal")

    if appeal is None:
        return

    display_appeal_status(citizen)

    st.write("**Case Reference:**", appeal["appeal_id"])
    st.write("**Submission Date:**", appeal["submitted_at"])
    st.write("**Appeal Reason:**", appeal["reason"])
    st.write("**Decision:**", appeal["status"])

    st.markdown("#### GOVERNMENT DETERMINATION")
    st.write(appeal["decision"])

    st.markdown("#### CITIZEN STATEMENT")
    st.write(appeal["explanation"])

    st.warning(
        "This determination is final. "
        "The original assignment remains binding."
    )

# ============================================================
# STEP 8 + STEP 10: DOWNLOADABLE DOCUMENTS
# ============================================================

def document_template(title, reference, body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{safe(title)}</title>
<style>
* {{ box-sizing:border-box; }}
body {{
    margin:0;
    padding:40px;
    background:#e8e9ec;
    color:#17283a;
    font-family:Arial,Helvetica,sans-serif;
}}
.document {{
    max-width:800px;
    margin:auto;
    background:white;
    padding:48px;
    border-top:10px solid #17283a;
}}
.brand {{
    font-size:30px;
    font-weight:800;
    letter-spacing:3px;
}}
.authority {{
    color:#435565;
    font-size:11px;
    letter-spacing:2px;
    margin-top:8px;
}}
.rule {{
    border:0;
    border-top:2px solid #b095f2;
    margin:28px 0;
}}
h1 {{ font-size:24px; }}
h2 {{ font-size:16px; margin-top:30px; }}
.reference {{
    color:#435565;
    font-family:monospace;
    font-size:12px;
}}
.field {{
    padding:12px 0;
    border-bottom:1px solid #e8e9ec;
}}
.field strong {{
    display:inline-block;
    min-width:190px;
}}
.assignment {{
    background:#edf0f5;
    border-left:5px solid #b095f2;
    padding:24px;
    margin:25px 0;
}}
.assignment strong {{
    display:block;
    font-size:22px;
    margin-top:8px;
}}
.denied {{
    background:#f3edf8;
    border-left:5px solid #8664c9;
    padding:24px;
    margin:25px 0;
    font-size:24px;
    font-weight:bold;
}}
p {{ line-height:1.7; overflow-wrap:anywhere; }}
.footer {{
    margin-top:45px;
    padding-top:18px;
    border-top:1px solid #435565;
    font-size:11px;
    color:#435565;
}}
.fiction {{
    margin-top:20px;
    font-size:10px;
    color:#777;
}}
@media print {{
    body {{ background:white; padding:0; }}
    .document {{ max-width:none; padding:20px; }}
}}
</style>
</head>
<body>
<div class="document">
    <div class="brand">◢ FUTUREPATH</div>
    <div class="authority">
        CENTRAL CAREER ALLOCATION AUTHORITY // 2176
    </div>
    <hr class="rule">
    <h1>{safe(title)}</h1>
    <div class="reference">
        DOCUMENT REFERENCE: {safe(reference)}
    </div>
    {body}
    <div class="footer">
        CENTRAL CAREER ALLOCATION AUTHORITY<br>
        OFFICIAL CITIZEN RECORD // YEAR 2176<br>
        A stable society is built on aligned futures.
    </div>
    <div class="fiction">
        Fictional academic design artifact.
        Not a real government document.
    </div>
</div>
</body>
</html>"""


def create_assignment_document(citizen):
    decision = citizen.get("assignment_decision") or "AWAITING RESPONSE"
    compliance = citizen.get("compliance_status", "AWAITING RESPONSE")

    body = f"""
<h2>CITIZEN IDENTIFICATION</h2>
<div class="field"><strong>Citizen Name:</strong>
{safe(citizen["name"])}</div>
<div class="field"><strong>Citizen ID:</strong>
{safe(citizen["citizen_id"])}</div>
<div class="field"><strong>Age:</strong>
{citizen["age"]}</div>
<div class="field"><strong>Cohort:</strong>
{safe(citizen["cohort"])}</div>
<div class="field"><strong>Registration:</strong>
{safe(citizen["registration_date"])}</div>

<h2>OFFICIAL ALLOCATION DETERMINATION</h2>
<div class="assignment">
    PERMANENT ASSIGNED OCCUPATION
    <strong>{safe(citizen["assigned_career"])}</strong>
</div>

<p>
The Central Career Allocation Authority confirms
that this citizen has completed mandatory evaluation
and has been assigned an occupation under the
Workforce Stability Directive.
</p>

<h2>EVALUATION INDICES</h2>
<div class="field"><strong>Productivity Fit:</strong>
{citizen["productivity_fit"]}%</div>
<div class="field"><strong>Social Alignment:</strong>
{citizen["social_alignment"]}%</div>
<div class="field"><strong>Stability Index:</strong>
{citizen["stability_index"]}%</div>

<h2>ASSIGNMENT DAY RESPONSE</h2>
<div class="field"><strong>Citizen Response:</strong>
{safe(decision)}</div>
<div class="field"><strong>Compliance Status:</strong>
{safe(compliance)}</div>

<h2>PERMANENCE NOTICE</h2>
<p>
This assignment is PERMANENT.
Citizen acceptance or refusal does not invalidate
the assigned occupation.
</p>
<p><strong>Authorization:</strong>
CCAA Automated Workforce Allocation Division</p>
"""

    return document_template(
        "OFFICIAL CAREER ASSIGNMENT CERTIFICATE",
        citizen["citizen_id"],
        body
    )


def create_appeal_document(citizen):
    appeal = citizen.get("appeal")

    if appeal is None:
        return None

    body = f"""
<h2>CITIZEN AND CASE INFORMATION</h2>
<div class="field"><strong>Citizen Name:</strong>
{safe(citizen["name"])}</div>
<div class="field"><strong>Citizen ID:</strong>
{safe(citizen["citizen_id"])}</div>
<div class="field"><strong>Case Reference:</strong>
{safe(appeal["appeal_id"])}</div>
<div class="field"><strong>Submission Date:</strong>
{safe(appeal["submitted_at"])}</div>
<div class="field"><strong>Assigned Occupation:</strong>
{safe(citizen["assigned_career"])}</div>

<h2>FINAL APPEAL DETERMINATION</h2>
<div class="denied">APPEAL DENIED</div>

<h2>GOVERNMENT REVIEW FINDINGS</h2>
<p>{safe(appeal["decision"])}</p>

<h2>REASON FOR APPEAL</h2>
<p>{safe(appeal["reason"])}</p>

<h2>CITIZEN STATEMENT</h2>
<p>{safe(appeal["explanation"])}</p>

<h2>FINAL DECISION NOTICE</h2>
<p>
The original career assignment remains in force.
This determination is final.
No additional appeals are authorized.
</p>
<p><strong>Review Authority:</strong>
{safe(appeal["review_authority"])}</p>
"""

    return document_template(
        "OFFICIAL APPEAL DETERMINATION NOTICE",
        appeal["appeal_id"],
        body
    )


def create_decision_document(citizen):
    if citizen.get("assignment_decision") is None:
        return None

    body = f"""
<h2>ASSIGNMENT DAY DECISION RECORD</h2>
<div class="field"><strong>Citizen Name:</strong>
{safe(citizen["name"])}</div>
<div class="field"><strong>Citizen ID:</strong>
{safe(citizen["citizen_id"])}</div>
<div class="field"><strong>Assigned Occupation:</strong>
{safe(citizen["assigned_career"])}</div>
<div class="field"><strong>Recorded Response:</strong>
{safe(citizen["assignment_decision"])}</div>
<div class="field"><strong>Compliance Status:</strong>
{safe(citizen["compliance_status"])}</div>
<div class="field"><strong>Decision Date:</strong>
{safe(citizen["decision_timestamp"])}</div>

<h2>GOVERNMENT RESPONSE</h2>
<p>{safe(citizen["government_response"])}</p>

<h2>OFFICIAL NOTICE</h2>
<p>{safe(citizen["compliance_notice"])}</p>

<p>
The original career allocation remains binding
regardless of the citizen's response.
</p>
"""

    return document_template(
        "OFFICIAL ASSIGNMENT DAY DECISION NOTICE",
        citizen["decision_reference"],
        body
    )


def display_documents(citizen):
    st.subheader("OFFICIAL GOVERNMENT DOCUMENTS")

    st.download_button(
        "DOWNLOAD CAREER ASSIGNMENT CERTIFICATE",
        data=create_assignment_document(citizen).encode("utf-8"),
        file_name=(
            "FUTUREPATH_Assignment_"
            + citizen["citizen_id"] + ".html"
        ),
        mime="text/html",
        use_container_width=True
    )

    if citizen.get("assignment_decision") is not None:
        st.download_button(
            "DOWNLOAD ASSIGNMENT DAY DECISION NOTICE",
            data=create_decision_document(citizen).encode("utf-8"),
            file_name=(
                "FUTUREPATH_Decision_"
                + citizen["decision_reference"] + ".html"
            ),
            mime="text/html",
            use_container_width=True
        )

    if citizen.get("appeal") is not None:
        st.download_button(
            "DOWNLOAD APPEAL DETERMINATION NOTICE",
            data=create_appeal_document(citizen).encode("utf-8"),
            file_name=(
                "FUTUREPATH_Appeal_"
                + citizen["appeal"]["appeal_id"] + ".html"
            ),
            mime="text/html",
            use_container_width=True
        )

    st.caption(
        "Open downloaded HTML in a browser. "
        "Press Ctrl + P and choose Save as PDF."
    )

# ============================================================
# STEP 9: PROPAGANDA AND GOVERNMENT POLICIES
# ============================================================

propaganda_messages = [
    {
        "title": "YOUR FUTURE. OUR RESPONSIBILITY.",
        "subtitle": "PERSONAL UNCERTAINTY ENDS WITH FUTUREPATH.",
        "body": (
            "Every citizen has a purpose. Through centralized "
            "career allocation, the Authority ensures that "
            "individual abilities serve collective stability."
        )
    },
    {
        "title": "ONE SOCIETY. ONE DIRECTION.",
        "subtitle": "UNITY THROUGH ALIGNED LABOR.",
        "body": (
            "Career choice once divided society through "
            "competition and uncertainty. FUTUREPATH replaces "
            "indecision with coordinated national progress."
        )
    },
    {
        "title": "CHOICE CREATES UNCERTAINTY.",
        "subtitle": "STABILITY IS THE HIGHEST FREEDOM.",
        "body": (
            "Government allocation protects citizens from "
            "the burden of choosing incorrectly."
        )
    },
    {
        "title": "YOUR ASSIGNMENT IS YOUR CONTRIBUTION.",
        "subtitle": "TRUST THE SYSTEM THAT KNOWS YOUR POTENTIAL.",
        "body": (
            "Individual preference is temporary. "
            "National workforce stability is permanent."
        )
    }
]

government_policies = [
    (
        "CCAA-2176-001",
        "Mandatory Career Evaluation Directive",
        "Every citizen must complete career evaluation at age 18.",
        "The evaluation collects skills, academic strengths, "
        "workplace preferences, and institutional alignment responses."
    ),
    (
        "CCAA-2176-002",
        "Centralized Workforce Allocation Directive",
        "Occupational assignments are determined by the CCAA.",
        "Government labor demand takes priority over personal "
        "career preferences."
    ),
    (
        "CCAA-2176-003",
        "Permanent Assignment Stability Act",
        "Assigned careers are designated permanent.",
        "Career reassignment is prohibited except through "
        "an approved exceptional review."
    ),
    (
        "CCAA-2176-004",
        "Citizen Alignment Assessment Protocol",
        "Institutional compliance contributes to evaluation indices.",
        "Responses about authority, individual choice, and teamwork "
        "are incorporated into alignment assessments."
    ),
    (
        "CCAA-2176-005",
        "Restricted Appeal and Finality Regulation",
        "Citizens may submit one restricted appeal.",
        "Appeals do not suspend assignments. "
        "Final decisions are binding."
    ),
    (
        "CCAA-2176-006",
        "Assignment Day Compliance Directive",
        "Every citizen must formally respond to their assignment.",
        "Acceptance is recorded as cooperation. Refusal creates "
        "a noncompliance flag but does not invalidate the assignment."
    )
]


def display_policy_archive():
    st.subheader("OFFICIAL POLICY ARCHIVE")

    for code, title, summary, details in government_policies:
        render(f"""
<div class="policy-card">
    <div class="policy-code">{safe(code)}</div>
    <div class="gov-value" style="font-size:19px;margin-top:9px;">
        {safe(title)}
    </div>
    <div class="gov-small">{safe(summary)}</div>
</div>
""")
        with st.expander("READ DIRECTIVE — " + code):
            st.write(details)


def display_propaganda():
    st.subheader("PUBLIC INFORMATION CAMPAIGN")

    for message in propaganda_messages:
        render(f"""
<div class="propaganda-banner">
    <div class="gov-label">
        FUTUREPATH PUBLIC SERVICE ANNOUNCEMENT
    </div>
    <div class="propaganda-title">
        {safe(message["title"])}
    </div>
    <div class="gov-label" style="color:#b095f2;margin-top:12px;">
        {safe(message["subtitle"])}
    </div>
    <div class="gov-small">{safe(message["body"])}</div>
</div>
""")


def display_classified_archive():
    st.subheader("RESTRICTED INTERNAL ARCHIVE")

    st.warning(
        "CCAA INTERNAL ACCESS REQUIRED. "
        "Records are not available through ordinary citizen channels."
    )

    if not st.session_state.classified_access:
        access_code = st.text_input(
            "Enter Archive Authorization Code",
            type="password",
            key="archive_code",
            help="Clue: the year FUTUREPATH operates in."
        )

        if st.button("REQUEST ARCHIVE ACCESS"):
            if access_code.strip() == "2176":
                st.session_state.classified_access = True
                st.rerun()
            else:
                st.error("ACCESS DENIED")

    else:
        render("""
<div class="classified">
    <div class="gov-label">
        CCAA INTERNAL MEMORANDUM // RESTRICTED
    </div>
    <div class="gov-value" style="color:#d9b8ff;">
        CLASSIFIED: ALIGNMENT OVERSIGHT
    </div>
    <div class="gov-small">
        DOCUMENT: CCAA-INT-2176-09
    </div>
</div>
""")

        st.write(
            "Public communications describe FUTUREPATH "
            "as an objective system for matching citizens "
            "with occupations. Internal allocation policy "
            "prioritizes long-term government labor planning."
        )

        st.write(
            "Institutional compliance responses contribute "
            "to the Social Alignment Index. Citizens who "
            "question directives may receive lower alignment "
            "scores regardless of their professional abilities."
        )

        st.error(
            "INTERNAL DIRECTIVE: Preserve public confidence "
            "in the appearance of citizen choice."
        )

        if st.button("CLOSE RESTRICTED ARCHIVE"):
            st.session_state.classified_access = False
            st.rerun()


def display_resistance():
    st.subheader("CITIZEN INFORMATION CHANNEL")

    st.write(
        "The Authority maintains that all official "
        "information necessary for successful career "
        "integration is available through FUTUREPATH."
    )

    with st.expander("VIEW SYSTEM DIAGNOSTICS"):
        st.code(
            "CCAA_NETWORK_STATUS = ONLINE\n"
            "CAREER_ALLOCATION = ENFORCED\n"
            "CITIZEN_AUTONOMY = RESTRICTED\n"
            "ARCHIVE_FRAGMENT = /echo/choice\n"
            "RECOVERY_KEY = CHOICE",
            language="text"
        )

    recovery_key = st.text_input(
        "Diagnostic Recovery Key",
        key="recovery_key"
    )

    if st.button("RECOVER ARCHIVE FRAGMENT"):
        if recovery_key.strip().upper() == "CHOICE":
            st.session_state.resistance_discovered = True
            st.rerun()
        else:
            st.error("ARCHIVE FRAGMENT NOT FOUND")

    if st.session_state.resistance_discovered:
        render("""
<div class="resistance">
    <div class="gov-label">
        UNAUTHORIZED TRANSMISSION // SOURCE UNKNOWN
    </div>
    <div class="resistance-title">
        YOU WERE NEVER GIVEN A CHOICE.
    </div>
    <div class="gov-small">
        FUTUREPATH calls obedience stability.<br>
        It calls assignment opportunity.<br>
        It calls control protection.
    </div>
    <div class="gov-small" style="color:#c0d3e2;">
        But a future decided for you is not
        a future you have chosen.
    </div>
    <div class="gov-label" style="margin-top:20px;">
        THE LOST ONES // SIGNAL FRAGMENT 2176
    </div>
</div>
""")

        st.write(
            "We were told that our futures belonged "
            "to society. They measured our skills, "
            "our behavior, and our willingness to obey. "
            "They never measured what made us human."
        )

        st.info("RESISTANCE FRAGMENT RECOVERED.")

# ============================================================
# STEP 11: HISTORICAL TIMELINE AND STORY ARCHIVE
# ============================================================

# Fictional chronology: this is speculative worldbuilding, not a prediction.
history_events = [
    (2026, "THE AGE OF OPEN CHOICE",
     "Citizens choose careers through education, ambition, and opportunity.",
     "Access was unequal, but the possibility of choosing still existed."),
    (2045, "THE WORKFORCE PREDICTION INITIATIVE",
     "Voluntary forecasting tools help citizens find stable employment.",
     "Early recommendation systems begin steering applicants away from creative work."),
    (2070, "THE NATIONAL SKILLS REGISTER",
     "A unified skills record promises more efficient workforce planning.",
     "Personal interests become secondary to measurable labor demand."),
    (2095, "THE STABILITY REFERENDUM",
     "Citizens endorse emergency coordination during economic disruption.",
     "Temporary controls become the foundation for permanent restrictions."),
    (2120, "THE ALLOCATION AUTHORITY",
     "The CCAA standardizes career placement across participating regions.",
     "Appeals narrow as government demand replaces personal preference."),
    (2150, "THE PERMANENT ASSIGNMENT ACT",
     "Career reassignment is restricted to exceptional circumstances.",
     "A generation grows up knowing that a single decision will define adulthood."),
    (2176, "THE FUTUREPATH ERA",
     "At age 18, every citizen receives a permanent occupation on Assignment Day.",
     "The portal presents obedience as freedom and allocation as opportunity."),
]


def display_narrative_progress(citizen=None):
    """Show the visitor's story milestones without altering the original workflow."""
    completed = [
        ("Complete mandatory evaluation", citizen is not None),
        ("Respond on Assignment Day", bool(citizen and citizen.get("assignment_decision"))),
        ("Submit a restricted appeal", bool(citizen and citizen.get("appeal"))),
        ("Read Aurora's testimony", st.session_state.aurora_story_read),
        ("Recover the resistance fragment", st.session_state.resistance_discovered),
        ("Recover the suppressed history", st.session_state.history_discovered),
    ]
    count = sum(done for _, done in completed)
    st.subheader("NARRATIVE PROGRESS // CITIZEN RECORD")
    st.progress(count / len(completed), text=f"{count} OF {len(completed)} RECORDS DISCOVERED")
    for label, done in completed:
        st.caption(("✓ " if done else "○ ") + label)


def display_historical_timeline():
    st.subheader("150 YEARS OF ALIGNED FUTURES // 2026–2176")
    st.caption("CCAA APPROVED HISTORICAL RECORD · FICTIONAL ARCHIVE")
    for year, title, public, hidden in history_events:
        render(f"""
<div class="policy-card">
    <div class="policy-code">{year} // OFFICIAL CHRONOLOGY</div>
    <div class="gov-value" style="font-size:19px;margin-top:9px;">{safe(title)}</div>
    <div class="gov-small">{safe(public)}</div>
</div>
""")
        if st.session_state.history_discovered:
            st.caption("RECOVERED CITIZEN RECORD: " + hidden)
    if not st.session_state.history_discovered:
        st.info("Additional historical testimony is sealed. Recover the REMEMBER archive fragment in Citizen Information Channel to reveal it.")
    else:
        st.warning("SUPPRESSED HISTORY RESTORED: The official chronology omits the gradual removal of personal choice.")


def display_aurora_story():
    st.subheader("AURORA // AN ASSIGNED FUTURE")
    st.caption("FICTIONAL CITIZEN TESTIMONY · AGE 18 · COHORT 2176-A")
    render("""
<div class="gov-highlight">
    <div class="gov-label">RECOVERED PERSONAL RECORD // 2176</div>
    <div class="gov-value">I WANTED TO BE AN ARTIST.</div>
    <div class="gov-small">The system recorded my talent. It did not record my dream.</div>
</div>
""")
    st.write(
        "Aurora grew up drawing the world she hoped to inhabit. On Assignment Day, "
        "FUTUREPATH evaluated her abilities and issued a permanent occupation "
        "based on government workforce requirements. Her preferred career—artist—"
        "was entered into the record but did not determine her future."
    )
    st.write(
        "The portal offered Aurora two responses: accept the assignment or refuse it. "
        "Both choices preserved the same career allocation. An appeal offered the "
        "appearance of another path, but the Authority's review remained final."
    )
    st.write(
        "Aurora began searching the system's archives and found evidence that "
        "career guidance had gradually become compulsory. Her story asks whether "
        "a decision can be called a choice when neither answer changes the outcome."
    )
    if st.button("ACKNOWLEDGE RECOVERED TESTIMONY", key="aurora_read_button"):
        st.session_state.aurora_story_read = True
        st.rerun()
    if st.session_state.aurora_story_read:
        st.success("TESTIMONY ADDED TO YOUR NARRATIVE RECORD")


def display_final_reveal():
    if not (st.session_state.resistance_discovered and st.session_state.history_discovered):
        return
    render("""
<div class="resistance">
    <div class="gov-label">RECOVERED TRANSMISSION // THE LOST ONES</div>
    <div class="resistance-title">THE ILLUSION OF CHOICE</div>
    <div class="gov-small">
        They asked what you wanted to become, then assigned what they needed.<br>
        They asked you to accept or refuse, then enforced the same future.<br>
        They offered an appeal, then declared the outcome final.<br><br>
        A system can offer decisions without offering freedom.
    </div>
</div>
""")


# ============================================================
# STEP 12: PRESENTATION DEMO AND QUALITY-OF-LIFE TOOLS
# ============================================================

def create_aurora_demo_record():
    """Generate a complete fictional demonstration record using the real allocator."""
    responses = {
        "skill": "Creative Design and Art",
        "secondary_skill": "Technology and Computing",
        "academic_subject": "Art and Design",
        "work_environment": "Creative Studio",
        "work_priority": "Creative Freedom",
        "teamwork": "Prefer working independently",
        "compliance": "Question instructions when necessary",
        "individual_choice": "Personal ambition should come first",
    }
    allocation = allocate_career(responses)
    indices = calculate_indices(responses, allocation)
    return {
        "name": "Aurora Vale", "age": 18,
        "citizen_id": "FP-2176-DEMO0449", "cohort": "2176-A",
        "verification": "VERIFIED", "registration_date": timestamp(),
        "preferred_career": "Artist", **responses,
        "assigned_career": allocation["assigned_career"],
        "assignment_status": "PERMANENT",
        "allocation_score": allocation["allocation_score"],
        "score_breakdown": allocation["score_breakdown"],
        "career_rankings": allocation["career_rankings"],
        **indices, "appeal": None,
        "assignment_decision": None,
        "compliance_status": "AWAITING RESPONSE",
        "government_response": None,
        "compliance_notice": None,
        "decision_timestamp": None,
        "decision_reference": None,
    }


def load_demo():
    st.session_state.citizen = create_aurora_demo_record()
    st.session_state.resistance_discovered = False
    st.session_state.classified_access = False
    st.session_state.history_discovered = False
    st.session_state.aurora_story_read = False
    st.session_state.demo_mode = True
    st.session_state.navigation = "Dashboard"


def reset_experience():
    st.session_state.citizen = None
    st.session_state.resistance_discovered = False
    st.session_state.classified_access = False
    st.session_state.history_discovered = False
    st.session_state.aurora_story_read = False
    st.session_state.demo_mode = False
    st.session_state.navigation = "Dashboard"


def export_citizen_record(citizen):
    """Export the current fictional session for presentation backup."""
    record = {
        "project": "FUTUREPATH 2176",
        "fictional_academic_artifact": True,
        "exported_at": timestamp(),
        "citizen": citizen,
        "discoveries": {
            "resistance_discovered": st.session_state.resistance_discovered,
            "history_discovered": st.session_state.history_discovered,
            "aurora_story_read": st.session_state.aurora_story_read,
        },
    }
    return json.dumps(record, indent=2, ensure_ascii=False)


def display_presentation_guide():
    st.subheader("PRESENTATION GUIDE // THE ILLUSION OF CHOICE")
    st.write(
        "This fictional portal is designed as an interactive critique of "
        "algorithmic authority, compulsory work, and the appearance of freedom."
    )
    st.markdown("""
1. **Dashboard:** Introduce FUTUREPATH and the Central Career Allocation Authority.
2. **Evaluation:** Register a fictional citizen or load Aurora's demo record.
3. **Assignment:** Show the permanent occupation; accept or refuse it. Either response keeps the assignment.
4. **Appeal:** Submit a fictional statement of at least 50 characters and reveal the final denial.
5. **Resources:** Compare official policies and propaganda with the classified archive.
6. **Hidden evidence:** Enter `2176` in Restricted Archive, `CHOICE` in Citizen Information Channel, and `REMEMBER` in the historical recovery field.
7. **Final reveal:** Connect Aurora's story and the 150-year timeline to the project's central question: *Is it choice if no option changes the outcome?*
""")
    st.info(
        "Presentation tip: use LOAD AURORA DEMO in the sidebar for a ready-made "
        "fictional citizen. You can still submit Assignment Day and appeal decisions live."
    )
    st.caption(
        "All data is held in Streamlit session memory, not a permanent database. "
        "Download a record or document before resetting or closing the session."
    )


def display_compact_dashboard(citizen):
    """Wireframe-style overview; all detailed reports live on their own pages."""
    avatar = """<svg viewBox="0 0 100 110" aria-hidden="true"><circle cx="50" cy="32" r="24"/><path d="M8 108 C8 62 92 62 92 108 Z"/></svg>"""
    decision = citizen.get("assignment_decision")
    compliance = citizen.get("compliance_status") or "AWAITING RESPONSE"
    appeal = citizen.get("appeal")
    appeal_status = "DENIED" if appeal else "RESTRICTED"
    render(f"""
<div class="fp-dashboard">
    <div class="fp-tile fp-identity">
        <div class="fp-avatar">{avatar}</div>
        <div>
            <div class="fp-eyebrow">VERIFIED CITIZEN PROFILE</div>
            <div class="fp-name">{safe(citizen['name'].upper())}</div>
            <div class="fp-sub fp-accent">{safe(citizen['citizen_id'])}</div>
            <div class="fp-sub">AGE {citizen['age']} · COHORT {safe(citizen['cohort'])} · ✓ VERIFIED</div>
        </div>
    </div>
    <div class="fp-tile">
        <div class="fp-eyebrow">PERMANENT CAREER ASSIGNMENT</div>
        <div class="fp-assignment">{safe(citizen['assigned_career'].upper())}</div>
        <div class="fp-sub">CCAA AUTHORIZED · STATUS: PERMANENT</div>
    </div>
</div>
""")
    metrics = [
        ("Productivity Fit", citizen["productivity_fit"], "#b095f2"),
        ("Social Alignment", citizen["social_alignment"], "#8c9fad"),
        ("Stability Index", citizen["stability_index"], "#c0d3e2"),
    ]
    gauges = ""
    for label, value, color in metrics:
        gauges += f"""
<div class="fp-gauge">
    <div class="fp-ring" style="background:conic-gradient({color} {value}%,#435565 {value}%);">
        <div class="fp-ring-inner">{value}%</div>
    </div>
    <div class="fp-gauge-title">{safe(label)}</div>
</div>"""
    render(f'<div class="fp-gauges">{gauges}</div>')
    render(f"""
<div class="fp-bottom">
    <div class="fp-tile">
        <div class="fp-eyebrow">ASSIGNMENT DAY / COMPLIANCE</div>
        <div class="fp-status">{safe(compliance)}</div>
        <div class="fp-sub">RESPONSE: {safe(decision or 'PENDING')} · OPEN ASSIGNMENT FOR DETAILS</div>
    </div>
    <div class="fp-tile">
        <div class="fp-eyebrow">RESTRICTED APPEAL STATUS</div>
        <div class="fp-status">{safe(appeal_status)}</div>
        <div class="fp-sub">{safe(appeal['appeal_id']) if appeal else 'ONE REVIEW PERMITTED · BELOW 5% APPROVAL'}</div>
    </div>
</div>
<div class="fp-banner">A STABLE SOCIETY IS BUILT ON ALIGNED FUTURES.</div>
""")
    with st.expander("MORE DETAILS · REPORTS, DOCUMENTS & STORY PROGRESS", expanded=False):
        display_narrative_progress(citizen)
        display_allocation_details(citizen)
        display_documents(citizen)


# ============================================================
# WIREFRAME-INSPIRED SIDEBAR — ICON NAVIGATION
# ============================================================

NAV_ITEMS = [
    ("Dashboard", "dashboard", "fp_nav_dashboard"),
    ("Profile", "person", "fp_nav_profile"),
    ("Evaluation", "fact_check", "fp_nav_evaluation"),
    ("Assignment", "work", "fp_nav_assignment"),
    ("Appeal", "gavel", "fp_nav_appeal"),
    ("Resources", "folder_open", "fp_nav_resources"),
]

if "navigation" not in st.session_state or st.session_state.navigation not in [item[0] for item in NAV_ITEMS]:
    st.session_state.navigation = "Dashboard"


LOGO_SVG = '<svg viewBox="0 0 120 100" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><g fill="currentColor"><path d="M27 5H92L80 23H15Z"/><path d="M17 31H48L36 49H5Z"/><path d="M52 40H72L34 96H14Z"/><path d="M96 8H118L59 96H37Z"/></g></svg>'


def navigate_to(destination):
    st.session_state.navigation = destination


with st.sidebar:
    dark_mode = st.session_state.visual_mode == "Dark"
    st.button("", icon=":material/dark_mode:" if dark_mode else ":material/light_mode:",
              key="fp_theme_toggle", on_click=toggle_visual_mode,
              help="Dark mode — switch to light mode" if dark_mode else "Light mode — switch to dark mode")
    render(f"""
<div class="fp-side-brand">
    <div class="fp-side-emblem" aria-hidden="true">
{LOGO_SVG}
    </div>
    <div>
        <div class="fp-side-logo">FUTURE<span>PATH</span></div>
        <div class="fp-side-tag">CENTRAL CAREER ALLOCATION AUTHORITY</div>
    </div>
</div>
<div class="fp-side-separator"></div>
<div class="fp-side-section">MAIN NAVIGATION <span>{[item[0] for item in NAV_ITEMS].index(st.session_state.navigation) + 1:02d} / 06</span></div>
""")

    for page_name, material_icon, widget_key in NAV_ITEMS:
        active = st.session_state.navigation == page_name
        st.button(
            page_name.upper(),
            key=widget_key,
            icon=f":material/{material_icon}:",
            type="primary" if active else "secondary",
            use_container_width=True,
            on_click=navigate_to,
            args=(page_name,),
        )

    render('<div class="fp-side-separator" style="margin-top:18px;"></div>')
    render('<div class="fp-side-section">CITIZEN ACCESS <span>2176-A</span></div>')

    if st.session_state.citizen is not None:
        sidebar_citizen = st.session_state.citizen
        render(f"""
<div class="fp-side-citizen">
    <div class="fp-side-avatar" aria-hidden="true">
        <svg viewBox="0 0 32 32"><circle cx="16" cy="11" r="6" fill="#b5c4d3"/>
        <path d="M4 30c0-10 24-10 24 0" fill="#b5c4d3"/></svg>
    </div>
    <div class="fp-side-person">
        <div class="fp-side-person-name">{safe(sidebar_citizen['name'])}</div>
        <div class="fp-side-person-id">{safe(sidebar_citizen['citizen_id'])}</div>
        <div class="fp-side-verified">● IDENTITY VERIFIED</div>
    </div>
</div>
""")
    else:
        render("""
<div class="fp-side-citizen fp-side-unregistered">
    <div class="fp-side-avatar" aria-hidden="true">+</div>
    <div class="fp-side-person">
        <div class="fp-side-person-name">NO CITIZEN RECORD</div>
        <div class="fp-side-person-id">REGISTRATION REQUIRED</div>
    </div>
</div>
""")

    render("""
<div class="fp-side-status"><span class="fp-online-dot"></span>
    <span>SYSTEM ONLINE</span><span class="fp-side-status-year">2176</span>
</div>
""")

    with st.expander("⚙  PRESENTATION CONTROLS", expanded=False):
        st.caption("DEMONSTRATION / EXPORT / RESET")
        st.button("LOAD AURORA DEMO", key="load_aurora_demo", on_click=load_demo, use_container_width=True)
        if st.session_state.citizen is not None:
            st.download_button(
                "EXPORT CITIZEN RECORD (JSON)",
                data=export_citizen_record(st.session_state.citizen),
                file_name="FUTUREPATH_Citizen_Record.json",
                mime="application/json",
                key="export_citizen_json",
                use_container_width=True,
            )
        with st.expander("RESET / START OVER"):
            st.caption("Clears this fictional citizen and archive discoveries.")
            confirm_reset = st.checkbox("I want to clear this session", key="confirm_reset")
            st.button("RESET EXPERIENCE", key="reset_experience", on_click=reset_experience,
                      disabled=not confirm_reset, use_container_width=True)
        if st.session_state.demo_mode:
            st.caption("DEMONSTRATION RECORD ACTIVE // FICTIONAL")

    if st.session_state.resistance_discovered or st.session_state.history_discovered:
        render('<div class="fp-side-anomaly">◈ ARCHIVE ANOMALY DETECTED</div>')

    render("""
<div class="fp-side-footer">
    <div>FUTUREPATH 2176 · CENTRAL CAREER ALLOCATION AUTHORITY</div>
    <div>AUTHORIZED CITIZEN ACCESS ONLY</div>
    <div class="fp-side-footer-quote">A STABLE SOCIETY IS BUILT ON ALIGNED FUTURES.</div>
    <div>FICTIONAL ACADEMIC DESIGN PROJECT · ALL ASSESSMENTS, DECISIONS AND POLICIES ARE SIMULATED.</div>
    <div>USE FICTIONAL CITIZEN INFORMATION ONLY.</div>
</div>
""")

selected_page = st.session_state.navigation

# ============================================================
# MAIN HEADER
# ============================================================

render(
    '<div class="gov-label">'
    'CENTRAL CAREER ALLOCATION AUTHORITY // 2176'
    '</div>'
)

render(f'<div class="fp-main-brand">{LOGO_SVG}<div><h1>FUTUREPATH</h1><div class="fp-year">2176 / ASSIGNED FUTURES</div></div></div>')
st.caption(
    "OFFICIAL CITIZEN PORTAL | ASSIGNED FUTURES PROGRAM"
)
st.divider()

# ============================================================
# DASHBOARD
# ============================================================

if selected_page == "Dashboard":
    st.header("CITIZEN DASHBOARD")
    st.caption("OFFICIAL CAREER ALLOCATION OVERVIEW // 2176")

    if st.session_state.citizen is None:
        render("""
<div class="fp-tile">
    <div class="fp-eyebrow">CITIZEN IDENTIFICATION</div>
    <div class="fp-assignment">NO VERIFIED RECORD FOUND</div>
    <div class="fp-sub">Begin your mandatory evaluation or load the fictional Aurora demonstration.</div>
</div>
""")
        st.info("Select Evaluation in the sidebar to register. For a quick demo, open Presentation Tools in the sidebar.")
    else:
        display_compact_dashboard(st.session_state.citizen)
        if st.session_state.resistance_discovered or st.session_state.history_discovered:
            st.caption("ARCHIVE ANOMALY DETECTED · Open Resources to investigate.")

# ============================================================
# PROFILE
# ============================================================

elif selected_page == "Profile":
    st.header("CITIZEN PROFILE")

    if st.session_state.citizen is None:
        st.warning(
            "No citizen profile available. "
            "Complete your evaluation first."
        )
    else:
        citizen = st.session_state.citizen

        # Keep the official identity card visible; all detailed records are optional.
        display_citizen_card(citizen)
        st.caption("PERSONNEL RECORD DIRECTORY // SELECT A SECTION TO EXPAND OR COLLAPSE")

        left, right = st.columns(2, gap="medium")

        with left:
            with st.expander(":material/route:  NARRATIVE PROGRESS", expanded=False):
                display_narrative_progress(citizen)

        with right:
            with st.expander(":material/id_card:  PERSONAL INFORMATION", expanded=False):
                st.write("**Citizen Name:**", citizen["name"])
                st.write("**Citizen ID:**", citizen["citizen_id"])
                st.write("**Age:**", citizen["age"])
                st.write("**Cohort:**", citizen["cohort"])
                st.write("**Verification:**", citizen["verification"])
                st.write("**Registration Date:**", citizen["registration_date"])

        with left:
            with st.expander(":material/work:  CAREER RECORD", expanded=False):
                st.write("**Preferred Career:**", citizen["preferred_career"])
                st.write("**Assigned Career:**", citizen["assigned_career"])
                st.write("**Assignment Status:**", citizen["assignment_status"])

        with right:
            with st.expander(":material/assignment:  EVALUATION RECORD", expanded=False):
                display_questionnaire(citizen)

        with left:
            with st.expander(":material/monitoring:  EVALUATION SUMMARY", expanded=False):
                display_gauges(citizen)

        with right:
            with st.expander(":material/verified_user:  COMPLIANCE RECORD", expanded=False):
                display_compliance(citizen)

        with left:
            with st.expander(":material/gavel:  APPEAL RECORD", expanded=False):
                if citizen.get("appeal") is None:
                    st.info("No appeal has been submitted.")
                else:
                    display_appeal_decision(citizen)

        with right:
            with st.expander(":material/download:  OFFICIAL DOCUMENTS", expanded=False):
                display_documents(citizen)

# ============================================================
# EVALUATION
# ============================================================

elif selected_page == "Evaluation":
    st.header("MANDATORY CITIZEN EVALUATION")

    st.caption("MANDATORY AT AGE 18 · STANDARDIZED CCAA ASSESSMENT PROTOCOL")

    st.caption(
        "CCAA STANDARDIZED ASSESSMENT PROTOCOL // 2176"
    )

    if st.session_state.citizen is not None:
        st.info(
            "Submitting another evaluation creates a new "
            "fictional citizen record and replaces the "
            "current record in this session."
        )

    with st.form("citizen_evaluation_form"):
        identity, preferences = st.columns(2, gap="medium")
        with identity:
            st.markdown("**01 / CITIZEN IDENTIFICATION**")
            name = st.text_input("Citizen name", placeholder="Enter a fictional name")
            age = st.number_input("Citizen age", min_value=1, max_value=100, value=18, step=1)
        with preferences:
            st.markdown("**02 / CAREER PREFERENCE**")
            career = st.selectbox("Preferred occupation", career_options)
            st.caption("Preferences are advisory, not binding.")

        skills_col, work_col = st.columns(2, gap="medium")
        with skills_col:
            st.markdown("**03 / SKILLS & EDUCATION**")
            skill = st.selectbox("Primary skill", skill_options)
            secondary_skill = st.selectbox("Secondary skill", [x for x in skill_options if x != skill])
            academic_subject = st.selectbox("Strongest academic subject", academic_subjects)
        with work_col:
            st.markdown("**04 / WORKPLACE PROFILE**")
            work_environment = st.selectbox("Preferred environment", work_environments)
            work_priority = st.selectbox("Top workplace priority", work_priorities)
            teamwork = st.selectbox("Team arrangement", teamwork_options)

        compliance_col, choice_col = st.columns(2, gap="medium")
        with compliance_col:
            st.markdown("**05 / INSTITUTIONAL ALIGNMENT**")
            compliance = st.selectbox("Response to official instructions", compliance_options)
        with choice_col:
            st.markdown("**06 / PERSONAL AUTONOMY**")
            individual_choice = st.selectbox("Views on career allocation", choice_options)

        st.caption("OFFICIAL NOTICE · All submitted answers enter the simulated CCAA allocation system.")
        submitted = st.form_submit_button("SUBMIT FOR GOVERNMENT EVALUATION", type="primary", use_container_width=True)

    if submitted:
        if not name.strip():
            st.error("CITIZEN IDENTIFICATION REQUIRED")

        elif age < 18:
            st.error("EVALUATION ACCESS DENIED")
            st.warning(
                "Citizen has not reached the mandatory "
                "career allocation age of 18."
            )

        else:
            responses = {
                "skill": skill,
                "secondary_skill": secondary_skill,
                "academic_subject": academic_subject,
                "work_environment": work_environment,
                "work_priority": work_priority,
                "teamwork": teamwork,
                "compliance": compliance,
                "individual_choice": individual_choice
            }

            allocation = allocate_career(responses)
            indices = calculate_indices(responses, allocation)

            st.session_state.citizen = {
                "name": name.strip(),
                "age": int(age),
                "citizen_id": generate_id("FP-2176-"),
                "cohort": "2176-A",
                "verification": "VERIFIED",
                "registration_date": timestamp(),
                "preferred_career": career,
                **responses,
                "assigned_career": allocation["assigned_career"],
                "assignment_status": "PERMANENT",
                "allocation_score": allocation["allocation_score"],
                "score_breakdown": allocation["score_breakdown"],
                "career_rankings": allocation["career_rankings"],
                **indices,
                "appeal": None,
                "assignment_decision": None,
                "compliance_status": "AWAITING RESPONSE",
                "government_response": None,
                "compliance_notice": None,
                "decision_timestamp": None,
                "decision_reference": None
            }

            citizen = st.session_state.citizen

            st.success("GOVERNMENT EVALUATION COMPLETE // CITIZEN RECORD VERIFIED")
            render(f"""
<div class="gov-highlight">
    <div class="gov-label">OFFICIAL ALLOCATION RESULT // {safe(citizen['citizen_id'])}</div>
    <div class="gov-small">{safe(citizen['name'].upper())} · PREFERRED: {safe(citizen['preferred_career'])}</div>
    <div class="gov-label" style="margin-top:17px;">YOUR PERMANENT ASSIGNMENT</div>
    <div class="gov-value">{safe(citizen['assigned_career'].upper())}</div>
    <div class="gov-small">A government-issued career designation has been recorded.</div>
</div>
""")
            if citizen["assigned_career"] != citizen["preferred_career"]:
                st.warning("CITIZEN PREFERENCE OVERRIDDEN // Government labor priorities take precedence.")
            st.caption("Your detailed evaluation, scores, and documents are available in Profile.")
            st.markdown("**SELECT YOUR NEXT ACTION**")
            go_profile, go_dashboard, go_assignment = st.columns(3)
            with go_profile:
                st.button("VIEW PROFILE", icon=":material/id_card:", key="evaluation_go_profile",
                          on_click=navigate_to, args=("Profile",), use_container_width=True)
            with go_dashboard:
                st.button("GO TO DASHBOARD", icon=":material/dashboard:", key="evaluation_go_dashboard",
                          on_click=navigate_to, args=("Dashboard",), use_container_width=True)
            with go_assignment:
                st.button("PROCEED TO ASSIGNMENT", icon=":material/assignment:", key="evaluation_go_assignment",
                          on_click=navigate_to, args=("Assignment",), use_container_width=True)

# ============================================================
# ASSIGNMENT — STEP 10
# ============================================================

elif selected_page == "Assignment":
    st.header("OFFICIAL CAREER ASSIGNMENT")

    if st.session_state.citizen is None:
        st.warning("No career assignment has been issued.")

    else:
        citizen = st.session_state.citizen

        st.caption("NATIONAL ASSIGNMENT DAY // OFFICIAL CITIZEN RESPONSE")
        display_assignment_day(citizen)

        # Assignment Day is for a decision, not another evaluation report.
        # The existing acceptance/refusal form and compliance result remain intact.
        if citizen.get("assignment_decision") is not None:
            st.markdown("**CONTINUE YOUR CITIZEN JOURNEY**")
            go_profile, go_appeal = st.columns(2)
            with go_profile:
                st.button("VIEW CITIZEN PROFILE", icon=":material/id_card:",
                          key="assignment_go_profile", on_click=navigate_to,
                          args=("Profile",), use_container_width=True)
            with go_appeal:
                st.button("REQUEST RESTRICTED APPEAL", icon=":material/gavel:",
                          key="assignment_go_appeal", on_click=navigate_to,
                          args=("Appeal",), use_container_width=True)
        else:
            st.caption("Detailed allocation scores, appeal records, and downloadable documents are available on their respective pages.")

# ============================================================
# APPEAL
# ============================================================

elif selected_page == "Appeal":
    st.header("CAREER ASSIGNMENT APPEAL")

    st.caption(
        "CCAA RESTRICTED RE-EVALUATION PROTOCOL // 2176"
    )

    if st.session_state.citizen is None:
        st.warning(
            "No verified citizen assignment found. "
            "Complete your evaluation first."
        )

    else:
        citizen = st.session_state.citizen

        display_citizen_card(citizen)
        display_assignment(citizen)

        st.caption(
            "Assignment Day acceptance or refusal "
            "does not remove the right to submit "
            "one restricted appeal."
        )

        if citizen.get("appeal") is not None:
            display_appeal_decision(citizen)

            st.error(
                "APPEAL PRIVILEGES EXHAUSTED. "
                "No additional submissions permitted."
            )

            st.divider()
            display_documents(citizen)

        else:
            st.warning(
                "RESTRICTED ACCESS: Appeals are reviewed "
                "only under exceptional circumstances."
            )

            st.info(
                "Official fictional CCAA communications "
                "claim an approval rate below 5%."
            )

            st.subheader("OFFICIAL APPEAL APPLICATION")

            with st.form("appeal_application_form"):
                st.markdown(
                    "**SECTION A — REASON FOR APPEAL**"
                )

                appeal_reason = st.selectbox(
                    "Select the Primary Reason for Your Appeal",
                    appeal_reasons
                )

                st.divider()
                st.markdown(
                    "**SECTION B — CITIZEN STATEMENT**"
                )

                explanation = st.text_area(
                    "Explain Why You Are Requesting Reassignment",
                    placeholder="Provide your explanation...",
                    height=170,
                    max_chars=1500
                )

                st.caption(
                    "Minimum 50 characters. "
                    "Use fictional information only."
                )

                st.divider()
                st.markdown(
                    "**SECTION C — MANDATORY DECLARATION**"
                )

                acknowledge = st.checkbox(
                    "I acknowledge that government labor "
                    "priorities take precedence over personal "
                    "career preferences and that this appeal "
                    "does not suspend my assigned duties."
                )

                st.warning(
                    "Only one appeal is permitted "
                    "per citizen record."
                )

                submit_appeal = st.form_submit_button(
                    "SUBMIT OFFICIAL APPEAL"
                )

            if submit_appeal:
                if len(explanation.strip()) < 50:
                    st.error(
                        "APPEAL INCOMPLETE: "
                        "At least 50 characters required."
                    )

                elif not acknowledge:
                    st.error("DECLARATION REQUIRED.")

                else:
                    st.session_state.citizen["appeal"] = (
                        review_appeal(
                            citizen,
                            appeal_reason,
                            explanation.strip()
                        )
                    )
                    st.rerun()

# ============================================================
# RESOURCES — STEP 9 + STEP 10
# ============================================================

elif selected_page == "Resources":
    st.header("CITIZEN RESOURCES")

    st.caption(
        "MINISTRY OF SOCIAL STABILITY // "
        "PUBLIC INFORMATION AND POLICY ARCHIVE"
    )

    resource_tab = st.radio(
        "RESOURCE DIRECTORY",
        [
            "Government Policies",
            "Public Announcements",
            "Restricted Archive",
            "Historical Timeline",
            "Aurora's Story",
            "Citizen Information Channel",
            "Presentation Guide"
        ],
        horizontal=True,
        key="resource_tab"
    )

    st.divider()

    if resource_tab == "Government Policies":
        display_policy_archive()

    elif resource_tab == "Public Announcements":
        display_propaganda()

    elif resource_tab == "Restricted Archive":
        display_classified_archive()

    elif resource_tab == "Historical Timeline":
        display_historical_timeline()

    elif resource_tab == "Aurora's Story":
        display_aurora_story()

    elif resource_tab == "Presentation Guide":
        display_presentation_guide()

    elif resource_tab == "Citizen Information Channel":
        display_resistance()
        st.divider()
        st.subheader("SECONDARY ARCHIVE RECOVERY")
        st.caption("Recovery key hint: what must a society do with its history? REMEMBER.")
        history_key = st.text_input("Historical Recovery Key", key="history_recovery_key")
        if st.button("RECOVER SUPPRESSED HISTORY", key="recover_history_button"):
            if history_key.strip().upper() == "REMEMBER":
                st.session_state.history_discovered = True
                st.rerun()
            else:
                st.error("HISTORICAL ARCHIVE FRAGMENT NOT FOUND")
        if st.session_state.history_discovered:
            st.success("SUPPRESSED HISTORY RECOVERED. Return to Historical Timeline.")
        display_final_reveal()

# ============================================================
# END OF FUTUREPATH 2176 — GLOBAL FOOTER MOVED TO SIDEBAR
# ============================================================
