import random
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="K-dairies 🌸", page_icon="🌸", layout="centered"
)

# 2. Custom Aesthetic Styling (Pink Theme)
st.markdown(
    """
    <style>
    :root {
        --primary-color: #f472b6 !important;
        --background-color: #fff0f5 !important;
        --secondary-background-color: #ffffff !important;
        --text-color: #9f1239 !important;
    }

    .stApp {
        background-color: #fff0f5 !important;
    }
    
    .main-title {
        color: #9f1239 !important;
        font-size: 40px !important;
        font-weight: 800 !important;
        margin-bottom: 2px !important;
        font-family: 'Segoe UI', sans-serif !important;
    }

    .main-subtitle {
        color: #be123c !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        margin-bottom: 20px !important;
    }

    /* Flashcard / Content Container */
    .content-box {
        background-color: #ffffff !important;
        border-radius: 24px !important;
        padding: 25px !important;
        border: 2px solid #f472b6 !important;
        box-shadow: 0px 10px 25px rgba(244, 114, 182, 0.15) !important;
        margin-bottom: 20px !important;
    }

    .korean-text {
        font-size: 42px !important;
        font-weight: bold !important;
        color: #db2777 !important;
        margin-top: 10px !important;
        text-align: center !important;
    }

    .card-subtitle {
        color: #f472b6 !important;
        font-size: 14px !important;
        font-weight: 600 !important;
        letter-spacing: 1px !important;
        text-align: center !important;
    }

    /* Hangul Custom Formatting */
    .hangul-char {
        display: inline-block;
        background-color: #fce7f3;
        color: #be123c;
        font-weight: bold;
        font-size: 20px;
        padding: 4px 12px;
        border-radius: 10px;
        border: 1px solid #f472b6;
        min-width: 45px;
        text-align: center;
    }

    .hangul-sound {
        color: #881337;
        font-weight: 600;
        font-size: 16px;
        margin-left: 10px;
    }

    .hangul-row {
        margin-bottom: 12px;
        display: flex;
        align-items: center;
    }

    /* Tabs Styling */
    button[data-baseweb="tab"] p {
        color: #9f1239 !important;
        font-weight: 700 !important;
        font-size: 16px !important;
    }

    /* Labels & Input styling */
    label, label p, label span {
        color: #9f1239 !important;
        font-size: 18px !important;
        font-weight: 700 !important;
    }

    div[data-baseweb="input"] {
        background-color: #ffffff !important;
        border-radius: 14px !important;
        border: 2px solid #f472b6 !important;
    }

    div[data-baseweb="input"] input {
        color: #881337 !important;
    }

    /* Pink Buttons */
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
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #ffe4e6 !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 3. Sidebar Navigation
st.sidebar.title("🌸 K-dairies Menu")
page = st.sidebar.radio(
    "Go to:",
    ["✨ Intro & Welcome", "🔤 Learn Hangul", "🎴 Vocab Practice"]
)

# -------------------------------------------------------------
# PAGE 1: INTRO & WELCOME
# -------------------------------------------------------------
if page == "✨ Intro & Welcome":
    st.markdown('<div class="main-title">🌸 Welcome to K-dairies</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Your aesthetic daily Korean learning space ✨</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="content-box">
            <h3 style="color: #9f1239; margin-top:0;">🎀 Ready to start learning?</h3>
            <p style="color: #4c0519; font-size: 16px; line-height: 1.6;">
                Welcome to your personal Korean learning diary! Learning a new language is an exciting journey, and the best way to begin is by mastering the basics step-by-step.
            </p>
            <p style="color: #4c0519; font-size: 16px; line-height: 1.6;">
                <b>How to use this app:</b><br>
                1. 🔤 Use the sidebar to go to <b>Learn Hangul</b> and master the basic characters.<br>
                2. 🎴 Switch to <b>Vocab Practice</b> to test your memory with interactive flashcards!
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------------------------------------------------
# PAGE 2: LEARN HANGUL
# -------------------------------------------------------------
elif page == "🔤 Learn Hangul":
    st.markdown('<div class="main-title">🔤 Basic Hangul (한글)</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Master the Korean alphabet consonants & vowels ✨</div>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["Consonants (자음)", "Vowels (모음)"])

    with tab1:
        st.markdown("<h3 style='color: #9f1239;'>📌 Basic Consonants</h3>", unsafe_allow_html=True)
        consonants = {
            "ㄱ": "g / k",
            "ㄴ": "n",
            "ㄷ": "d / t",
            "ㄹ": "r / l",
            "ㅁ": "m",
            "ㅂ": "b / p",
            "ㅅ": "s",
            "ㅇ": "silent (at start) / ng (at end)",
            "ㅈ": "j",
            "ㅊ": "ch",
            "ㅋ": "k",
            "ㅌ": "t",
            "ㅍ": "p",
            "ㅎ": "h"
        }
        
        html_content = '<div class="content-box">'
        for char, sound in consonants.items():
            html_content += f'''
            <div class="hangul-row">
                <span class="hangul-char">{char}</span>
                <span class="hangul-sound">Sounds like: <b>{sound}</b></span>
            </div>
            '''
        html_content += '</div>'
        st.markdown(html_content, unsafe_allow_html=True)

    with tab2:
        st.markdown("<h3 style='color: #9f1239;'>📌 Basic Vowels</h3>", unsafe_allow_html=True)
        vowels = {
            "ㅏ": "a (like 'ah')",
            "ㅑ": "ya",
            "ㅓ": "eo (like 'uh')",
            "ㅕ": "yeo",
            "ㅗ": "o (like 'oh')",
            "ㅛ": "yo",
            "ㅜ": "u (like 'oo')",
            "ㅠ": "yu",
            "ㅡ": "eu (like 'u' in 'pull')",
            "ㅣ": "i (like 'ee')"
        }
        
        html_content = '<div class="content-box">'
        for char, sound in vowels.items():
            html_content += f'''
            <div class="hangul-row">
                <span class="hangul-char">{char}</span>
                <span class="hangul-sound">Sounds like: <b>{sound}</b></span>
            </div>
            '''
        html_content += '</div>'
        st.markdown(html_content, unsafe_allow_html=True)

# -------------------------------------------------------------
# PAGE 3: VOCAB PRACTICE
# -------------------------------------------------------------
elif page == "🎴 Vocab Practice":
    st.markdown('<div class="main-title">🎴 Vocab Practice</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Test your memory on basic phrases ✨</div>', unsafe_allow_html=True)

    vocab = {
        "안녕하세요 (Annyeonghaseyo)": "hello",
        "감사합니다 (Gamsahamnida)": "thank you",
        "네 (Ne)": "yes",
        "아니요 (Aniyo)": "no",
        "죄송합니다 (Joesonghamnida)": "sorry",
    }

    if "word" not in st.session_state:
        st.session_state.word = random.choice(list(vocab.keys()))

    current_word = st.session_state.word
    correct_answer = vocab[current_word]

    st.markdown(
        f"""
        <div class="content-box">
            <p class="card-subtitle">WHAT DOES THIS MEAN?</p>
            <div class="korean-text">{current_word}</div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    user_answer = st.text_input("Type ur answer in English:", placeholder="e.g. hello")

    col1, col2 = st.columns(2)

    with col1:
        check_btn = st.button("💖 Check Answer", use_container_width=True)

    with col2:
        next_btn = st.button("🎀 Next Word", use_container_width=True)

    if check_btn:
        if user_answer.strip().lower() == correct_answer.lower():
            st.balloons()
            st.success("🌸 Spot on! Absolutely perfect!")
        else:
            st.error(f"💕 Close! The correct answer is: **{correct_answer}**")

    if next_btn:
        del st.session_state.word
        st.rerun()
