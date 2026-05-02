import streamlit as st
import requests

# --- إعدادات الصفحة ---
st.set_page_config(page_title="EcomMind AI Ultra Pro", layout="wide", initial_sidebar_state="collapsed")

# --- التصميم السينمائي المتكامل (CSS) ---
st.markdown("""
    <style>
    /* 1. إخفاء العناصر الافتراضية لسترمليت */
    header, footer, #MainMenu {visibility: hidden;}

    /* 2. الخلفية الفضائية العميقة */
    .stApp {
        background-color: #000000 !important;
        background-image: radial-gradient(circle at center, #001a33 0%, #000000 85%) !important;
    }

    /* محرك الجزيئات في الخلفية */
    #particles-js {
        position: fixed; width: 100%; height: 100%; top: 0; left: 0; z-index: -1;
    }

    /* 3. تصميم اسم المنتج الشعاعي (تحت الشعار) */
    .product-title {
        color: #00f2ff;
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
        font-size: 3rem !important;
        font-weight: 900;
        text-shadow: 0 0 15px #00f2ff, 0 0 30px #0062ff;
        margin-top: -10px;
        margin-bottom: 30px;
        letter-spacing: 5px;
    }

    /* 4. خانة البحث البيضوية المتوهجة (مطابقة تماماً للصورة) */
    div[data-baseweb="input"] {
        background-color: #000000 !important;
        border: 2px solid #00f2ff !important;
        border-radius: 50px !important;
        box-shadow: 0 0 20px #00f2ff, inset 0 0 10px rgba(0, 242, 255, 0.2) !important;
        padding: 5px 25px !important;
        transition: 0.3s;
    }
    input {
        color: #00f2ff !important;
        background-color: transparent !important;
        -webkit-text-fill-color: #00f2ff !important;
        font-size: 1.4rem !important;
        font-weight: bold !important;
        text-align: center !important;
    }

    /* 5. زر التوليد النيوني */
    .stButton>button {
        width: 100%; 
        background: linear-gradient(90deg, #00f2ff, #0062ff) !important;
        color: #000 !important; 
        font-weight: 900 !important; 
        border-radius: 50px !important;
        height: 60px; 
        border: none !important; 
        box-shadow: 0 0 20px #00f2ff !important;
        margin-top: 15px;
        font-size: 1.2rem;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 40px #00f2ff !important;
    }

    /* 6. نافذة الاشتراك الزجاجية (الكريستال) */
    .premium-card {
        background: rgba(255, 255, 255, 0.02) !important;
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border: 1px solid rgba(0, 242, 255, 0.3) !important;
        border-radius: 40px;
        padding: 40px; 
        text-align: center;
        box-shadow: 0 0 50px rgba(0, 0, 0, 0.8);
    }

    /* 7. صندوق النتائج الشعاعي */
    .result-box {
        background: rgba(0, 5, 15, 0.9);
        border: 2px solid #00f2ff;
        color: #00f2ff;
        padding: 25px;
        border-radius: 25px;
        margin-top: 30px;
        direction: rtl;
        line-height: 1.8;
        box-shadow: 0 0 30px rgba(0, 242, 255, 0.3);
        text-shadow: 0 0 5px #00f2ff;
    }

    .glass-btn {
        background: rgba(0, 242, 255, 0.1);
        border: 2px solid #00f2ff;
        color: #fff !important;
        padding: 15px 45px;
        border-radius: 50px;
        font-weight: 900;
        text-decoration: none;
        display: inline-block;
        box-shadow: 0 0 20px #00f2ff;
        transition: 0.3s;
    }
    .glass-btn:hover { background: #00f2ff; color: #000 !important; box-shadow: 0 0 50px #00f2ff; }
    </style>

    <div id="particles-js"></div>
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
        particlesJS('particles-js', {
            "particles": {
                "number": { "value": 160 },
                "color": { "value": "#00f2ff" },
                "shape": { "type": "circle" },
                "opacity": { "value": 0.5 },
                "size": { "value": 2 },
                "line_linked": { "enable": true, "distance": 150, "color": "#00f2ff", "opacity": 0.3 },
                "move": { "enable": true, "speed": 4, "direction": "none", "random": true, "out_mode": "out" }
            }
        });
    </script>
""", unsafe_allow_html=True)

# --- المحرك البرمجي (Groq) ---
def run_ai_engine(query):
    api_key = "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"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": f"أنت خبير تسويق محترف. اكتب وصف بيعي مذهل لمنتج: {query}"}],
        "temperature": 0.7
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=20)
        return response.json()['choices'][0]['message']['content']
    except:
        return "⚠️ النظام متصل.. جاري إعادة المحاولة خلال لحظات."

# --- الواجهة البرمجية ---

# 1. الشعار (Logo)
st.markdown(f'<div style="text-align:center;"><img src="https://raw.githubusercontent.com/alhajameer4-del/Python/main/logo.png" style="width:220px; filter:drop-shadow(0 0 20px #00f2ff);"></div>', unsafe_allow_html=True)

# 2. اسم المنتج (تحت الشعار)
st.markdown('<h1 class="product-title">EcomMind AI</h1>', unsafe_allow_html=True)

# 3. منطقة الإدخال والبحث
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    product = st.text_input("", placeholder="ما هو المنتج الذي تريد تسويقه بذكاء؟")
    if st.button("إطلاق المعالجة الشعاعية ⚡"):
        if product:
            with st.spinner('SYSTEM ANALYZING...'):
                res = run_ai_engine(product)
                st.markdown(f"<div class='result-box'>{res}</div>", unsafe_allow_html=True)

# 4. قسم الاشتراك الفاخر
st.markdown("<br><br><br>", unsafe_allow_html=True)
with col2:
    st.markdown(f"""
        <div class='premium-card'>
            <h2 style='color:#fff; text-shadow: 0 0 10px #00f2ff;'>EXECUTIVE PRO</h2>
            <p style='font-size:3.5rem; font-weight:900; color:#00f2ff; margin:0;'>49$</p>
            <p style='color:#888; margin-bottom: 25px;'>أولوية المعالجة ودعم فني مخصص للنخبة</p>
            <a href="mailto:SADAM.ALHAJ007@GMAIL.COM?subject=Upgrade%20to%20PRO" class="glass-btn">الذهاب للدفع الآمن 🔒</a>
            <p style='color:#111; font-size:0.5rem; margin-top:20px;'>V10.0</p>
        </div>
    """, unsafe_allow_html=True)
