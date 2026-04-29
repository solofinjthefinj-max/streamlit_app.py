import streamlit as st
import requests

# --- إعدادات الصفحة ---
st.set_page_config(page_title="EcomMind AI Pro", layout="wide")

# تصميم الواجهة الاحترافية (CSS)
st.markdown("""
    <style>
    /* خلفية سينمائية مرتبطة بالذكاء الاصطناعي */
    .stApp {
        background: linear-gradient(rgba(11, 14, 20, 0.8), rgba(11, 14, 20, 0.9)), 
        url('https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&q=80&w=2000');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* العنوان الرئيسي (حاد وشعاعي) */
    .neon-title {
        font-family: 'Arial Black', sans-serif;
        color: #00f2ff;
        text-align: center;
        font-size: 4rem !important;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 5px;
        text-shadow: 0 0 5px #00f2ff, 0 0 10px #00f2ff, 0 0 20px #00d4ff;
        margin-bottom: 0px;
    }

    /* نص الذكاء الاصطناعي (أزرق ليزر حاد) */
    .ai-response {
        color: #00f2ff;
        font-weight: bold;
        text-shadow: 0 0 2px #00f2ff; /* حاد وغير باهت */
        font-size: 1.2rem;
        background: rgba(0, 242, 255, 0.08);
        padding: 25px;
        border-radius: 12px;
        border: 2px solid #00f2ff;
        box-shadow: inset 0 0 15px rgba(0, 242, 255, 0.2);
        line-height: 1.6;
        direction: rtl;
    }

    /* نوافذ الاشتراك المرموقة */
    .premium-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-top: 4px solid #00f2ff;
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        transition: 0.4s;
        backdrop-filter: blur(15px);
    }
    .premium-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 40px rgba(0, 242, 255, 0.2);
        border-color: #ffffff;
    }

    /* زر التوليد */
    .stButton>button {
        width: 100%;
        background: #00f2ff;
        color: #000;
        border: none;
        padding: 20px;
        border-radius: 10px;
        font-weight: 900;
        font-size: 1.3rem;
        box-shadow: 0 0 15px #00f2ff;
    }
    .stButton>button:hover {
        background: #ffffff;
        box-shadow: 0 0 30px #ffffff;
        color: #000;
    }

    input { background-color: rgba(255,255,255,0.1) !important; color: #fff !important; border: 1px solid #00f2ff !important; font-size: 1.2rem !important; }
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
st.markdown("<p style='text-align: center; color: #fff; letter-spacing: 2px;'>ADVANCED ARTIFICIAL INTELLIGENCE FOR E-COMMERCE</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<div style='margin-top: 40px;'>", unsafe_allow_html=True)
    product_name = st.text_input("📦 أدخل اسم المنتج المراد تسويقه")
    if st.button("توليد الإستراتيجية الشعاعية ✨"):
        if product_name:
            with st.spinner('PROCESSING...'):
                result = call_ai(product_name)
                st.markdown(f"<div class='ai-response'>{result}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# نوافذ الاشتراك المرموقة (The Premium Section)
st.markdown("<br><br><br><h2 style='text-align: center; color: #fff;'>خطط العضوية الفاخرة</h2>", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 2, 1])

with c2:
    st.markdown(f"""
        <div class='premium-card'>
            <h2 style='color: #00f2ff; margin-bottom: 10px;'>EXECUTIVE PRO</h2>
            <p style='font-size: 3rem; font-weight: bold; color: #fff;'>49$ <small style='font-size: 1rem;'>/ Monthly</small></p>
            <hr style='border-color: rgba(0,242,255,0.2);'>
            <div style='text-align: right; margin: 25px 0; color: #ddd; line-height: 2;'>
                <p>✅ وصول غير محدود لمحرك Llama 3.1</p>
                <p>✅ إنتاج خطط تسويقية كاملة في ثوانٍ</p>
                <p>✅ دعم تقني VIP مباشر</p>
                <p>✅ ميزة تحليل المنافسين الحصرية</p>
            </div>
            <div style='background: rgba(0,0,0,0.3); padding: 20px; border-radius: 15px; border: 1px solid #333;'>
                <p style='color: #00f2ff; font-size: 0.9rem;'>PAYONEER:</p>
                <p style='font-weight: bold; font-size: 1.1rem;'>SADAM.ALHAJ007@GMAIL.COM</p>
                <br>
                <p style='color: #00f2ff; font-size: 0.9rem;'>USDT (TRC20):</p>
                <p style='font-size: 0.8rem; word-break: break-all; color: #34a853;'>TKCvNEvz59717dp5QZbrwCqCzTQqjrNxCX</p>
            </div>
            <a href="mailto:SADAM.ALHAJ007@GMAIL.COM" style='text-decoration: none;'>
                <div style='margin-top: 30px; background: #fff; color: #000; padding: 15px; border-radius: 10px; font-weight: bold;'>تفعيل العضوية الآن</div>
            </a>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: #555;'>POWERED BY SADAM AL-HAJ AI LABS</p>", unsafe_allow_html=True)
