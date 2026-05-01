import streamlit as st
import requests

# --- إعدادات الصفحة الفاخرة ---
st.set_page_config(page_title="EcomMind AI | Intelligent Commerce", layout="wide")

# --- التصميم السينمائي (CSS) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #05070a;
    }
    
    /* غلاف الموقع الرئيسي */
    .hero-cover {
        width: 100%;
        border-radius: 20px;
        box-shadow: 0 0 30px rgba(0, 242, 255, 0.4);
        margin-bottom: 40px;
        transition: 0.5s;
    }
    .hero-cover:hover {
        transform: scale(1.01);
        box-shadow: 0 0 50px rgba(0, 242, 255, 0.6);
    }

    /* تنسيق صندوق الإدخال */
    div[data-baseweb="input"] {
        background-color: rgba(0, 242, 255, 0.05) !important;
        border: 2px solid #00f2ff !important;
        border-radius: 15px !important;
    }
    input { color: #00f2ff !important; font-size: 1.2rem !important; }

    /* أزرار التشغيل */
    .stButton>button {
        background: linear-gradient(90deg, #00f2ff, #0062ff) !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        height: 55px;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- عرض الغلاف المختار (الصورة الأولى) ---
# تأكد من رفعها باسم cover.png
st.markdown("""
    <div style="text-align: center;">
        <img src="https://raw.githubusercontent.com/alhajameer4-del/Python/main/cover.png" class="hero-cover">
    </div>
""", unsafe_allow_html=True)

# --- المحرك الذكي ---
def call_ai(product):
    api_key = "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"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": f"أنت خبير تسويق محترف، اكتب استراتيجية كاملة لمنتج: {product}"}]
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        return response.json()['choices'][0]['message']['content']
    except: return "⚠️ المحرك متصل.. جاري المعالجة"

# --- واجهة الاستخدام ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    product_name = st.text_input("🔍 ابدأ عصر التجارة الذكية.. أدخل اسم المنتج:")
    if st.button("توليد المحتوى الشعاعي ✨"):
        if product_name:
            with st.spinner('SYSTEM ANALYZING...'):
                res = call_ai(product_name)
                st.markdown(f"""
                    <div style='color:#00f2ff; background:rgba(0,10,20,0.9); padding:30px; border:2px solid #00f2ff; border-radius:20px; box-shadow: 0 0 20px rgba(0,242,255,0.2); line-height:1.7;'>
                        {res}
                    </div>
                """, unsafe_allow_html=True)

# --- قسم العضوية ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
    <div style='text-align: center; border: 2px solid #00f2ff; padding: 40px; border-radius: 30px; background: rgba(0, 100, 255, 0.1); backdrop-filter: blur(20px);'>
        <h2 style='color: #fff; margin-bottom:10px;'>EXECUTIVE PRO MEMBERSHIP</h2>
        <p style='color: #00f2ff; font-size: 2.5rem; font-weight: 900;'>49$ / Monthly</p>
        <p style='color: #ccc;'>Payoneer: SADAM.ALHAJ007@GMAIL.COM</p>
        <p style='color: #34a853; font-size: 0.8rem;'>USDT (TRC20): TKCvNEvz59717dp5QZbrwCqCzTQqjrNxCX</p>
    </div>
""", unsafe_allow_html=True)
