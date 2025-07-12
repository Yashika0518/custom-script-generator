import streamlit as st
from langchain_script import generate_script

# Set up the page
st.set_page_config(
    page_title="🌸 Custom Script Generator",
    layout="centered",
    page_icon="🎬"
)

# Custom CSS for pastel theme
st.markdown("""
    <style>
    body {
        background-color: #fef6f9;
    }
    .stApp {
        background-color: #fef6f9;
        color: #4a4a4a;
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        font-size: 2.5rem;
        color: #d290c1;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stTextArea textarea {
        background-color: #fff0f5;
        color: #4a4a4a;
    }
    .stButton>button {
        background-color: #d7b4f3;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 1.5em;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #c08dd8;
    }
    .stTextArea {
        border: 1px solid #ffccf9;
        border-radius: 10px;
        margin-bottom: 1.5em;
    }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown('<div class="title">🎬 Custom Script Generator</div>', unsafe_allow_html=True)

st.markdown("Craft engaging scripts with a touch of creativity ✨")

# User input area
user_input = st.text_area("💡 Enter your script prompt (e.g. GRWM, brand ad, speech, etc.)")

# Generate button
if st.button("🚀 Generate Script"):
    if user_input.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating something amazing..."):
            script = generate_script(user_input)
        st.success("✨ Script Ready!")
        st.text_area("📜 Your Generated Script", script, height=300)
