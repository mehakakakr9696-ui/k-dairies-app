import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(page_title="K-dairies | Hangul Practice", page_icon="🌸", layout="centered")

# -----------------------------
# K-Diaries Navigation
# -----------------------------

if "page" not in st.session_state:
    st.session_state.page = "Home"

st.sidebar.title("🌸 K-Diaries")

page = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "🔤 Hangul Audio & Sound Guide"]
)

if page == "🏠 Home":
    st.session_state.page = "Home"
else:
    st.session_state.page = "Hangul"
    # -----------------------------
# HOME PAGE
# -----------------------------

if st.session_state.page == "Home":

    st.markdown(
        """
        <div class="home-container">
            <h1>🌸 K-Diaries</h1>
            <h3>Your little journey into Korean 🇰🇷</h3>
            <p>
                Learn Hangul, improve your pronunciation,
                and discover Korean through an interactive experience.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # Welcome section
    st.subheader("안녕하세요! 👋")
    st.write(
        "Welcome to K-Diaries! Start your Korean-learning journey "
        "one little step at a time."
    )

    st.write("")

    # Feature cards
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            ### 🔤 Learn Hangul
            Learn Korean consonants and vowels with
            pronunciation examples and audio.
            """
        )

       if st.button("🔤 Start Learning Hangul"):
          st.success("Hangul lessons are ready! 🎉")
          

    with col2:
        st.markdown(
            """
            ### 🎧 Listen & Practice
            Hear Korean sounds and become familiar
            with Korean pronunciation.
            """
        )

        st.info("More practice features coming soon! ✨")

    st.write("")
    st.divider()

    st.subheader("🌱 Your Korean Journey")

    st.progress(0)

    st.caption("Begin your journey by learning Hangul!")

    st.write("")
    st.write("💗 Made with Python & Streamlit")
