import streamlit as st
import requests

# --- إعدادات الصفحة ---
st.set_page_config(page_title="EcomMind AI Pro", layout="wide")

# --- الهندسة البصرية المتقدمة (CSS) ---
st.markdown("""
    <style>
    .stApp {
        background: #000000;
        background-image: radial-gradient(circle at center, rgba(0, 242, 255, 0.1) 0%, transparent 80%);
    }

    /* اللوجو */
    .logo-container { text-align: center; margin-top: -50px; padding-bottom: 20px; }
    .logo-img { width: 280px; filter: drop-shadow(0 0 20px #00f2ff); }

    /* خانة البحث المتوهجة (إجبار اللون الداكن) */
    div[data-baseweb="input"] {
        background-color: rgba(0, 5, 10, 0.95) !important;
        border: 2px solid #00f2ff !important;
        border-radius: 20px !important;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.3) !important;
    }
    input { color: #00f2ff !important; font-weight: bold !important; font-size: 1.2rem !important; }

    /* أزرار التشغيل النيونية */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #00f2ff, #0062ff) !important;
        color: white !important;
        font-weight: 900 !important;
        border: none !important;
        border-radius: 15px !important;
        height: 60px;
        box-shadow: 0 0 15px #00f2ff;
    }

    /* نافذة الاشتراك الكريستالية */
    .premium-card {
        background: rgba(0, 5, 10, 0.8);
        backdrop-filter: blur(20px);
        border: 2px solid #00f2ff;
        border-radius: 40px;
        padding: 40px;
        text-align: center;
        box-shadow: 0 0 50px rgba(0, 242, 255, 0.2);
        margin-top: 50px;
    }

    /* زر الدفع المخفي */
    .checkout-btn {
        background: #00f2ff;
        color: #000 !important;
        padding: 18px 40px;
        border-radius: 15px;
        font-weight: 900;
        font-size: 1.3rem;
        text-decoration: none;
        display: inline-block;
        transition: 0.4s;
        box-shadow: 0 0 25px #00f2ff;
        margin-top: 20px;
    }
    .checkout-btn:hover { background: #fff; box-shadow: 0 0 40px #fff; transform: scale(1.05); }

    .result-box {
        background: rgba(0, 10, 20, 0.9);
        border: 2px solid #00f2ff;
        color: #00f2ff;
        padding: 25px;
        border-radius: 20px;
        margin-top: 20px;
        direction: rtl;
    }
    </style>
    """, unsafe_allow_html=True)

# استدعاء المحرك الذكي
def call_ai_pro(product):
    api_key = "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"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": f"اكتب وصفاً تسويقياً لمنتج: {product}"}]
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        return response.json()['choices'][0]['message']['content']
    except: return "⚠️ جاري تهيئة المحرك النيوني.. حاول مجدداً."

# --- الواجهة ---
st.markdown(f'<div class="logo-container"><img src="https://raw.githubusercontent.com/alhajameer4-del/Python/main/logo.png" class="logo-img"></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    product_query = st.text_input("📦 اسم المنتج المراد تسويقه بذكاء:", placeholder="ساعة ذكية مقاومة للماء")
    if st.button("إطلاق المعالجة الشعاعية ✨"):
        if product_query:
            with st.spinner('SYSTEM ANALYZING...'):
                result = call_ai_pro(product_query)
                st.markdown(f"<div class='result-box'>{result}</div>", unsafe_allow_html=True)

# --- قسم الدفع المخفي ---
st.markdown("<br><br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    st.markdown(f"""
        <div class='premium-card'>
            <h1 style='color: #fff; text-shadow: 0 0 15px #00f2ff;'>EXECUTIVE PRO</h1>
            <p style='font-size: 3rem; font-weight: 900; color: #00f2ff;'>49$ <small style='font-size: 1rem; color: #fff;'>/ Monthly</small></p>
            <p style='color: #888;'>وصول كامل لمحرك الذكاء الاصطناعي مع دعم فني مخصص</p>
            
            <!-- زر الدفع الذي ينقل العميل للإيميل لطلب الفاتورة دون رؤية الحسابات فوراً -->
            <a href="mailto:SADAM.ALHAJ007@GMAIL.COM?subject=طلب تفعيل عضوية EcomMind AI PRO&body=مرحباً صدام، أريد تفعيل العضوية الاحترافية. يرجى تزويدي برابط الدفع." class='checkout-btn'>
                الذهاب للدفع الآمن 🔒
            </a>
            
            <p style='font-size: 0.7rem; color: #333; margin-top: 15px;'>تحصيل آمن عبر بايونير و USDT</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: #222;'>POWERED BY SADAM AL-HAJ AI LABS v5.0</p>", unsafe_allow_html=True)
