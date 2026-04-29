import streamlit as st
import requests
import json

# --- إعدادات الهوية البصرية (Google AI Design) ---
st.set_page_config(page_title="EcomMind AI | المحرك الذكي", layout="wide")

# تصميم الواجهة CSS
st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #e8eaed; font-family: 'Inter', sans-serif; }
    .stApp { background-color: #0b0e14; }
    .gradient-text {
        background: linear-gradient(90deg, #4285f4, #9b72cb, #d96570);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 3rem;
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 30px;
        margin: 10px 0;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #4285f4, #1a73e8);
        border: none;
        color: white;
        padding: 18px;
        border-radius: 15px;
        font-weight: bold;
        font-size: 1.1rem;
        transition: 0.4s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 10px 25px rgba(66, 133, 244, 0.4);
    }
    input { background-color: #1a1d23 !important; color: white !important; border-radius: 12px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- وظيفة الربط مع الذكاء الاصطناعي (Groq) ---
def call_ai_engine(product_input):
    api_key = "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" # مفتاحك مدمج هنا
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": f"أنت خبير تسويق. اكتب وصفاً بيعياً احترافياً لمنتج: {product_input} يتضمن: وصف جذاب، كلمات SEO، وفكرة فيديو تيك توك."}],
        "temperature": 0.7
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()['choices'][0]['message']['content']
    except:
        return "عذراً، المحرك مشغول حالياً. يرجى المحاولة بعد قليل."

# --- واجهة المستخدم ---
st.markdown("<div style='text-align: center; padding: 40px 0;'>", unsafe_allow_html=True)
st.markdown("<h1 class='gradient-text'>EcomMind AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #9aa0a6; font-size: 1.2rem;'>أتمتة تسويق المتاجر الإلكترونية بضغطة زر</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    product_name = st.text_input("📦 ما هو المنتج الذي تبيعه؟", placeholder="مثلاً: سماعات لاسلكية")
    if st.button("توليد المحتوى التسويقي ✨"):
        if product_name:
            with st.spinner('جاري التحليل...'):
                result = call_ai_engine(product_name)
                st.markdown("### 📋 النتائج الذكية:")
                st.info(result)
        else:
            st.error("يرجى كتابة اسم المنتج أولاً.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- قسم الدفع (بياناتك المدمجة) ---
st.markdown("<br><br><h2 style='text-align: center;'>الترقية للنسخة الاحترافية (PRO)</h2>", unsafe_allow_html=True)
p_col1, p_col2, p_col3 = st.columns([1, 1.5, 1])
with p_col2:
    st.markdown(f"""
        <div class='glass-card' style='border: 2px solid #4285f4; text-align: center;'>
            <h3 style='color: #4285f4;'>اشتراك العضوية الكاملة</h3>
            <p style='font-size: 2.5rem; font-weight: bold;'>49$ <small style='font-size: 0.8rem;'>شهرياً</small></p>
            <div style='text-align: right; margin: 20px 0; font-size: 0.9rem;'>
                <p>✅ محتوى غير محدود للمنتجات</p>
                <p>✅ أفكار حملات إعلانية يومية</p>
                <p>✅ دعم خاص للتجار</p>
            </div>
            <div style='background: rgba(66, 133, 244, 0.1); padding: 15px; border-radius: 12px;'>
                <p style='font-size: 0.8rem; margin-bottom: 5px;'>الدفع عبر بايونير (Payoneer):</p>
                <p style='color: #4285f4; font-weight: bold;'>SADAM.ALHAJ007@GMAIL.COM</p>
                <p style='font-size: 0.8rem; margin: 10px 0 5px 0;'>المحفظة الرقمية (USDT - TRC20):</p>
                <p style='color: #34a853; font-size: 0.7rem; word-break: break-all;'>TKCvNEvz59717dp5QZbrwCqCzTQqjrNxCX</p>
            </div>
            <a href="mailto:SADAM.ALHAJ007@GMAIL.COM" style='text-decoration: none;'>
                <button style='margin-top: 20px; width: 100%; padding: 12px; background: #34a853; border: none; border-radius: 8px; color: white; font-weight: bold;'>تأكيد الدفع وإرسال الإيصال</button>
            </a>
        </div>
    """, unsafe_allow_html=True)
