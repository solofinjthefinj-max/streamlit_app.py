import streamlit as st
import requests

# --- إعدادات الصفحة ---
st.set_page_config(page_title="EcomMind AI Ultra Pro", layout="wide", initial_sidebar_state="collapsed")

# --- محرك الفضاء والجزيئات النيونية (CSS & JS) ---
st.markdown("""
    <style>
    /* 1. تصميم الفضاء العميق */
    .stApp {
        background-color: #000000;
        overflow: hidden;
    }

    /* محرك الجزيئات في الخلفية */
    #particles-js {
        position: fixed;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        z-index: -1;
    }

    /* 2. تأثير الزجاج الشفاف (Glassmorphism) للنوافذ */
    .glass-panel {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(0, 242, 255, 0.2);
        border-radius: 30px;
        padding: 40px;
        box-shadow: 0 8px 32px 0 rgba(0, 242, 255, 0.2);
        margin-bottom: 20px;
    }

    /* 3. إصلاح خانة الكتابة - إجبار السواد والنيون */
    div[data-baseweb="input"] {
        background-color: rgba(0, 10, 20, 0.7) !important;
        border: 2px solid #00f2ff !important;
        border-radius: 15px !important;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.4) !important;
    }
    input {
        color: #00f2ff !important;
        background-color: transparent !important;
        font-weight: bold !important;
    }

    /* 4. زر الدفع الزجاجي المشع */
    .checkout-btn {
        background: rgba(0, 242, 255, 0.15);
        backdrop-filter: blur(10px);
        border: 2px solid #00f2ff;
        color: #fff !important;
        padding: 18px 45px;
        border-radius: 15px;
        font-weight: 900;
        font-size: 1.4rem;
        text-decoration: none !important;
        display: inline-block;
        transition: 0.4s;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.4);
        text-transform: uppercase;
    }
    .checkout-btn:hover {
        background: #00f2ff;
        color: #000 !important;
        box-shadow: 0 0 50px #00f2ff;
        transform: scale(1.05);
    }

    /* 5. زر التوليد */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #00f2ff, #0062ff) !important;
        color: white !important;
        font-weight: 900 !important;
        border-radius: 15px !important;
        height: 60px;
        box-shadow: 0 0 20px #00f2ff;
        border: none !important;
    }
    </style>

    <!-- إضافة مكتبة Particles.js لخلق فضاء النيون -->
    <div id="particles-js"></div>
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
        particlesJS('particles-js', {
            "particles": {
                "number": { "value": 120, "density": { "enable": true, "value_area": 800 } },
                "color": { "value": "#00f2ff" },
                "shape": { "type": "circle" },
                "opacity": { "value": 0.5, "random": true },
                "size": { "value": 3, "random": true },
                "line_linked": { "enable": true, "distance": 150, "color": "#00f2ff", "opacity": 0.3, "width": 1 },
                "move": { "enable": true, "speed": 3, "direction": "none", "random": true, "straight": false, "out_mode": "out", "bounce": false }
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": { "onhover": { "enable": true, "mode": "grab" }, "onclick": { "enable": true, "mode": "push" } },
                "modes": { "grab": { "distance": 200, "line_linked": { "opacity": 1 } } }
            },
            "retina_detect": true
        });
    </script>
    """, unsafe_allow_html=True)

# استدعاء المحرك
def call_ai_pro(product):
    api_key = "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"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": f"اكتب استراتيجية تسويقية ووصف لمنتج: {product}"}]
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        return response.json()['choices'][0]['message']['content']
    except: return "⚠️ النظام متصل.. جاري المعالجة الفضائية"

# --- الواجهة الرئيسية ---
st.markdown(f'<div style="text-align: center; margin-top: -50px;"><img src="https://raw.githubusercontent.com/alhajameer4-del/Python/main/logo.png" style="width: 280px; filter: drop-shadow(0 0 20px #00f2ff);"></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
    product_query = st.text_input("🔍 اسم المنتج المراد معالجته بذكاء:")
    if st.button("إطلاق المعالجة الشعاعية ✨"):
        if product_query:
            with st.spinner('SYSTEM ANALYZING...'):
                result = call_ai_pro(product_query)
                st.markdown(f"<div style='color:#00f2ff; background:rgba(0,0,0,0.7); padding:20px; border:1px solid #00f2ff; border-radius:15px;'>{result}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- قسم الدفع الكريستالي ---
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    st.markdown(f"""
        <div class='glass-panel' style='text-align: center;'>
            <h1 style='color: #fff; text-shadow: 0 0 15px #00f2ff; font-weight: 900;'>EXECUTIVE PRO</h1>
            <p style='font-size: 3.5rem; font-weight: 900; color: #00f2ff; margin: 0;'>49$</p>
            <p style='color: #888; margin-bottom: 30px;'>عضوية النخبة: دعم فني ومعالجة ذكية بلا حدود</p>
            <a href="mailto:SADAM.ALHAJ007@GMAIL.COM?subject=Upgrade%20to%20PRO" class='checkout-btn'>
                الذهاب للدفع الآمن 🔒
            </a>
            <p style='color: #333; font-size: 0.7rem; margin-top: 20px;'>SADAM AL-HAJ AI LABS v7.0</p>
        </div>
    """, unsafe_allow_html=True)
