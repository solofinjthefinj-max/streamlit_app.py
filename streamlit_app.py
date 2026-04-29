import streamlit as st
import requests

# --- إعدادات الصفحة ---
st.set_page_config(page_title="EcomMind AI", layout="wide")

# تصميم الواجهة CSS المتطور
st.markdown("""
    <style>
    /* الخلفية العامة */
    .main { background-color: #0b0e14; color: #e8eaed; }
    .stApp { background-color: #0b0e14; }
    
    /* العنوان الرئيسي بتأثير شعاعي */
    h1 {
        background: radial-gradient(circle, #00f2ff 0%, #0062ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 3.5rem !important;
        font-weight: 900;
        filter: drop-shadow(0 0 10px rgba(0, 242, 255, 0.5));
    }

    /* كرت إدخال البيانات */
    .glass-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(0, 242, 255, 0.2);
        border-radius: 24px;
        padding: 30px;
        margin-top: 20px;
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.05);
    }

    /* نص الذكاء الاصطناعي المتوهج */
    .ai-response {
        color: #00f2ff; /* اللون الأزرق الشعاعي */
        text-shadow: 0 0 8px rgba(0, 242, 255, 0.8), 0 0 20px rgba(0, 242, 255, 0.4);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.8;
        font-size: 1.1rem;
        background: rgba(0, 242, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border-right: 4px solid #00f2ff;
        direction: rtl;
    }

    /* زر التوليد */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #00f2ff 0%, #0062ff 100%);
        border: none;
        color: white;
        padding: 18px;
        border-radius: 15px;
        font-weight: bold;
        font-size: 1.2rem;
        transition: 0.5s;
        box-shadow: 0 4px 15px rgba(0, 98, 255, 0.3);
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0, 242, 255, 0.5);
    }

    input { background-color: #161b22 !important; color: white !important; border: 1px solid #30363d !important; }
    </style>
    """, unsafe_allow_html=True)

# وظيفة المحرك الذكي
def call_ai(product):
    api_key = "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"
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": "أنت خبير تسويق رقمي. قدم نتائجك بنقاط واضحة ومنظمة جداً."},
            {"role": "user", "content": f"اكتب وصفاً تسويقياً لمنتج: {product}"}
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        return response.json()['choices'][0]['message']['content']
    except:
        return "فشل الاتصال بالمحرك الذكي."

# واجهة المستخدم
st.markdown("<h1>EcomMind AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e; margin-bottom: 30px;'>المحرك الأول لأتمتة مبيعاتك بالذكاء الاصطناعي</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    product_name = st.text_input("📦 اسم المنتج المراد تسويقه")
    if st.button("توليد المحتوى التسويقي ✨"):
        if product_name:
            with st.spinner('جاري البرمجة الشعاعية...'):
                result = call_ai(product_name)
                st.markdown("---")
                # هنا قمنا بتطبيق اللون الأزرق الشعاعي المتوهج
                st.markdown(f"<div class='ai-response'>{result}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# تذييل الصفحة (بياناتك)
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown(f"""
    <div style='text-align: center; padding: 20px; border-top: 1px solid rgba(0,242,255,0.1);'>
        <p style='color: #8b949e;'>حقوق الملكية © 2024 - EcomMind AI Pro</p>
        <p style='color: #00f2ff; font-weight: bold;'>للاشتراك: SADAM.ALHAJ007@GMAIL.COM</p>
    </div>
""", unsafe_allow_html=True)
