import streamlit as st
import requests

# --- إعدادات الصفحة ---
st.set_page_config(page_title="EcomMind AI Ultra Pro", layout="wide")

# --- التصميم المتكامل (CSS) ---
st.markdown("""
    <style>
    /* 1. الخلفية التقنية (أيقونات ذكاء اصطناعي ورموز إلكترونية) */
    .stApp {
        background: linear-gradient(rgba(5, 7, 10, 0.8), rgba(5, 7, 10, 0.9)), 
        url('https://www.transparenttextures.com/patterns/carbon-fibre.png'),
        url('https://img.freepik.com/free-vector/artificial-intelligence-icon-set_53876-115911.jpg?t=st=1715424564~exp=1715428164~hmac=02e605d83637e199d6515f4e0c8b6b0b5e5e6e6e6e6e6e6e6e6e6e6e6e6e6e');
        background-blend-mode: overlay;
        background-color: #05070a;
        background-size: cover;
        background-attachment: fixed;
    }

    /* 2. العنوان النيوني الصارخ */
    .neon-title {
        color: #00f2ff;
        text-align: center;
        font-size: 4rem !important;
        font-weight: 900;
        text-shadow: 0 0 20px #00f2ff, 0 0 40px #0062ff;
        font-family: 'Courier New', Courier, monospace;
    }

    /* 3. الحل الجذري والنهائي لخانة الكتابة (تحويلها لأسود نيوني) */
    .stTextInput > div > div {
        background-color: rgba(0, 5, 10, 0.9) !important;
        border: 2px solid #00f2ff !important;
        border-radius: 15px !important;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.4) !important;
    }
    .stTextInput input {
        color: #00f2ff !important;
        background-color: transparent !important;
        font-size: 1.3rem !important;
        font-weight: bold !important;
        padding: 15px !important;
    }
    
    /* إخفاء أي خلفية بيضاء تظهر عند النقر */
