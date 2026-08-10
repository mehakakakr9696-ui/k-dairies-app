import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(page_title="K-dairies | Hangul Practice", page_icon="🌸", layout="centered")

# Visual Styling fix for readable text across Light/Dark modes
st.markdown("""
    <style>
    .hangul-box {
        background-color: #2b2b2b;
        color: #ffffff !important;
        padding: 16px;
        border-radius: 12px;
        border: 2px solid #ffb6c1;
        text-align: center;
        margin-bottom: 12px;
    }
    .hangul-char {
        font-size: 42px;
        font-weight: bold;
        color: #ffb6c1 !important;
        margin: 0;
    }
    .sound-text {
        color: #e0e0e0 !important;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# Helper function to trigger real browser audio playback in Korean
def play_korean_sound(text_to_speak):
    js_code = f"""
        <script>
        var msg = new SpeechSynthesisUtterance('{text_to_speak}');
        msg.lang = 'ko-KR';
        msg.rate = 0.8;
        window.speechSynthesis.speak(msg);
        </script>
    """
    components.html(js_code, height=0)

# Sidebar
st.sidebar.title("🌸 K-dairies")
st.sidebar.caption("Developed with 🌸 by **Your Name**")
st.sidebar.caption("[GitHub Repository](https://github.com/your-username/k-dairies)")

# Main Header
st.title("🔤 Hangul Audio & Sound Guide")
st.write("Click any **'🔊 Play Sound'** button to hear native Korean audio spoken out loud!")

# Tabs
tab1, tab2 = st.tabs(["🔊 Basic Consonants", "🌸 Basic Vowels"])

with tab1:
    st.subheader("1. Basic Consonants (자음)")

    consonants = [
        {"char": "ㄱ", "name": "Giyeok", "sound": "G / K sound", "example": "고기"},
        {"char": "ㄴ", "name": "Nieun", "sound": "N sound", "example": "나무"},
        {"char": "ㄷ", "name": "Digeut", "sound": "D / T sound", "example": "다리"},
        {"char": "ㄹ", "name": "Rieul", "sound": "R / L sound", "example": "라면"},
        {"char": "ㅁ", "name": "Mieum", "sound": "M sound", "example": "마음"},
        {"char": "ㅂ", "name": "Bieup", "sound": "B / P sound", "example": "바다"},
        {"char": "ㅅ", "name": "Siot", "sound": "S sound", "example": "사랑"},
        {"char": "ㅇ", "name": "Ieung", "sound": "Silent / NG", "example": "안녕"},
        {"char": "ㅈ", "name": "Jieut", "sound": "J sound", "example": "지구"},
    ]

    col1, col2 = st.columns(2)
    for index, c in enumerate(consonants):
        target_col = col1 if index % 2 == 0 else col2
        with target_col:
            st.markdown(f"""
            <div class="hangul-box">
                <p class="hangul-char">{c['char']}</p>
                <b>{c['name']}</b><br>
                <span class="sound-text">Sound: <b>{c['sound']}</b></span><br>
                <small class="sound-text">Ex: {c['example']}</small>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"🔊 Listen to {c['char']}", key=f"btn_c_{index}"):
                play_korean_sound(c['example'])

with tab2:
    st.subheader("2. Basic Vowels (모음)")

    vowels = [
        {"char": "ㅏ", "sound": "'Ah'", "example": "아"},
        {"char": "ㅑ", "sound": "'Yah'", "example": "야"},
        {"char": "ㅓ", "sound": "'Eoh'", "example": "어"},
        {"char": "ㅕ", "sound": "'Yeoh'", "example": "여"},
        {"char": "ㅗ", "sound": "'Oh'", "example": "오"},
        {"char": "ㅛ", "sound": "'Yoh'", "example": "요"},
        {"char": "ㅜ", "sound": "'Oo'", "example": "우"},
        {"char": "ㅠ", "sound": "'Yoo'", "example": "유"},
        {"char": "ㅡ", "sound": "'Eu'", "example": "으"},
        {"char": "ㅣ", "sound": "'Ee'", "example": "이"},
    ]

    col1, col2 = st.columns(2)
    for index, v in enumerate(vowels):
        target_col = col1 if index % 2 == 0 else col2
        with target_col:
            st.markdown(f"""
            <div class="hangul-box">
                <p class="hangul-char">{v['char']}</p>
                <span class="sound-text">Sound: <b>{v['sound']}</b></span>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"🔊 Listen to {v['char']}", key=f"btn_v_{index}"):
                play_korean_sound(v['example'])
