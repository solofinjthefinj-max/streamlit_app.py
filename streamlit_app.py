import streamlit as st
import requests

# --- إعدادات الصفحة ---
st.set_page_config(page_title="EcomMind AI Pro", layout="wide", initial_sidebar_state="collapsed")

# --- الهندسة البصرية (دمج صورتك كخلفية للموقع) ---
st.markdown(f"""
    <style>
    /* 1. إخفاء العناصر الافتراضية */
    header, footer, #MainMenu {{visibility: hidden;}}

    /* 2. جعل صورتك هي الخلفية الكاملة للموقع */
    .stApp {{
        background: url("https://raw.githubusercontent.com/alhajameer4-del/Python/main/background.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* 3. تأثير الزجاج الشفاف للنوافذ لكي تظهر الخلفية من خلفها */
    .glass-card {{
        background: rgba(0, 0, 0, 0.6) !important;
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(0, 242, 255, 0.3);
        border-radius: 30px;
        padding: 35px;
        margin-bottom: 20px;
    }}

    /* 4. اسم المنتج النيوني */
    .neon-title {{
        color: #00f2ff;
        text-align: center;
        font-family: 'Orbitron', sans-serif;
        font-size: 3.5rem !important;
        font-weight: 900;
        text-shadow: 0 0 15px #00f2ff, 0 0 30px #0062ff;
        letter-spacing: 5px;
    }}

    /* 5. خانة البحث البيضوية (سوداء شفافة بحدود نيون) */
    div[data-baseweb="input"] {{
        background-color: rgba(0, 0, 0, 0.8) !important;
        border: 2px solid #00f2ff !important;
        border-radius: 50px !important;
        box-shadow: 0 0 20px #00f2ff !important;
        height: 70px !important;
    }}
    input {{
        color: #00f2ff !important;
        background-color: transparent !important;
        -webkit-text-fill-color: #00f2ff !important;
        font-size: 1.5rem !important;
        font-weight: bold !important;
        text-align: center !important;
    }}

    /* 6. زر التوليد */
    .stButton>button {{
        width: 100%;
        background: linear-gradient(90deg, #00f2ff, #0062ff) !important;
        color: #000 !important;
        font-weight: 900 !important;
        border-radius: 50px !important;
        height: 60px;
        border: none !important;
        box-shadow: 0 0 20px #00f2ff !important;
        font-size: 1.3rem;
    }}

    /* 7. زر الدفع الزجاجي */
    .checkout-btn {{
        background: rgba(0, 242, 255, 0.2);
        border: 2px solid #00f2ff;
        color: #fff !important;
        padding: 15px 40px;
        border-radius: 50px;
        font-weight: bold;
        text-decoration: none;
        display: inline-block;
        box-shadow: 0 0 20px #00f2ff;
    }}
    </style>
""", unsafe_allow_html=True)

# --- المحرك البرمجي ---
def run_ai(query):
    api_key = "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"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": f"اكتب وصف بيعي لمنتج: {query}"}]
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        return response.json()['choices'][0]['message']['content']
    except: return "⚠️ النظام متصل.. جاري المعالجة النيونية"

# --- الواجهة ---
# الشعار
st.markdown(f'<div style="text-align:center;"><img src="https://raw.githubusercontent.com/alhajameer4-del/Python/main/logo.png" style="width:200px; filter:drop-shadow(0 0 20px #00f2ff);"></div>', unsafe_allow_html=True)

# اسم المنتج
st.markdown('<h1 class="neon-title">EcomMind AI</h1>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    p_name = st.text_input("", placeholder="ما هو منتجك القادم؟")
    if st.button("توليد الإبداع الذكي ✨"):
        if p_name:
            with st.spinner('ANALYZING...'):
                result = run_ai(p_name)
                st.markdown(f"<div style='color:#00f2ff; padding:20px; border-top:1px solid #00f2ff; margin-top:20px;'>{result}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# نافذة الاشتراك
st.markdown("<br>", unsafe_allow_html=True)
with col2:
    st.markdown(f"""
        <div class='glass-card' style='text-align:center;'>
            <h2 style='color:#fff;'>EXECUTIVE PRO</h2>
            <p style='font-size:3rem; font-weight:900; color:#00f2ff; margin:0;'>49$</p>
            <a href="mailto:SADAM.ALHAJ007@GMAIL.COM" class="checkout-btn">تفعيل العضوية الآن 💎</a>
        </div>
    """, unsafe_allow_html=True)
