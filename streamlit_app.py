import streamlit as st
import requests

# --- 1. إعدادات الصفحة الأساسية لإزالة القوائم الافتراضية ---
st.set_page_config(page_title="EcomMind AI Pro", layout="wide", initial_sidebar_state="collapsed")

# --- 2. الهندسة البصرية (CSS) مطابقة للصورة 100% ---
st.markdown("""
    <style>
    /* إخفاء شريط سترمليت العلوي */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}

    /* الخلفية الفضائية العميقة */
    .stApp {
        background-color: #000000 !important;
        background-image: radial-gradient(circle at center, #001a33 0%, #000000 80%) !important;
    }

    #particles-js {
        position: fixed;
        width: 100vw;
        height: 100vh;
        top: 0;
        left: 0;
        z-index: -1;
    }

    /* تصميم خانة البحث (مثل الصورة تماماً) */
    div[data-baseweb="input"] {
        background-color: #000000 !important;
        border: 2px solid #00f2ff !important;
        border-radius: 50px !important; /* شكل بيضاوي مثل الصورة */
        box-shadow: 0 0 20px #00f2ff, inset 0 0 10px rgba(0, 242, 255, 0.5) !important;
        height: 70px !important;
        padding: 0 20px !important;
        transition: 0.3s;
    }
    
    input {
        color: #00f2ff !important;
        background-color: transparent !important;
        -webkit-text-fill-color: #00f2ff !important;
        font-size: 1.5rem !important;
        font-weight: bold !important;
        text-align: center !important;
        border: none !important;
        margin-top: 10px !important;
    }

    /* زر التوليد النيوني الحاد */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #00f2ff, #0062ff) !important;
        color: #000 !important; /* نص أسود ليكون حاداً */
        font-weight: 900 !important;
        border-radius: 50px !important;
        height: 60px !important;
        border: none !important;
        box-shadow: 0 0 25px #00f2ff !important;
        font-size: 1.2rem !important;
        margin-top: 20px !important;
    }

    /* صندوق النتائج الزجاجي */
    .result-box {
        background: rgba(0, 15, 30, 0.9);
        border: 2px solid #00f2ff;
        color: #00f2ff;
        padding: 30px;
        border-radius: 25px;
        margin-top: 30px;
        box-shadow: 0 0 30px rgba(0, 242, 255, 0.3);
        direction: rtl;
        font-size: 1.2rem;
        line-height: 1.8;
    }

    /* نافذة الاشتراك (الكريستال الأزرق) */
    .premium-panel {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        border: 2px solid rgba(0, 242, 255, 0.4);
        border-radius: 40px;
        padding: 40px;
        text-align: center;
        box-shadow: 0 0 50px rgba(0, 0, 0, 0.5);
    }

    .checkout-link {
        background: #00f2ff;
        color: #000 !important;
        padding: 15px 40px;
        border-radius: 50px;
        font-weight: 900;
        text-decoration: none;
        box-shadow: 0 0 20px #00f2ff;
        display: inline-block;
        margin-top: 20px;
    }
    </style>

    <!-- محرك الجزيئات المشعة (خلفية الفيديو) -->
    <div id="particles-js"></div>
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
        particlesJS('particles-js', {
            "particles": {
                "number": { "value": 200 },
                "color": { "value": "#00f2ff" },
                "shape": { "type": "circle" },
                "opacity": { "value": 0.8, "random": true },
                "size": { "value": 2 },
                "line_linked": { "enable": true, "distance": 120, "color": "#00f2ff", "opacity": 0.3 },
                "move": { "enable": true, "speed": 8, "direction": "none", "random": true, "out_mode": "out" }
            }
        });
    </script>
""", unsafe_allow_html=True)

# --- 3. محرك البحث الذكي (تم إصلاح منطق الاستجابة) ---
def get_ai_response(text):
    api_key = "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"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": f"أنت خبير تسويق محترف. اكتب وصفاً بيعياً مذهلاً لمنتج: {text}"}],
        "temperature": 0.7
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=20)
        return response.json()['choices'][0]['message']['content']
    except:
        return "⚠️ النظام متصل.. جاري إعادة المحاولة خلال ثوانٍ."

# --- 4. واجهة المستخدم ---
# اللوجو
st.markdown(f'<div style="text-align: center; margin-bottom: 20px;"><img src="https://raw.githubusercontent.com/alhajameer4-del/Python/main/logo.png" style="width: 250px; filter: drop-shadow(0 0 20px #00f2ff);"></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # المدخلات
    product_name = st.text_input("", placeholder="أدخل اسم المنتج هنا...")
    
    if st.button("توليد الإبداع الشعاعي ⚡"):
        if product_name:
            with st.spinner('جاري التحليل النيوني...'):
                ans = get_ai_response(product_name)
                st.markdown(f"<div class='result-box'>{ans}</div>", unsafe_allow_html=True)

# --- 5. قسم الاشتراك (نهاية الفيديو) ---
st.markdown("<br><br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    st.markdown(f"""
        <div class='premium-panel'>
            <h2 style='color: #fff;'>EXECUTIVE PRO</h2>
            <p style='font-size: 3.5rem; font-weight: 900; color: #00f2ff; margin:0;'>49$</p>
            <p style='color: #888;'>Premium AI Access & VIP Direct Support</p>
            <a href="mailto:SADAM.ALHAJ007@GMAIL.COM?subject=Upgrade%20to%20PRO" class='checkout-link'>
                الذهاب للدفع الآمن 🔒
            </a>
        </div>
    """, unsafe_allow_html=True)
