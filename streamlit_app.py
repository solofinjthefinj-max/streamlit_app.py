import streamlit as st
import requests

# --- إعدادات الصفحة ---
st.set_page_config(page_title="EcomMind AI Ultra", layout="wide")

# --- محرك الجزيئات والخلفية التقنية (CSS & JS) ---
st.markdown("""
    <style>
    /* خلفية داكنة ثابتة */
    .stApp {
        background-color: #05070a;
        overflow: hidden;
    }

    /* نظام الجزيئات المتحركة (تأثير نيوتني تقني) */
    #particles-js {
        position: fixed;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        z-index: -1;
    }

    /* العنوان النيوني الصارخ */
    .neon-title {
        font-family: 'Orbitron', sans-serif;
        color: #00f2ff;
        text-align: center;
        font-size: 4rem !important;
        font-weight: 900;
        text-shadow: 0 0 20px #00f2ff, 0 0 40px #0062ff;
        margin-bottom: 10px;
    }

    /* حل نهائي وجذري لخانة الكتابة (إجبار اللون الداكن) */
    div[data-baseweb="input"], .stTextInput input {
        background-color: rgba(0, 242, 255, 0.05) !important;
        color: #00f2ff !important;
        border: 2px solid #00f2ff !important;
        border-radius: 15px !important;
        font-size: 1.2rem !important;
        box-shadow: 0 0 10px rgba(0, 242, 255, 0.2) !important;
    }
    label { color: #00f2ff !important; font-weight: bold !important; }

    /* نتائج الذكاء الاصطناعي (ليزر حاد) */
    .ai-response {
        color: #00f2ff;
        font-weight: bold;
        text-shadow: 0 0 5px #00f2ff;
        font-size: 1.3rem;
        background: rgba(0, 5, 10, 0.8);
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #00f2ff;
        box-shadow: 0 0 30px rgba(0, 242, 255, 0.3);
        line-height: 1.7;
        direction: rtl;
    }

    /* نافذة الاشتراك (كريستال أزرق مشع) */
    .premium-card {
        background: rgba(0, 100, 255, 0.1);
        backdrop-filter: blur(25px);
        border: 3px solid #00f2ff;
        border-radius: 35px;
        padding: 50px;
        text-align: center;
        box-shadow: 0 0 50px rgba(0, 242, 255, 0.4);
        margin-top: 50px;
    }

    /* زر تفعيل العضوية (الجوهرة الزرقاء) */
    .glass-active-btn {
        background: linear-gradient(135deg, #00f2ff 0%, #0062ff 100%);
        border: 2px solid #fff;
        color: #fff !important;
        padding: 20px 50px;
        border-radius: 20px;
        font-weight: 900;
        font-size: 1.5rem;
        text-decoration: none;
        display: inline-block;
        box-shadow: 0 0 30px #00f2ff;
        transition: 0.5s;
        text-transform: uppercase;
    }
    .glass-active-btn:hover {
        transform: scale(1.1) rotate(1deg);
        box-shadow: 0 0 60px #00f2ff;
        filter: brightness(1.2);
    }

    /* أزرار Streamlit */
    .stButton>button {
        background: #00f2ff !important;
        color: #000 !important;
        font-weight: 900 !important;
        border-radius: 15px !important;
        height: 60px;
        box-shadow: 0 0 20px #00f2ff;
    }
    </style>

    <!-- إضافة مكتبة الجزيئات -->
    <div id="particles-js"></div>
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
        particlesJS('particles-js', {
            "particles": {
                "number": { "value": 100 },
                "color": { "value": "#00f2ff" },
                "shape": { "type": "circle" },
                "opacity": { "value": 0.5 },
                "size": { "value": 3 },
                "line_linked": { "enable": true, "distance": 150, "color": "#00f2ff", "opacity": 0.4, "width": 1 },
                "move": { "enable": true, "speed": 4 }
            }
        });
    </script>
    """, unsafe_allow_html=True)

# محرك الذكاء الاصطناعي
def call_ai(product):
    api_key = "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"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": f"اكتب استراتيجية تسويقية كاملة لمنتج: {product}"}]
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        return response.json()['choices'][0]['message']['content']
    except:
        return "⚠️ النظام متصل.. جاري إعادة المحاولة"

# واجهة التطبيق
st.markdown("<h1 class='neon-title'>ECOMMIND AI PRO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #00f2ff; font-weight: bold; letter-spacing: 5px;'>NEURONAL MARKETING ENGINE</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<div style='margin-top: 50px;'>", unsafe_allow_html=True)
    # الخانة الآن محصنة ضد اللون الأبيض
    product_name = st.text_input("🔍 استفسر من العقل الاصطناعي عن منتجك:")
    if st.button("إطلاق المعالجة الشعاعية ⚡"):
        if product_name:
            with st.spinner('SYSTEM ANALYZING...'):
                result = call_ai(product_name)
                st.markdown(f"<div class='ai-response'>{result}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# قسم الاشتراك الإمبراطوري
st.markdown("<br><br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 2, 1])

with c2:
    st.markdown(f"""
        <div class='premium-card'>
            <h1 style='color: #fff; text-shadow: 0 0 10px #00f2ff;'>عضوية النخبة</h1>
            <p style='font-size: 4rem; font-weight: 900; color: #00f2ff;'>49$ <small style='font-size: 1rem; color: #fff;'>/ شهر</small></p>
            <div style='background: rgba(0,0,0,0.5); padding: 25px; border-radius: 20px; border: 1px solid #00f2ff; margin: 20px 0;'>
                <p style='color: #00f2ff; margin-bottom: 5px;'>ID PAYONEER:</p>
                <p style='font-size: 1.2rem; font-weight: bold; color: #fff;'>SADAM.ALHAJ007@GMAIL.COM</p>
                <p style='color: #34a853; margin-top: 15px;'>USDT (TRC20):</p>
                <p style='font-size: 0.9rem; color: #fff; word-break: break-all;'>TKCvNEvz59717dp5QZbrwCqCzTQqjrNxCX</p>
            </div>
            <a href="mailto:SADAM.ALHAJ007@GMAIL.COM" class='glass-active-btn'>
                تفعيل العضوية الآن 💎
            </a>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br><p style='text-align: center; color: #333;'>SADAM AL-HAJ AI SYSTEMS v2.0</p>", unsafe_allow_html=True)
