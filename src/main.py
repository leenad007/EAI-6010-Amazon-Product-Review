import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/predict-text"

# Streamlit UI with emoji 🎯
st.title("📢 Amazon Product Review Sentiment Analysis")
st.write("Enter a text below and click 'Analyze' to determine its sentiment.")

# Text input
text_input = st.text_area("📝 Enter your product review here", "")

if st.button("🔍 Analyze Sentiment"):
    if text_input.strip():
        with st.spinner("🔄 Analyzing..."):
            # Send request to FastAPI backend
            response = requests.post(API_URL, json={"text": text_input})
            
            if response.status_code == 200:
                result = response.json()
                sentiment = result["sentiment"]

                # Display sentiment with an emoji
                emoji = "😊" if sentiment == "positive" else "😞"
                st.success(f"Sentiment: {emoji} **{sentiment.capitalize()}**")
            else:
                st.error("❌ Error: Could not analyze sentiment. Try again!")
    else:
        st.warning("⚠️ Please enter some text before clicking Analyze.")
