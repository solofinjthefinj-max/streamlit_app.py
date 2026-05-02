import streamlit as st
import requests
import json

# --- إعدادات النظام الأساسية ---
st.set_page_config(page_title="EcomMind AI Pro", layout="wide", initial_sidebar_state="collapsed")

# --- حقن الهندسة البصرية الفضائية (CSS + JS) ---
st.markdown("""
    <style>
    /* 1. تصفير واجهة سترمليت وتثبيت السواد المطلق */
    header, footer, #MainMenu {visibility: hidden;}
    .stApp {
        background-color: #000000 !important;
        background: radial-gradient(circle at center, #001a33 0%, #000000 90%) !important;
        overflow: hidden;
    }

    /* 2. محرك الجزيئات الفضائية */
    #particles-js {
        position: fixed; width: 100vw; height: 100vh;
        top: 0; left: 0; z-index: -1;
    }

    /* 3. تصميم الغلاف السينمائي (الصورة العرضية) */
    .hero-cover {
        width: 100%; max-width: 1000px;
        border-radius: 30px;
        box-shadow: 0 0 50px rgba(0, 242, 255, 0.5);
        margin: 0 auto 10px;
        display: block;
        border: 2px solid rgba(0, 242, 255, 0.3);
        transition: 0.5s;
    }
    .hero-cover:hover { transform: scale(1.01); filter: brightness(1.2); }

    /* 4. اسم المنتج (ليزر شعاعي متوهج) */
    .product-title {
        color: #00f2ff;
        text-align: center;
        font-family: 'Orbitron', sans-serif;
        font-size: 4rem !important;
        font-weight: 900;
        text-shadow: 0 0 15px #00f2ff, 0 0 40px #0062ff;
        margin-top: 10px;
        letter-spacing: 8px;
        text-transform: uppercase;
    }

    /* 5. الحل الجذري لخانة البحث (بيضوية، متوهجة، سوداء تماماً) */
    div[data-baseweb="input"] {
        background-color: #000000 !important;
        border: 2px solid #00f2ff !important;
        border-radius: 60px !important; /* شكل بيضاوي مثالي */
        box-shadow: 0 0 30px rgba(0, 242, 255, 0.6) !important;
        height: 75px !important;
        padding: 0 30px !important;
    }
    input {
        color: #00f2ff !important;
        background-color: transparent !important;
        -webkit-text-fill-color: #00f2ff !important;
        font-size: 1.6rem !important;
        font-weight: 900 !important;
        text-align: center !important;
        border: none !important;
        caret-color: #00f2ff !important; /* لون مؤشر الكتابة */
    }
    /* منع ظهور الخلفية البيضاء عند النقر */
    div[class*="st-"] { background-color: transparent !important; }

    /* 6. زر التوليد الشعاعي (نيون ليزر) */
    .stButton>button {
        width: 100%; background: linear-gradient(90deg, #00f2ff, #0062ff) !important;
        color: #000 !important; font-weight: 900 !important; border-radius: 50px !important;
        height: 65px; border: none !important; box-shadow: 0 0 30px #00f2ff !important;
        font-size: 1.4rem; margin-top: 20px; transition: 0.4s;
    }
    .stButton>button:hover { transform: scale(1.03); box-shadow: 0 0 60px #00f2ff !important; filter: brightness(1.2); }

    /* 7. النتائج الذكية (زجاج مشفر) */
    .result-box {
        background: rgba(0, 5, 15, 0.95); border: 2px solid #00f2ff;
        color: #00f2ff; padding: 35px; border-radius: 30px;
        margin-top: 30px; direction: rtl; line-height: 1.8;
        box-shadow: 0 0 40px rgba(0, 242, 255, 0.4); 
        text-shadow: 0 0 5px #00f2ff; font-size: 1.2rem;
    }

    /* 8. نافذة الاشتراك (كريستال نيون فضائي) */
    .premium-card {
        background: rgba(255, 255, 255, 0.02) !important;
        backdrop-filter: blur(30px);
        -webkit-backdrop-filter: blur(30px);
        border: 2px solid rgba(0, 242, 255, 0.5) !important;
        border-radius: 45px;
        padding: 60px; text-align: center;
        box-shadow: 0 0 80px rgba(0, 0, 0, 0.9);
        margin-top: 50px;
    }

    .checkout-btn {
        background: rgba(0, 242, 255, 0.1); border: 2px solid #00f2ff;
        color: #fff !important; padding: 22px 60px; border-radius: 50px;
        font-weight: 900; text-decoration: none; display: inline-block;
        box-shadow: 0 0 30px #00f2ff; transition: 0.5s; font-size: 1.5rem;
    }
    .checkout-btn:hover { background: #00f2ff; color: #000 !important; box-shadow: 0 0 70px #00f2ff; transform: scale(1.1); }
    </style>

    <div id="particles-js"></div>
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
        particlesJS('particles-js', {
            "particles": {
                "number": { "value": 180, "density": { "enable": true, "value_area": 800 } },
                "color": { "value": "#00f2ff" },
                "shape": { "type": "circle" },
                "opacity": { "value": 0.7, "random": true },
                "size": { "value": 3, "random": true },
                "line_linked": { "enable": true, "distance": 130, "color": "#00f2ff", "opacity": 0.4, "width": 1 },
                "move": { "enable": true, "speed": 4, "direction": "none", "random": true, "straight": false, "out_mode": "out", "bounce": false }
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": { "onhover": { "enable": true, "mode": "grab" }, "onclick": { "enable": true, "mode": "push" } }
            },
            "retina_detect": true
        });
    </script>
""", unsafe_allow_html=True)

# --- المحرك الذكي الصارم (أقوى استجابة) ---
def start_ai_engine(query):
    api_key = "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"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "أنت خبير تجارة إلكترونية عالمي. قدم استراتيجية مبيعات مكتملة تتضمن وصف AIDA، كلمات SEO، وسيناريو إعلان فيديو جذاب."},
            {"role": "user", "content": query}
        ],
        "temperature": 0.7,
        "max_tokens": 2048
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=25)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return f"⚠️ المحرك يعيد شحن طاقته.. (كود {response.status_code}). اضغط مرة أخرى."
    except:
        return "⚠️ فشل في الاتصال الشعاعي.. تأكد من الإنترنت."

# --- واجهة المستخدم النهائية ---

# 1. الغلاف السينمائي
st.markdown('<img src="https://raw.githubusercontent.com/alhajameer4-del/Python/main/cover.png" class="hero-cover">', unsafe_allow_html=True)

# 2. اسم المنتج
st.markdown('<h1 class="product-title">EcomMind AI</h1>', unsafe_allow_html=True)

# 3. وحدة الإدخال
col1, col2, col3 = st.columns([1, 2.5, 1])
with col2:
    p_input = st.text_input("", placeholder="أدخل اسم المنتج لتوليد السحر النيوني...")
    if st.button("إطلاق المعالجة الشعاعية ⚡"):
        if p_input:
            with st.spinner('SYSTEM ANALYZING...'):
                result = start_ai_engine(p_input)
                st.markdown(f"<div class='result-box'>{result}</div>", unsafe_allow_html=True)

# 4. قسم الاشتراك الإمبراطوري (Executive Pro)
st.markdown("<br><br>", unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class='premium-card'>
            <h2 style='color:#fff; text-shadow: 0 0 15px #00f2ff; letter-spacing: 3px;'>EXECUTIVE PRO</h2>
            <p style='font-size:4rem; font-weight:900; color:#00f2ff; margin:0;'>49$</p>
            <p style='color:#888; margin-bottom: 40px;'>أولوية المعالجة الذكية اللامحدودة ودعم فني VIP</p>
            <a href="mailto:SADAM.ALHAJ007@GMAIL.COM?subject=Upgrade%20to%20EcomMind%20PRO" class="checkout-btn">الذهاب للدفع الآمن 🔒</a>
            <p style='color:#111; font-size:0.5rem; margin-top:25px;'>V13.0 FINAL MASTERPIECE</p>
        </div>
    """, unsafe_allow_html=True)
