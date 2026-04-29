import streamlit as st
import requests

# --- إعدادات الصفحة ---
st.set_page_config(page_title="EcomMind AI Ultra Pro", layout="wide")

# --- التصميم المتكامل (CSS) ---
st.markdown("""
    <style>
    /* 1. الخلفية التقنية (أيقونات ذكاء اصطناعي ورموز إلكترونية) */
    .stApp {
        background: linear-gradient(rgba(5, 7, 10, 0.8), rgba(5, 7, 10, 0.9)), 
        url('https://www.transparenttextures.com/patterns/carbon-fibre.png'),
        url('https://img.freepik.com/free-vector/artificial-intelligence-icon-set_53876-115911.jpg?t=st=1715424564~exp=1715428164~hmac=02e605d83637e199d6515f4e0c8b6b0b5e5e6e6e6e6e6e6e6e6e6e6e6e6e6e');
        background-blend-mode: overlay;
        background-color: #05070a;
        background-size: cover;
        background-attachment: fixed;
    }

    /* 2. العنوان النيوني الصارخ */
    .neon-title {
        color: #00f2ff;
        text-align: center;
        font-size: 4rem !important;
        font-weight: 900;
        text-shadow: 0 0 20px #00f2ff, 0 0 40px #0062ff;
        font-family: 'Courier New', Courier, monospace;
    }

    /* 3. الحل الجذري والنهائي لخانة الكتابة (تحويلها لأسود نيوني) */
    .stTextInput > div > div {
        background-color: rgba(0, 5, 10, 0.9) !important;
        border: 2px solid #00f2ff !important;
        border-radius: 15px !important;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.4) !important;
    }
    .stTextInput input {
        color: #00f2ff !important;
        background-color: transparent !important;
        font-size: 1.3rem !important;
        font-weight: bold !important;
        padding: 15px !important;
    }
    
    /* إخفاء أي خلفية بيضاء تظهر عند النقر */
    .stTextInput input:focus {
        background-color: rgba(0, 242, 255, 0.1) !important;
        outline: none !important;
    }

    /* 4. نافذة الاشتراك (كريستال زجاجي مشع) */
    .premium-card {
        background: rgba(0, 100, 255, 0.1);
        backdrop-filter: blur(30px);
        border: 3px solid #00f2ff;
        border-radius: 40px;
        padding: 50px;
        text-align: center;
        box-shadow: 0 0 60px rgba(0, 242, 255, 0.3);
        margin-top: 40px;
    }

    /* 5. زر تفعيل العضوية (الجوهرة الزرقاء الحادة) */
    .glass-active-btn {
        background: linear-gradient(135deg, #00f2ff 0%, #0062ff 100%);
        border: 2px solid #fff;
        color: #fff !important;
        padding: 22px 60px;
        border-radius: 20px;
        font-weight: 900;
        font-size: 1.6rem;
        text-decoration: none;
        display: inline-block;
        box-shadow: 0 0 40px #00f2ff;
        transition: 0.4s;
    }
    .glass-active-btn:hover {
        transform: scale(1.1);
        box-shadow: 0 0 80px #00f2ff;
        filter: brightness(1.2);
    }

    /* أزرار التشغيل */
    .stButton > button {
        background-color: #00f2ff !important;
        color: #000 !important;
        font-weight: 900 !important;
        border-radius: 12px !important;
        height: 60px;
        box-shadow: 0 0 20px #00f2ff;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# محرك الذكاء الاصطناعي (Groq)
def call_ai(product):
    api_key = "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"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": f"أنت خبير تسويق، اكتب استراتيجية كاملة لمنتج: {product}"}]
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        return response.json()['choices'][0]['message']['content']
    except:
        return "⚠️ النظام متصل.. جاري المعالجة"

# واجهة التطبيق الرئيسية
st.markdown("<h1 class='neon-title'>ECOMMIND AI PRO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #00f2ff; font-weight: bold; letter-spacing: 4px;'>NEURAL COMMERCE ENGINE</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<div style='margin-top: 40px;'>", unsafe_allow_html=True)
    # الخانة الآن مجبرة على اللون الداكن
    product_name = st.text_input("📦 ما هو المنتج الذي تريد تسويقه بذكاء؟", key="product_input")
    if st.button("إطلاق الذكاء الشعاعي ✨"):
        if product_name:
            with st.spinner('SYSTEM ANALYZING...'):
                result = call_ai(product_name)
                st.markdown(f"<div style='color:#00f2ff; background:rgba(0,0,0,0.8); padding:30px; border:2px solid #00f2ff; border-radius:20px; text-shadow: 0 0 5px #00f2ff;'>{result}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# قسم الاشتراك الفاخر
st.markdown("<br><br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 2, 1])

with c2:
    st.markdown(f"""
        <div class='premium-card'>
            <h1 style='color: #fff; text-shadow: 0 0 15px #00f2ff;'>عضوية النخبة الرقمية</h1>
            <p style='font-size: 4rem; font-weight: 900; color: #00f2ff;'>49$ <small style='font-size: 1rem; color: #fff;'>/ شهر</small></p>
            <div style='background: rgba(0,0,0,0.6); padding: 25px; border-radius: 20px; border: 1px solid #00f2ff; margin: 25px 0;'>
                <p style='color: #00f2ff; margin-bottom: 5px; font-weight: bold;'>PAYONEER ID:</p>
                <p style='font-size: 1.2rem; font-weight: bold; color: #fff;'>SADAM.ALHAJ007@GMAIL.COM</p>
                <p style='color: #34a853; margin-top: 20px; font-weight: bold;'>USDT WALLET (TRC20):</p>
                <p style='font-size: 0.8rem; color: #fff; word-break: break-all;'>TKCvNEvz59717dp5QZbrwCqCzTQqjrNxCX</p>
            </div>
            <a href="mailto:SADAM.ALHAJ007@GMAIL.COM" class='glass-active-btn'>
                تفعيل العضوية الآن 💎
            </a>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br><p style='text-align: center; color: #333;'>POWERED BY SADAM AL-HAJ AI LABS v3.0</p>", unsafe_allow_html=True)
