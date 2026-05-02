import streamlit as st
import requests
import json

# --- إعدادات الصفحة الفنية ---
st.set_page_config(page_title="EcomMind AI Ultra Pro", layout="wide", initial_sidebar_state="collapsed")

# --- حقن الهندسة البصرية المتقدمة (CSS + JS) ---
st.markdown("""
    <style>
    /* 1. تصفير الإعدادات وإخفاء القوائم */
    header, footer, #MainMenu {visibility: hidden;}
    .stApp { background-color: #000000 !important; }

    /* 2. محرك الجزيئات الفضائية في الخلفية */
    #particles-js {
        position: fixed; width: 100vw; height: 100vh;
        top: 0; left: 0; z-index: -1;
        background-image: radial-gradient(circle at center, #001a33 0%, #000000 90%);
    }

    /* 3. دمج الغلاف (الصورة العرضية) */
    .hero-cover {
        width: 100%; max-width: 1000px;
        border-radius: 25px;
        box-shadow: 0 0 40px rgba(0, 242, 255, 0.4);
        margin: 0 auto 20px;
        display: block;
        border: 1px solid rgba(0, 242, 255, 0.2);
    }

    /* 4. اسم المنتج النيوني الحاد */
    .neon-title {
        color: #00f2ff;
        text-align: center;
        font-family: 'Orbitron', sans-serif;
        font-size: 3.5rem !important;
        font-weight: 900;
        text-shadow: 0 0 15px #00f2ff, 0 0 30px #0062ff;
        margin-top: 10px;
        letter-spacing: 5px;
    }

    /* 5. الحل النهائي لخانة البحث (سواد نيون بيضاوي) */
    div[data-baseweb="input"] {
        background-color: #000000 !important;
        border: 2px solid #00f2ff !important;
        border-radius: 50px !important;
        box-shadow: 0 0 25px rgba(0, 242, 255, 0.5) !important;
        height: 70px !important;
        padding: 0 25px !important;
    }
    input {
        color: #00f2ff !important;
        background-color: transparent !important;
        -webkit-text-fill-color: #00f2ff !important;
        font-size: 1.5rem !important;
        font-weight: bold !important;
        text-align: center !important;
        border: none !important;
    }

    /* 6. زر التوليد الشعاعي */
    .stButton>button {
        width: 100%; background: linear-gradient(90deg, #00f2ff, #0062ff) !important;
        color: #000 !important; font-weight: 900 !important; border-radius: 50px !important;
        height: 60px; border: none !important; box-shadow: 0 0 25px #00f2ff !important;
        font-size: 1.3rem; margin-top: 15px; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 50px #00f2ff !important; }

    /* 7. النافذة الزجاجية (الكريستال الأزرق المشع) */
    .premium-card {
        background: rgba(0, 242, 255, 0.03) !important;
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border: 2px solid rgba(0, 242, 255, 0.4) !important;
        border-radius: 40px;
        padding: 50px; text-align: center;
        box-shadow: 0 0 60px rgba(0, 0, 0, 0.8);
        margin-top: 40px;
    }

    .glass-btn {
        background: rgba(0, 242, 255, 0.1); border: 2px solid #00f2ff;
        color: #fff !important; padding: 18px 50px; border-radius: 50px;
        font-weight: 900; text-decoration: none; display: inline-block;
        box-shadow: 0 0 20px #00f2ff; transition: 0.4s; font-size: 1.3rem;
    }
    .glass-btn:hover { background: #00f2ff; color: #000 !important; box-shadow: 0 0 60px #00f2ff; }
    
    .result-box {
        background: rgba(0, 5, 15, 0.9); border: 2px solid #00f2ff;
        color: #00f2ff; padding: 30px; border-radius: 25px;
        margin-top: 30px; direction: rtl; line-height: 1.8;
        box-shadow: 0 0 30px rgba(0, 242, 255, 0.3); text-shadow: 0 0 5px #00f2ff;
    }
    </style>

    <div id="particles-js"></div>
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
        particlesJS('particles-js', {
            "particles": {
                "number": { "value": 160 },
                "color": { "value": "#00f2ff" },
                "shape": { "type": "circle" },
                "opacity": { "value": 0.6, "random": true },
                "size": { "value": 3, "random": true },
                "line_linked": { "enable": true, "distance": 130, "color": "#00f2ff", "opacity": 0.4, "width": 1 },
                "move": { "enable": true, "speed": 4, "direction": "none", "random": true, "out_mode": "out" }
            }
        });
    </script>
""", unsafe_allow_html=True)

# --- محرك الاستجابة الذكي (إصلاح خطأ 401) ---
def call_groq_engine(query):
    api_key = "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"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "أنت خبير تسويق رقمي محترف. قدم استراتيجية كاملة تتضمن وصفاً جذاباً، كلمات SEO، وسيناريو فيديو."},
            {"role": "user", "content": query}
        ],
        "temperature": 0.7
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=25)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return f"⚠️ المحرك يستعد.. يرجى الضغط مجدداً (كود {response.status_code})"
    except:
        return "⚠️ فشل في المعالجة.. تحقق من اتصال الإنترنت."

# --- الواجهة البرمجية ---

# 1. عرض الغلاف
st.markdown('<img src="https://raw.githubusercontent.com/alhajameer4-del/Python/main/cover.png" class="hero-cover">', unsafe_allow_html=True)

# 2. اسم المنتج
st.markdown('<h1 class="neon-title">EcomMind AI</h1>', unsafe_allow_html=True)

# 3. منطقة الإدخال
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    product_in = st.text_input("", placeholder="أدخل اسم المنتج لبدء السحر الشعاعي...")
    if st.button("إطلاق المعالجة الشعاعية ⚡"):
        if product_in:
            with st.spinner('SYSTEM ANALYZING...'):
                res = call_groq_engine(product_in)
                st.markdown(f"<div class='result-box'>{res}</div>", unsafe_allow_html=True)

# 4. قسم الاشتراك (نفس نهاية الفيديو)
st.markdown("<br><br>", unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class='premium-card'>
            <h2 style='color:#fff; text-shadow: 0 0 10px #00f2ff;'>EXECUTIVE PRO</h2>
            <p style='font-size:3.5rem; font-weight:900; color:#00f2ff; margin:0;'>49$</p>
            <p style='color:#888; margin-bottom: 30px;'>المعالجة الذكية اللامحدودة ودعم فني VIP</p>
            <a href="mailto:SADAM.ALHAJ007@GMAIL.COM?subject=Upgrade" class="glass-btn">الذهاب للدفع الآمن 🔒</a>
            <p style='color:#111; font-size:0.5rem; margin-top:20px;'>V12.0 Final PRO</p>
        </div>
    """, unsafe_allow_html=True)
