import streamlit as st
import requests

# --- إعدادات الصفحة الفنية ---
st.set_page_config(page_title="EcomMind AI Pro", layout="wide")

# --- الهندسة البصرية المتقدمة (CSS) لمحاكاة الفيديو الإعلاني ---
st.markdown("""
    <style>
    /* 1. خلفية الفضاء الرقمي والجزيئات (مثل بداية الفيديو) */
    .stApp {
        background: #000000;
        background-image: 
            radial-gradient(circle at 50% 50%, rgba(0, 242, 255, 0.1) 0%, transparent 80%),
            url('https://www.transparenttextures.com/patterns/stardust.png');
        background-attachment: fixed;
    }

    /* 2. شعار الدماغ والسلة (اللوجو المشع) */
    .logo-container {
        text-align: center;
        margin-top: -50px;
        padding-bottom: 20px;
    }
    .logo-img {
        width: 280px;
        filter: drop-shadow(0 0 25px #00f2ff); /* توهج ليزري حاد */
        animation: pulse 3s infinite ease-in-out;
    }
    @keyframes pulse {
        0% { filter: drop-shadow(0 0 15px #00f2ff); transform: scale(1); }
        50% { filter: drop-shadow(0 0 35px #00f2ff); transform: scale(1.02); }
        100% { filter: drop-shadow(0 0 15px #00f2ff); transform: scale(1); }
    }

    /* 3. خانة البحث المتوهجة (مثل لقطة الفيديو 0:05) */
    div[data-baseweb="input"] {
        background-color: rgba(0, 5, 10, 0.9) !important;
        border: 2px solid #00f2ff !important;
        border-radius: 20px !important;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.4) !important;
        transition: 0.4s;
    }
    div[data-baseweb="input"]:focus-within {
        box-shadow: 0 0 40px #00f2ff !important;
    }
    input {
        color: #00f2ff !important;
        font-weight: bold !important;
        font-size: 1.3rem !important;
        text-shadow: 0 0 5px #00f2ff;
    }

    /* 4. زر التوليد النيوني (مثل زر Generate في الفيديو) */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #00f2ff, #0062ff) !important;
        color: white !important;
        font-weight: 900 !important;
        border: none !important;
        border-radius: 15px !important;
        height: 65px;
        font-size: 1.4rem !important;
        box-shadow: 0 0 20px #00f2ff;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    .stButton>button:hover {
        box-shadow: 0 0 50px #00f2ff;
        transform: translateY(-2px);
    }

    /* 5. نتائج الذكاء الاصطناعي (مربع شعاعي) */
    .result-box {
        background: rgba(0, 10, 20, 0.9);
        border: 2px solid #00f2ff;
        color: #00f2ff;
        padding: 30px;
        border-radius: 25px;
        box-shadow: 0 0 30px rgba(0, 242, 255, 0.2);
        line-height: 1.8;
        font-size: 1.1rem;
        text-shadow: 0 0 2px #00f2ff;
        direction: rtl;
    }

    /* 6. نافذة الاشتراك (الكريستال الأزرق من الفيديو) */
    .premium-card {
        background: rgba(0, 100, 255, 0.05);
        backdrop-filter: blur(25px);
        border: 3px solid #00f2ff;
        border-radius: 40px;
        padding: 50px;
        text-align: center;
        box-shadow: 0 0 60px rgba(0, 242, 255, 0.3);
        margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- استدعاء المحرك الذكي (تم إصلاح منطق البحث) ---
def call_ai_pro(product):
    # مفتاحك الخاص مدمج هنا
    api_key = "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"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "أنت خبير تسويق ذكي جداً. اكتب وصفاً بيعياً مذهلاً لمنتج العميل يتضمن: وصف AIDA، كلمات SEO، وفكرة إعلان فيديو."},
            {"role": "user", "content": product}
        ],
        "temperature": 0.7
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return f"⚠️ خطأ فني (كود {response.status_code}): يرجى إعادة المحاولة."
    except Exception as e:
        return "⚠️ المحرك يمر بتحديث سريع.. يرجى الضغط على زر التوليد مجدداً."

# --- واجهة المستخدم الرئيسية ---

# عرض اللوجو المدمج (تأكد من رفعه باسم logo.png)
st.markdown(f"""
    <div class="logo-container">
        <img src="https://raw.githubusercontent.com/alhajameer4-del/Python/main/logo.png" class="logo-img">
    </div>
""", unsafe_allow_html=True)

# منطقة الإدخال
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    product_query = st.text_input("📦 أدخل اسم المنتج لبدء المعالجة النيونية", placeholder="مثلاً: ساعة ذكية مقاومة للماء")
    
    if st.button("توليد الإبداع الشعاعي ⚡"):
        if product_query:
            with st.spinner('SYSTEM ANALYZING...'):
                result = call_ai_pro(product_query)
                st.markdown(f"<div class='result-box'>{result}</div>", unsafe_allow_html=True)
        else:
            st.warning("يرجى كتابة اسم المنتج أولاً.")

# --- نافذة الاشتراك (نفس شكل الفيديو الختامي) ---
st.markdown("<br><br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    st.markdown(f"""
        <div class='premium-card'>
            <h1 style='color: #fff; text-shadow: 0 0 15px #00f2ff;'>PREMIUM MEMBERSHIP</h1>
            <p style='font-size: 3.5rem; font-weight: 900; color: #00f2ff;'>49$ <small style='font-size: 1rem; color: #fff;'>/ Monthly</small></p>
            <div style='background: rgba(0,0,0,0.6); padding: 25px; border-radius: 20px; border: 1px solid #00f2ff; margin: 25px 0;'>
                <p style='color: #00f2ff; margin-bottom: 5px; font-weight: bold;'>PAYONEER ID:</p>
                <p style='font-size: 1.2rem; font-weight: bold; color: #fff;'>SADAM.ALHAJ007@GMAIL.COM</p>
                <p style='color: #34a853; margin-top: 20px; font-weight: bold;'>USDT WALLET (TRC20):</p>
                <p style='font-size: 0.8rem; color: #fff; word-break: break-all;'>TKCvNEvz59717dp5QZbrwCqCzTQqjrNxCX</p>
            </div>
            <a href="mailto:SADAM.ALHAJ007@GMAIL.COM" style='text-decoration: none;'>
                <div style='background: #00f2ff; color: #000; padding: 15px; border-radius: 12px; font-weight: bold;'>تفعيل العضوية الآن 💎</div>
            </a>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: #333;'>SADAM AL-HAJ AI LABS v4.0</p>", unsafe_allow_html=True)
