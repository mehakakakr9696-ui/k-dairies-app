import streamlit as st

# page configurations
st.set_page_config(
    page_title="K-Diaries: Learn Hangul!",
    page_icon="🇰🇷",
    layout="centered"
)
# custom css layout block
st.markdown("""
<style>
.home-box {
    background-color: #ffe6f0;
    color: #8B1E3F
    padding: 25px;
    border-radius: 15px;
    text-align: center;
}
.home-box h1 {
    color: #8B1E3F
}
</style>
""", unsafe_allow_html=True)
# Main title display
st.markdown('<div class="home-box"><h1>Welcome to K-Diaries</h1></div>', unsafe_allow_html=True)
    

st.subheader("Your little journey Into Korean")

st.write("Learn Korean step by step through Hangul, syllables, pronunciation, and practice.")
st.markdown("""
<div style="
    background-color: #fff0f5;
    color: #8B1E3F;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    margin-top: 15px;
">
    <h3>안녕하세요! </h3>
    <p>Welcome to your Korean-learning journey!</p>
    <p>📃 Learn • 🎧 Listen • ❤️ Practice • 🇰🇷 Discover</p>
</div>
""", unsafe_allow_html=True)

st.divider()
# titles for app header section
st.title("K-Diaries: Learn Hangul")
st.caption("Master Korean step-by-step from characters to syllable blocks!")

# sidebar navigation links
tab = st.sidebar.radio("Navigate Lessons", [
    "1. Vowels & Consonants", 
    "2. Syllable Box (C + V)", 
    "3. Practice & Quiz"
])

# lesson 1 tab view
if tab == "1. Vowels & Consonants":
    st.header("1. Basic Consonants & Vowels")
    st.write("Before making syllable blocks, let's review the basic letters:")

    col_c, col_v = st.columns(2)

    with col_c:
        st.subheader("Basic Consonants (자음)")
        st.write("• **ㄱ** - g / k")
        st.write("• **ㄴ** - n")
        st.write("• **ㄷ** - d / t")
        st.write("• **ㄹ** - r / l")
        st.write("• **ㅁ** - m")
        st.write("• **ㅂ** - b / p")
        st.write("• **ㅅ** - s")
        st.write("• **ㅇ** - silent (start) / ng (end)")
        st.write("• **ㅈ** - j")
        st.write("• **ㅊ** - ch")
        st.write("• **ㅋ** - k")
        st.write("• **ㅌ** - t")
        st.write("• **ㅍ** - p")
        st.write("• **ㅎ** - h")

    with col_v:
        st.subheader("Vertical Vowels (모음)")
        st.write("• **ㅏ** - a" )
        st.write("• **ㅓ** - eo")
        st.write("• **ㅣ** - i" )
        st.write("• **ㅑ** - ya")
        st.write("• **ㅕ** - yeo")
        st.write("• **ㅗ** - o")
        st.write("• **ㅛ** - yo")
        st.write("• **ㅜ** - u")
        st.write("• **ㅠ** - yu")
        st.write("• **ㅡ** - eu")
        
# Lesson 2 tab view
elif tab == "2. Syllable Box (C + V)":
    st.header("2. Side-by-Side Syllable Box")
    st.write("In Korean, individual letters are never written alone. They are combined into 'syllable blocks'.")
    st.info(" **Rule:** When a vowel has a vertical line (like ㅏ, ㅣ, ㅓ, ㅑ), the consonant sits on the *LEFT* and the vowel sits on the *RIGHT*.")

    # simple lists for selection box inputs
    consonants = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ"]
    vowels = ["ㅏ", "ㅓ", "ㅣ", "ㅑ"]
    # translations data dictionary
    syllable_map = {
        ("ㄱ", "ㅏ"): ("가", "ga"), ("ㄱ", "ㅓ"): ("거", "geo"), ("ㄱ", "ㅣ"): ("기", "gi"), ("ㄱ", "ㅑ"): ("갸", "gya"),
        ("ㄴ", "ㅏ"): ("나", "na"), ("ㄴ", "ㅓ"): ("너", "neo"), ("ㄴ", "ㅣ"): ("니", "ni"), ("ㄴ", "ㅑ"): ("냐", "nya"),
        ("ㄷ", "ㅏ"): ("다", "da"), ("ㄷ", "ㅓ"): ("더", "deo"), ("ㄷ", "ㅣ"): ("디", "di"), ("ㄷ", "ㅑ"): ("댜", "dya"),
        ("ㄹ", "ㅏ"): ("라", "ra"), ("ㄹ", "ㅓ"): ("러", "reo"), ("ㄹ", "ㅣ"): ("리", "ri"), ("ㄹ", "ㅑ"): ("랴", "rya"),
        ("ㅁ", "ㅏ"): ("마", "ma"), ("ㅁ", "ㅓ"): ("머", "meo"), ("ㅁ", "ㅣ"): ("미", "mi"), ("ㅁ", "ㅑ"): ("먀", "mya"),
        ("ㅂ", "ㅏ"): ("바", "ba"), ("ㅂ", "ㅓ"): ("버", "beo"), ("ㅂ", "ㅣ"): ("비", "bi"), ("ㅂ", "ㅑ"): ("뱌", "bya"),
        ("ㅅ", "ㅏ"): ("사", "sa"), ("ㅅ", "ㅓ"): ("서", "seo"), ("ㅅ", "ㅣ"): ("시", "si"), ("ㅅ", "ㅑ"): ("샤", "sya"),
        ("ㅇ", "ㅏ"): ("아", "a"),  ("ㅇ", "ㅓ"): ("어", "eo"), ("ㅇ", "ㅣ"): ("이", "i"),  ("ㅇ", "ㅑ"): ("야", "ya"),  
        ("ㅈ", "ㅏ"): ("자", "ja"), ("ㅈ", "ㅓ"): ("저", "jeo"), ("ㅈ", "ㅣ"): ("지", "ji"), ("ㅈ", "ㅑ"): ("쟈", "jya"),
    }

    st.subheader(" Build a Syllable Block:")
    col1, col2 = st.columns(2)

    with col1:
        sel_c = st.selectbox("Choose Consonant (Left):", consonants)
    with col2:
        sel_v = st.selectbox("Choose Vowel (Right):", vowels)
    # find the character in our dictionary

    syllable, pronunciation = syllable_map.get((sel_c, sel_v), ("?", "?"))

    # Display Syllable Box UI
    st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center; gap: 15px; margin: 30px 0;">
            <div style="border: 2px dashed #4A90E2; padding: 15px 25px; border-radius: 10px; font-size: 36px; font-weight: bold; background-color: #f0f4f8; color: #6B1E3E">
                {sel_c}
            </div>
            <span style="font-size: 28px;">+</span>
            <div style="border: 2px dashed #E91E63; padding: 15px 25px; border-radius: 10px; font-size: 36px; font-weight: bold; background-color: #fdf0f4; color: #6B1E3E">
                {sel_v}
            </div>
            <span style="font-size: 28px;">=</span>
            <div style="border: 3px solid #2ECC71; padding: 20px 35px; border-radius: 10px; font-size: 48px; font-weight: bold; background-color: #eafaf1; color: #6B1E3E">
                {syllable}
            </div>
        </div>
        """, unsafe_allow_html=True)
# tab 3 content setup
elif tab == "3. Practice & Quiz":
    st.header("3. Practice & Quiz")

    st.subheader("Simple One-Syllable Words")
    st.write("• **가** (ga) = Go `[ㄱ + ㅏ]`")
    st.write("• **나** (na) = Me / I `[ㄴ + ㅏ]`")
    st.write("• **사** (sa) = Buy `[ㅅ + ㅏ]`")

    st.write("---")
    st.subheader("Put Letters in the Box")
    st.write("Test your Knowledge by assembling the correct syllable blocks")
    
    consonants = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ"]
    vowels = ["ㅏ", "ㅓ", "ㅣ", "ㅑ"]
    
    st.subheader("Question 1: Make the syllable 'ga' (as in 가 - Go)")
    q1_c = st.selectbox("Select Consonant:", consonants, key="q1_c")
    q1_v = st.selectbox("Select Vowel:", vowels, key="q1_v")

    if st.button("Check Question 1"):
        if q1_c == "ㄱ" and q1_v == "ㅏ":
            st.success("Correct! ㄱ + ㅏ = 가")
            st.balloons()
        else:
            st.error("Try again! Hint: look for 'g' sound is ㄱ, 'a' sound is ㅏ.")

    st.markdown("---")

    st.subheader("Question 2: Make the syllable 'na' (as in 나 - Me / I)")
    q2_c = st.selectbox("Select Consonant:", options=consonants, key="q2_c")
    q2_v = st.selectbox("Select Vowel:", options=vowels, key="q2_v")

    if st.button("Check Question 2"):
        if q2_c == "ㄴ" and q2_v == "ㅏ":
            st.success("Correct! ㄴ + ㅏ = 나")
            st.balloons()
        else:
            st.error("Try again! Hint: look for the 'n' sound (ㄴ) and 'a' sound (ㅏ)")
    if tab == "2. Syllable Box (C + V)":

        st.subheader("Syllable Box 2")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            <div style="
                background-color: #f0f4f8;
                color: #6B1E3E;
                padding: 15px;
                border-radius: 10px;
                text-align: center;
                font-size: 36px;
                font-weight: bold;
            ">
            ㄱ
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div style="
                background-color: #fdf0f4;
                color: #6B1E3E;
                padding: 15px;
                border-radius: 10px;
                text-align: center;
                font-size: 36px;
                font-weight: bold;
            ">
            ㅏ
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div style="
                background-color: #fdf0f4;
                color: #6B1E3E;
                padding: 15px;
                border-radius: 10px;
                text-align: center;
                font-size: 48px;
                font-weight: bold;
            ">
            가
            </div>
            """, unsafe_allow_html=True)

       
