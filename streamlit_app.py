import streamlit as st
import requests

# --- إعدادات الصفحة ---
st.set_page_config(page_title="EcomMind AI Pro", layout="wide")

# تصميم الواجهة الاحترافية (CSS)
st.markdown("""
    <style>
    /* خلفية سينمائية للذكاء الاصطناعي */
    .stApp {
        background: linear-gradient(rgba(11, 14, 20, 0.85), rgba(11, 14, 20, 0.95)), 
        url('https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&q=80&w=2000');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* العنوان الرئيسي (حاد وشعاعي) */
    .neon-title {
        font-family: 'Arial Black', sans-serif;
        color: #00f2ff;
        text-align: center;
        font-size: 3.5rem !important;
        font-weight: 900;
        text-shadow: 0 0 15px #00f2ff;
        margin-bottom: 5px;
    }

    /* إصلاح خانة الكتابة - جعلها داكنة وشفافة */
    div[data-baseweb="input"] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid #00f2ff !important;
        border-radius: 12px !important;
    }
    input {
        color: #ffffff !important;
        background-color: transparent !important;
    }

    /* نص الذكاء الاصطناعي (أزرق ليزر حاد) */
    .ai-response {
        color: #00f2ff;
        font-weight: bold;
        text-shadow: 0 0 2px #00f2ff;
        font-size: 1.2rem;
        background: rgba(0, 242, 255, 0.08);
        padding: 25px;
        border-radius: 12px;
        border: 2px solid #00f2ff;
        box-shadow: inset 0 0 15px rgba(0, 242, 255, 0.2);
        direction: rtl;
    }

    /* نافذة الاشتراك المرموقة */
    .premium-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 30px;
        padding: 40px;
        text-align: center;
        backdrop-filter: blur(20px);
    }

    /* زر تفعيل العضوية (زجاجي أزرق مميز) */
    .glass-active-btn {
        background: rgba(0, 150, 255, 0.2);
        backdrop-filter: blur(15px);
        border: 2px solid rgba(0, 242, 255, 0.6);
        color: #fff;
        padding: 20px 40px;
        border-radius: 15px;
        font-weight: bold;
        font-size: 1.3rem;
        text-decoration: none;
        display: inline-block;
        transition: 0.4s;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.3);
        margin-top: 20px;
    }
    .glass-active-btn:hover {
        background: rgba(0, 242, 255, 0.5);
        box-shadow: 0 0 40px #00f2ff;
        border-color: #fff;
        transform: scale(1.05);
    }

    /* زر التوليد الرئيسي */
    .stButton>button {
        background: #00f2ff;
        color: #000;
        border-radius: 10px;
        font-weight: 900;
        font-size: 1.2rem;
        padding: 15px;
        box-shadow: 0 0 15px #00f2ff;
    }
    </style>
    """, unsafe_allow_html=True)

# محرك الذكاء الاصطناعي
def call_ai(product):
    api_key = "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"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": f"اكتب وصفاً تسويقياً لمنتج: {product}"}]
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        return response.json()['choices'][0]['message']['content']
    except:
        return "فشل النظام في الاستجابة.."

# الواجهة
st.markdown("<h1 class='neon-title'>EcomMind AI PRO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #fff; letter-spacing: 2px; font-weight: 300;'>PREMIUM AI MARKETING ENGINE</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<div style='margin-top: 30px;'>", unsafe_allow_html=True)
    product_name = st.text_input("📦 أدخل اسم المنتج")
    if st.button("توليد الإستراتيجية الشعاعية ✨"):
        if product_name:
            with st.spinner('PROCESSING...'):
                result = call_ai(product_name)
                st.markdown(f"<div class='ai-response'>{result}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# قسم العضوية الفاخرة
st.markdown("<br><br><br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 2, 1])

with c2:
    st.markdown(f"""
        <div class='premium-card'>
            <h2 style='color: #00f2ff;'>EXECUTIVE MEMBERSHIP</h2>
            <p style='font-size: 3rem; font-weight: 900;'>49$ <small style='font-size: 1rem;'>/ Monthly</small></p>
            <div style='text-align: right; margin: 20px 0; color: #ccc;'>
                <p>✅ محرك Llama 3.1 فائق السرعة</p>
                <p>✅ إنتاج محتوى بيعي بلا حدود</p>
                <p>✅ أولوية في المعالجة الذكية</p>
            </div>
            <div style='background: rgba(0,0,0,0.4); padding: 15px; border-radius: 15px; border: 1px solid rgba(0,242,255,0.3);'>
                <p style='color: #00f2ff; font-size: 0.8rem;'>PAYONEER:</p>
                <p style='font-weight: bold;'>SADAM.ALHAJ007@GMAIL.COM</p>
                <p style='color: #34a853; font-size: 0.8rem; margin-top: 10px;'>USDT (TRC20):</p>
                <p style='font-size: 0.7rem; word-break: break-all;'>TKCvNEvz59717dp5QZbrwCqCzTQqjrNxCX</p>
            </div>
            <a href="mailto:SADAM.ALHAJ007@GMAIL.COM" class='glass-active-btn'>
                تفعيل العضوية الآن 💎
            </a>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: #444;'>SADAM AL-HAJ AI LABS © 2024</p>", unsafe_allow_html=True)
