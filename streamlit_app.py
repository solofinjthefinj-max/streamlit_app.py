import streamlit as st
import requests

# --- إعدادات الصفحة ---
st.set_page_config(page_title="EcomMind AI", layout="wide")

# تصميم الواجهة (CSS)
st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #e8eaed; }
    .stApp { background-color: #0b0e14; }
    h1 { background: linear-gradient(90deg, #4285f4, #9b72cb, #d96570); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align: center; font-size: 3rem !important; font-weight: 800; }
    .glass-card { background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; margin-top: 20px; }
    .stButton>button { width: 100%; background: linear-gradient(90deg, #4285f4, #1a73e8); border: none; color: white; padding: 15px; border-radius: 12px; font-weight: bold; }
    input { background-color: #1a1d23 !important; color: white !important; border-radius: 10px !important; }
    </style>
    """, unsafe_allow_html=True)

# وظيفة الذكاء الاصطناعي
def call_ai(product):
    api_key = "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"
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # استخدمنا نموذج llama-3.1-8b-instant لأنه الأحدث والأكثر استقراراً
    payload = {
        "model": "llama-3.1-8b-instant", 
        "messages": [
            {"role": "system", "content": "أنت خبير تسويق إلكتروني محترف تكتب باللغة العربية بلهجة بيعية جذابة."},
            {"role": "user", "content": f"اكتب وصفاً تسويقياً كاملاً لمنتج: {product} يتضمن مميزات، كلمات SEO، وفكرة إعلان فيديو."}
        ],
        "temperature": 0.7
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return f"خطأ من المصدر: يرجى التأكد من تفعيل الـ API Key الخاص بك (كود الخطأ: {response.status_code})"
    except Exception as e:
        return "عذراً، حدث خطأ في الاتصال بالمحرك. تأكد من جودة الإنترنت."

# محتوى الموقع
st.markdown("<h1>EcomMind AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9aa0a6;'>أتمتة تسويق متجرك بذكاء عالمي</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    product_name = st.text_input("📦 أدخل اسم المنتج")
    if st.button("توليد المحتوى ✨"):
        if product_name:
            with st.spinner('جاري التحليل...'):
                result = call_ai(product_name)
                st.markdown("---")
                st.markdown("### 📋 النتائج المقترحة:")
                st.write(result)
        else:
            st.warning("يرجى كتابة اسم المنتج")
    st.markdown("</div>", unsafe_allow_html=True)

# قسم الدفع والاشتراك
st.markdown("<br><br><h3 style='text-align: center;'>خطة العضوية الاحترافية (PRO)</h3>", unsafe_allow_html=True)
st.markdown(f"""
    <div style='max-width: 500px; margin: auto; padding: 20px; border: 1px solid #4285f4; border-radius: 15px; text-align: center; background: rgba(66, 133, 244, 0.05);'>
        <p style='font-size: 1.5rem; font-weight: bold;'>49$ شهرياً</p>
        <p style='color: #9aa0a6; font-size: 0.9rem;'>بايونير: SADAM.ALHAJ007@GMAIL.COM</p>
        <p style='color: #34a853; font-size: 0.8rem;'>USDT: TKCvNEvz59717dp5QZbrwCqCzTQqjrNxCX</p>
        <a href='mailto:SADAM.ALHAJ007@GMAIL.COM' style='text-decoration: none;'><button style='background: #4285f4; color: white; border: none; padding: 10px 20px; border-radius: 8px; cursor: pointer; margin-top: 10px;'>إرسال إيصال الدفع</button></a>
    </div>
""", unsafe_allow_html=True)
