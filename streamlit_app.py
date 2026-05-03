import streamlit as st
import requests

# --- 1. إعدادات الصفحة الفنية ---
st.set_page_config(page_title="EcomMind AI Pro", layout="wide", initial_sidebar_state="collapsed")

# --- 2. الهندسة البصرية المتقدمة (إجبار السواد والزجاج) ---
st.markdown("""
    <style>
    /* إخفاء القوائم */
    header, footer, #MainMenu {visibility: hidden;}

    /* 3. إجبار الخلفية على السواد ثم تحميل صورتك */
    [data-testid="stAppViewContainer"] {
        background: #000000 !important;
        background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.7)), 
                          url("https://raw.githubusercontent.com/alhajameer4-del/Python/main/background.jpg") !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
    }

    /* 4. تحويل النوافذ إلى زجاج نقي شفاف (Glassmorphism) */
    .glass-card {
        background: rgba(0, 0, 0, 0.65) !important;
        backdrop-filter: blur(15px) !important;
        -webkit-backdrop-filter: blur(15px) !important;
        border: 1px solid rgba(0, 242, 255, 0.3) !important;
        border-radius: 30px !important;
        padding: 40px !important;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.8) !important;
        margin-bottom: 25px;
    }

    /* 5. اسم المنتج المتوهج */
    .neon-title {
        color: #00f2ff !important;
        text-align: center;
        font-size: 4rem !important;
        font-weight: 900 !important;
        text-shadow: 0 0 20px #00f2ff, 0 0 40px #0062ff !important;
        margin-top: 10px;
        letter-spacing: 5px;
    }

    /* 6. خانة البحث البيضوية (سواد ليزري) */
    div[data-baseweb="input"] {
        background-color: rgba(0, 0, 0, 0.9) !important;
        border: 2px solid #00f2ff !important;
        border-radius: 50px !important;
        box-shadow: 0 0 25px #00f2ff !important;
        height: 75px !important;
    }
    input {
        color: #00f2ff !important;
        background-color: transparent !important;
        -webkit-text-fill-color: #00f2ff !important;
        font-size: 1.5rem !important;
        font-weight: bold !important;
        text-align: center !important;
    }

    /* 7. الأزرار النيونية */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #00f2ff, #0062ff) !important;
        color: #000 !important;
        font-weight: 900 !important;
        border-radius: 50px !important;
        height: 60px;
        border: none !important;
        box-shadow: 0 0 25px #00f2ff !important;
        font-size: 1.3rem;
        transition: 0.4s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 50px #00f2ff !important; }

    /* 8. زر الدفع الزجاجي */
    .checkout-btn {
        background: rgba(0, 242, 255, 0.2) !important;
        border: 2px solid #00f2ff !important;
        color: #fff !important;
        padding: 20px 60px !important;
        border-radius: 50px !important;
        font-weight: 900 !important;
        text-decoration: none !important;
        display: inline-block !important;
        box-shadow: 0 0 30px #00f2ff !important;
        font-size: 1.5rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- المحرك البرمجي ---
def run_ai(query):
    api_key = "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"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": f"اكتب وصف بيعي احترافي لمنتج: {query}"}]
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        return response.json()['choices'][0]['message']['content']
    except: return "⚠️ النظام متصل.. جاري المعالجة الشعاعية"

# --- الواجهة الرئيسية ---

# عرض الشعار مع رابط GitHub المباشر
st.markdown(f'<div style="text-align:center;"><img src="https://raw.githubusercontent.com/alhajameer4-del/Python/main/logo.png" style="width:230px; filter:drop-shadow(0 0 20px #00f2ff);"></div>', unsafe_allow_html=True)

# اسم المنتج
st.markdown('<h1 class="neon-title">EcomMind AI</h1>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2.5, 1])
with col2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    p_name = st.text_input("", placeholder="ما هو المنتج الذي تريد تسويقه بذكاء؟")
    if st.button("إطلاق الذكاء الشعاعي ✨"):
        if p_name:
            with st.spinner('SYSTEM ANALYZING...'):
                result = run_ai(p_name)
                st.markdown(f"<div style='color:#00f2ff; background:rgba(0,0,0,0.85); padding:25px; border:2px solid #00f2ff; border-radius:20px; box-shadow:0 0 20px #00f2ff;'>{result}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# نافذة الاشتراك الزجاجية
st.markdown("<br><br>", unsafe_allow_html=True)
with col2:
    st.markdown(f"""
        <div class='glass-card' style='text-align:center;'>
            <h1 style='color:#fff; text-shadow: 0 0 10px #00f2ff;'>EXECUTIVE PRO</h1>
            <p style='font-size:3.5rem; font-weight:900; color:#00f2ff; margin:0;'>49$</p>
            <p style='color:#888; margin-bottom: 30px;'>وصول كامل لأقوى محركات الذكاء الاصطناعي</p>
            <a href="mailto:SADAM.ALHAJ007@GMAIL.COM?subject=PRO" class="checkout-btn">تفعيل العضوية الآن 💎</a>
        </div>
    """, unsafe_allow_html=True)
