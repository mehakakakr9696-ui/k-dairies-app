import random
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="K-dairies 🌸", page_icon="🌸", layout="centered"
)

# 2. Custom Aesthetic Styling (Forces Light Pink Theme Everywhere)
st.markdown(
    """
    <style>
    /* 🌸 Overriding Streamlit's Base Theme Variables */
    :root {
        --primary-color: #f472b6 !important;
        --background-color: #fff0f5 !important;
        --secondary-background-color: #ffffff !important;
        --text-color: #9f1239 !important;
    }

    /* Main Page Background */
    .stApp {
        background-color: #fff0f5 !important;
    }
    
    /* Cherry Red Title */
    .main-title {
        color: #9f1239 !important;
        font-size: 42px !important;
        font-weight: 800 !important;
        margin-bottom: 2px !important;
        font-family: 'Segoe UI', sans-serif !important;
    }

    /* Dark Berry Subtitle */
    .main-subtitle {
        color: #be123c !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        margin-bottom: 25px !important;
    }

    /* Flashcard Container */
    .flashcard-box {
        background-color: #ffffff !important;
        border-radius: 24px !important;
        padding: 35px !important;
        text-align: center !important;
        border: 2px solid #f472b6 !important;
        box-shadow: 0px 12px 30px rgba(244, 114, 182, 0.2) !important;
        margin-bottom: 25px !important;
    }
    
    .korean-text {
        font-size: 44px !important;
        font-weight: bold !important;
        color: #db2777 !important;
        margin-top: 10px !important;
    }

    .card-subtitle {
        color: #f472b6 !important;
        font-size: 15px !important;
        font-weight: 600 !important;
        letter-spacing: 1px !important;
        margin: 0 !important;
    }

    /* 💖 FORCE ALL LABELS ("type ur answer...") TO CHERRY RED */
    label, label p, label span {
        color: #9f1239 !important;
        font-size: 18px !important;
        font-weight: 700 !important;
    }

    /* 💖 FORCE INPUT BOX TO WHITE WITH PINK BORDER */
    input {
        background-color: #ffffff !important;
        color: #881337 !important;
        border: 2px solid #f472b6 !important;
        border-radius: 14px !important;
        font-weight: 600 !important;
    }

    /* Input Box Wrapper */
    div[data-baseweb="input"] {
        background-color: #ffffff !important;
        border-radius: 14px !important;
        border: 2px solid #f472b6 !important;
    }

    /* 💖 FORCE BUTTONS TO ROSY PINK */
    button, div.stButton > button {
        background-color: #f472b6 !important;
        color: #ffffff !important;
        border-radius: 16px !important;
        border: none !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        box-shadow: 0px 4px 12px rgba(244, 114, 182, 0.3) !important;
    }

    button:hover, div.stButton > button:hover {
        background-color: #db2777 !important;
        color: #ffffff !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 3. Header & Subtitle
st.markdown('<div class="main-title">🌸 K-dairies</div>', unsafe_allow_html=True)
st.markdown('<div class="main-subtitle">✨ practice ur daily korean vocabulary in style ✨</div>', unsafe_allow_html=True)

# 4. Vocabulary Dictionary
vocab = {
    "안녕하세요 (Annyeonghaseyo)": "hello",
    "감사합니다 (Gamsahamnida)": "thank you",
    "네 (Ne)": "yes",
    "아니요 (Aniyo)": "no",
    "죄송합니다 (Joesonghamnida)": "sorry",
}

# 5. Pick and store current word
if "word" not in st.session_state:
    st.session_state.word = random.choice(list(vocab.keys()))

current_word = st.session_state.word
correct_answer = vocab[current_word]

# 6. Flashcard Display
st.markdown(
    f"""
    <div class="flashcard-box">
        <p class="card-subtitle">WHAT DOES THIS MEAN?</p>
        <div class="korean-text">{current_word}</div>
    </div>
""",
    unsafe_allow_html=True,
)

# 7. Text Input & Buttons
user_answer = st.text_input("Type ur answer in English:", placeholder="e.g. hello")

col1, col2 = st.columns(2)

with col1:
    check_btn = st.button("💖 Check Answer", use_container_width=True)

with col2:
    next_btn = st.button("🎀 Next Word", use_container_width=True)

# 8. Interactive Logic
if check_btn:
    if user_answer.strip().lower() == correct_answer.lower():
        st.balloons()
        st.success("🌸 Spot on! Absolutely perfect!")
    else:
        st.error(f"💕 Close! The correct answer is: **{correct_answer}**")

if next_btn:
    del st.session_state.word
    st.rerun()