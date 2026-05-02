import streamlit as st
import requests

# --- إعدادات الصفحة ---
st.set_page_config(page_title="EcomMind AI Ultra Pro", layout="wide", initial_sidebar_state="collapsed")

# --- الهندسة اللونية (مطابقة للفيديو تماماً) ---
st.markdown("""
    <style>
    /* 1. الخلفية: سواد مطلق مع توهج أزرق شعاعي من المركز */
    .stApp {
        background: #000000 !important;
        background-image: radial-gradient(circle at center, rgba(0, 242, 255, 0.15) 0%, #000000 70%) !important;
    }

    #particles-js {
        position: fixed;
        width: 100vw;
        height: 100vh;
        top: 0;
        left: 0;
        z-index: -1;
    }

    /* 2. خانة البحث: سوداء من الداخل مع توهج ليزري حاد (مثل الفيديو ثانية 0:01) */
    div[data-baseweb="input"] {
        background-color: #000000 !important; /* سواد خالص مثل الفيديو */
        border: 2px solid #00f2ff !important; /* أزرق كهربائي */
        border-radius: 15px !important;
        box-shadow: 0 0 15px #00f2ff, inset 0 0 10px rgba(0, 242, 255, 0.5) !important;
        padding: 5px !important;
    }
    
    input {
        color: #00f2ff !important; /* لون النص نيون */
        background-color: transparent !important;
        -webkit-text-fill-color: #00f2ff !important;
        font-family: 'Courier New', Courier, monospace;
        font-size: 1.4rem !important;
        text-shadow: 0 0 10px #00f2ff !important;
    }

    /* 3. الأزرار: تدرج الليزر (Cyan to Deep Blue) */
    .stButton>button {
        background: linear-gradient(90deg, #00f2ff, #0062ff) !important;
        color: white !important;
        font-weight: 900 !important;
        border-radius: 12px !important;
        height: 60px !important;
        border: none !important;
        box-shadow: 0 0 25px rgba(0, 242, 255, 0.6) !important;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    .stButton>button:hover {
        box-shadow: 0 0 50px #00f2ff !important;
        transform: scale(1.02);
    }

    /* 4. النوافذ الزجاجية: شفافة جداً ومبهمة (مثل الثانية 0:15) */
    .glass-panel {
        background: rgba(255, 255, 255, 0.02) !important;
        backdrop-filter: blur(25px) !important;
        -webkit-backdrop-filter: blur(25px) !important;
        border: 1px solid rgba(0, 242, 255, 0.3) !important;
        border-radius: 30px !important;
        padding: 40px !important;
        box-shadow: 0 0 40px rgba(0, 0, 0, 0.5) !important;
    }

    /* 5. زر الدفع (الكريستال الأزرق المشع) */
    .checkout-btn {
        background: rgba(0, 242, 255, 0.1) !important;
        border: 2px solid #00f2ff !important;
        color: #fff !important;
        padding: 20px 50px !important;
        border-radius: 15px !important;
        font-weight: 900 !important;
        font-size: 1.5rem !important;
        text-decoration: none !important;
        display: inline-block !important;
        box-shadow: 0 0 30px #00f2ff !important;
        transition: 0.5s !important;
    }
    </style>

    <!-- حقن نظام جزيئات النيون (Warp Speed Effect) -->
    <div id="particles-js"></div>
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
        particlesJS('particles-js', {
            "particles": {
                "number": { "value": 160, "density": { "enable": true, "value_area": 800 } },
                "color": { "value": "#00f2ff" },
                "shape": { "type": "circle" },
                "opacity": { "value": 0.7, "random": true },
                "size": { "value": 2, "random": true },
                "line_linked": { "enable": true, "distance": 140, "color": "#00f2ff", "opacity": 0.4, "width": 1 },
                "move": { "enable": true, "speed": 6, "direction": "none", "random": true, "out_mode": "out" }
            },
            "interactivity": {
                "events": { "onhover": { "enable": true, "mode": "grab" } }
            }
        });
    </script>
    """, unsafe_allow_html=True)

# محرك الذكاء الاصطناعي
def call_ai_pro(product):
    api_key = "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"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": f"اكتب استراتيجية تسويقية ذكية لمنتج: {product}"}]
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        return response.json()['choices'][0]['message']['content']
    except: return "⚠️ جاري الاتصال بالمحرك الشعاعي.."

# --- الواجهة ---
# اللوجو يظهر كأنه قطعة من الفيديو
st.markdown(f'<div style="text-align: center; margin-top: -30px;"><img src="https://raw.githubusercontent.com/alhajameer4-del/Python/main/logo.png" style="width: 250px; filter: drop-shadow(0 0 30px #00f2ff);"></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
    product_query = st.text_input("📦 أدخل اسم المنتج لبدء المعالجة النيونية:", placeholder="ساعة ذكية مقاومة للماء")
    if st.button("إطلاق المعالجة الشعاعية ⚡"):
        if product_query:
            with st.spinner('SYSTEM ANALYZING...'):
                result = call_ai_pro(product_query)
                st.markdown(f"<div style='color:#00f2ff; background:rgba(0,0,0,0.9); padding:25px; border:1px solid #00f2ff; border-radius:20px; box-shadow: 0 0 20px #00f2ff; text-shadow: 0 0 5px #00f2ff;'>{result}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- قسم الدفع الكريستالي (مطابق لنهاية الفيديو) ---
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    st.markdown(f"""
        <div class='glass-panel' style='text-align: center;'>
            <h1 style='color: #fff; text-shadow: 0 0 15px #00f2ff; font-family: sans-serif;'>EXECUTIVE PRO</h1>
            <p style='font-size: 4rem; font-weight: 900; color: #00f2ff;'>49$</p>
            <p style='color: #888;'>Premium AI Access & VIP Support</p>
            <a href="mailto:SADAM.ALHAJ007@GMAIL.COM?subject=Upgrade%20to%20PRO" class='checkout-btn'>
                تفعيل العضوية الآن 💎
            </a>
            <p style='color: #000; font-size: 0.1rem;'>v9.0</p>
        </div>
    """, unsafe_allow_html=True)
