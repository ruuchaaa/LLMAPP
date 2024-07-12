import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Debugging
st.write("Environment Variables Loaded")

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("API key is missing. Check your .env file.")
else:
    genai.configure(api_key=api_key)
    st.write("GenAI Configured")

try:
    model = genai.GenerativeModel("gemini-pro")
    st.write("Model Initialized")
except Exception as e:
    st.error(f"Model Initialization Error: {e}")

def get_gemini_response(question):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return "Error"

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

input_text = st.text_input("Input:", key="input")
submit_button = st.button("Ask the question")

if submit_button:
    if input_text:
        response = get_gemini_response(input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.error("Please enter a question.")
