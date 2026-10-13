import streamlit as st
import requests

API = "http://localhost:8000"

st.set_page_config(
    page_title="Wathiqa — Saudi Document Intelligence",
    page_icon="🇸🇦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Theme toggle ----------
if "theme" not in st.session_state:
    st.session_state.theme = "light"

with st.sidebar:
    st.markdown("### 🇸🇦 Wathiqa")
    st.caption("Saudi Document Intelligence")
    st.markdown("---")
    theme_choice = st.radio(
        "Appearance",
        ["☀️ Warm", "🌙 Dark"],
        index=0 if st.session_state.theme == "light" else 1,
        horizontal=True,
    )
    st.session_state.theme = "light" if "Warm" in theme_choice else "dark"
    st.markdown("---")
    st.markdown("**Pipeline**")
    st.markdown("- Extract text")
    st.markdown("- Detect Arabic / English")
    st.markdown("- Mask PII (PDPL)")
    st.markdown("- Hybrid RAG retrieval")
    st.markdown("- LLM answer (Groq)")
    st.markdown("---")
    st.caption("Built by Shafeer Said Alavi")

dark = st.session_state.theme == "dark"

# ---------- Colors ----------
if dark:
    bg = "#14110c"          # warm near-black (deep espresso)
    card_bg = "#1c1812"     # warm dark card
    text = "#ece4d3"        # warm cream text
    subtext = "#a89a7c"     # muted warm gold-gray
    border = "#2e2718"      # warm dark border
    accent = "#0a7d47"      # brighter Saudi green for dark
    accent_dark = "#064a2a"
    gold = "#c9a44c"        # warm gold
    pattern_opacity = "0.05"
    pattern_stroke = "%23c9a44c"   # gold pattern stroke (URL-encoded #)
else:
    bg = "#faf6ee"
    card_bg = "#fffdf8"
    text = "#2b2416"
    subtext = "#7a6a4f"
    border = "#e8dfc9"
    accent = "#0a5c36"
    accent_dark = "#064a2a"
    gold = "#b8860b"
    pattern_opacity = "0.06"
    pattern_stroke = "%230a5c36"   # green pattern stroke



st.markdown(f"""
<style>
    @keyframes heroShimmer {{
        0%   {{ background-position: 0% 50%; }}
        50%  {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}
    @keyframes floatUp {{
        0%   {{ transform: translateY(0px); opacity: 0.9; }}
        50%  {{ transform: translateY(-6px); opacity: 1; }}
        100% {{ transform: translateY(0px); opacity: 0.9; }}
    }}
    @keyframes glowPulse {{
        0%   {{ box-shadow: 0 0 0 0 rgba(184,134,11,0.4); }}
        70%  {{ box-shadow: 0 0 0 12px rgba(184,134,11,0); }}
        100% {{ box-shadow: 0 0 0 0 rgba(184,134,11,0); }}
    }}

    .stApp {{
    background-color: {bg};
    background-image:
        url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='120' height='120' viewBox='0 0 120 120'><g fill='none' stroke='{pattern_stroke}' stroke-width='1' opacity='{pattern_opacity}'><path d='M60 10 L75 35 L105 35 L85 55 L95 85 L60 70 L25 85 L35 55 L15 35 L45 35 Z'/><circle cx='60' cy='60' r='48'/><circle cx='60' cy='60' r='30'/></g></svg>");
    background-attachment: fixed;
    color: {text};
    }}
    h1, h2, h3, h4, h5, h6, p, span, div, label {{ color: {text}; }}
    section[data-testid="stSidebar"] {{ background: {card_bg}; }}
    section[data-testid="stSidebar"] * {{ color: {text} !important; }}

    .hero {{
        position: relative;
        background: linear-gradient(120deg,
            {accent} 0%, {accent_dark} 25%, {gold} 50%,
            {accent_dark} 75%, {accent} 100%);
        background-size: 300% 300%;
        animation: heroShimmer 14s ease-in-out infinite;
        color: #ffffff;
        padding: 2.2rem 2.4rem;
        border-radius: 20px;
        box-shadow: 0 14px 40px rgba(10,92,54,0.28), inset 0 0 0 1px rgba(255,255,255,0.15);
        margin-bottom: 1.4rem;
        overflow: hidden;
    }}
    .hero::after {{
        content: "";
        position: absolute;
        right: -50px; top: -50px;
        width: 200px; height: 200px;
        background: radial-gradient(circle, rgba(255,255,255,0.15), transparent 70%);
        pointer-events: none;
        animation: floatUp 6s ease-in-out infinite;
    }}
    .hero h1 {{
        color: #ffffff; margin: 0; font-size: 2.05rem;
        letter-spacing: -0.4px;
        display: flex; align-items: center; gap: 0.9rem;
        position: relative; z-index: 2;
    }}
    .hero p  {{ color: #f7f1e3; margin: 0.55rem 0 0 0; font-size: 1.02rem; position: relative; z-index: 2; }}
    .hero .flag-img {{
        display: inline-block;
        border-radius: 5px;
        box-shadow: 0 3px 12px rgba(0,0,0,0.4);
        background: #fff;
        flex-shrink: 0;
    }}
    .badge {{
        display: inline-block;
        background: rgba(255,255,255,0.16);
        color: #fff8e7;
        padding: 0.32rem 0.9rem;
        border-radius: 999px;
        font-size: 0.78rem;
        margin-right: 0.5rem;
        margin-top: 1rem;
        border: 1px solid rgba(255,255,255,0.28);
        backdrop-filter: blur(4px);
        position: relative; z-index: 2;
    }}

    .stat-card {{
        background: {card_bg};
        padding: 1.15rem 1.35rem;
        border-radius: 14px;
        border-left: 4px solid {gold};
        box-shadow: 0 3px 18px rgba(184,134,11,0.10);
        transition: transform 0.25s ease, box-shadow 0.25s ease;
    }}
    .stat-card:hover {{
        transform: translateY(-3px);
        box-shadow: 0 8px 26px rgba(184,134,11,0.20);
    }}
    .stat-card h3 {{ margin: 0; color: {accent}; font-size: 1.55rem; font-weight: 700; }}
    .stat-card p  {{ margin: 0.2rem 0 0 0; color: {subtext}; font-size: 0.85rem; }}

    .answer-card {{
        background: {card_bg};
        padding: 1.7rem 1.9rem;
        border-radius: 16px;
        border-left: 5px solid {gold};
        box-shadow: 0 6px 28px rgba(184,134,11,0.12);
        color: {text};
        font-size: 1.06rem;
        line-height: 1.7;
    }}
    .answer-card h3 {{ color: {accent}; margin-top: 0; letter-spacing: 0.2px; }}

    .doc-row {{
        background: {card_bg};
        padding: 0.95rem 1.15rem;
        border-radius: 11px;
        border-left: 3px solid {gold};
        margin-bottom: 0.55rem;
        color: {text};
        border: 1px solid {border};
        transition: transform 0.2s ease;
    }}
    .doc-row:hover {{ transform: translateX(3px); }}
    .doc-row small {{ color: {subtext}; }}

    .stButton>button {{
        background: linear-gradient(135deg, {accent} 0%, {accent_dark} 100%) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        border: 1px solid {gold} !important;
        padding: 0.55rem 1.55rem !important;
        font-weight: 600 !important;
        transition: all 0.25s ease;
        animation: glowPulse 3s ease-in-out infinite;
    }}
    .stButton>button:hover {{
        background: linear-gradient(135deg, {gold} 0%, {accent} 100%) !important;
        transform: translateY(-1px);
    }}
    .stTabs [data-baseweb="tab"] {{ color: {text}; font-weight: 500; }}
    .stTabs [aria-selected="true"] {{ color: {accent} !important; }}
</style>
""", unsafe_allow_html=True)

# ---------- Hero ----------
st.markdown("""
<div class="hero">
    <h1>
        <img class="flag-img" src="https://flagcdn.com/w80/sa.png" width="54" height="36" alt="Saudi Arabia" />
        Wathiqa — Saudi Document Intelligence
    </h1>
    <p>Bilingual Arabic / English document Q&amp;A with automatic PII masking (PDPL-aligned).</p>
    <span class="badge">Hybrid RAG</span>
    <span class="badge">ChromaDB + BM25 + RRF</span>
    <span class="badge">Cross-Encoder Rerank</span>
    <span class="badge">Saudi ID / IBAN Masking</span>
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📤  Upload", "💬  Ask Wathiqa", "📚  Library"])

# ---------- Upload ----------
with tab1:
    f = st.file_uploader("Upload a PDF (Arabic or English)", type=["pdf"])
    if f and st.button("Process Document"):
        with st.spinner("Extracting, masking PII, and indexing…"):
            files = {"file": (f.name, f.getvalue(), "application/pdf")}
            r = requests.post(f"{API}/documents/upload", files=files)
            if r.ok:
                d = r.json()
                st.success(f"Indexed: {d['filename']}")
                pii_total = sum(len(v) for v in d["pii_found"].values())
                c1, c2, c3 = st.columns(3)
                c1.markdown(f"<div class='stat-card'><h3>{d['language'].upper()}</h3><p>Detected language</p></div>", unsafe_allow_html=True)
                c2.markdown(f"<div class='stat-card'><h3>{d['doc_type'].title()}</h3><p>Document type</p></div>", unsafe_allow_html=True)
                c3.markdown(f"<div class='stat-card'><h3>{pii_total}</h3><p>PII items masked</p></div>", unsafe_allow_html=True)
                if pii_total:
                    st.warning("Personal data detected and masked before indexing:")
                    st.json(d["pii_found"])
            else:
                st.error(r.text)

# ---------- Ask ----------
with tab2:
    q = st.text_input("Ask a question about your documents")
    if st.button("Ask Wathiqa") and q:
        with st.spinner("Retrieving and reasoning…"):
            r = requests.post(f"{API}/query/ask", json={"question": q})
            if r.ok:
                d = r.json()
                st.markdown(
                    f"<div class='answer-card'><h3>Answer</h3>{d['answer']}</div>",
                    unsafe_allow_html=True,
                )
            else:
                st.error(r.text)

# ---------- Library ----------
with tab3:
    r = requests.get(f"{API}/documents/")
    if r.ok:
        docs = r.json()
        if not docs:
            st.info("No documents yet. Upload one from the first tab.")
        for d in docs:
            st.markdown(
                f"<div class='doc-row'><b>{d['filename']}</b><br>"
                f"<small>🌐 {d['language']} · 📄 {d['doc_type']} · 🔒 PII: {d['pii_count']}</small></div>",
                unsafe_allow_html=True,
            )