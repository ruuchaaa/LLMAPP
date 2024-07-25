from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import io

# Configure the generative AI model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input_text, image):
    if input_text != "":
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    return response.text

# Streamlit app configuration
st.set_page_config(page_title="Gemini Image DEMO")
st.header("Gemini Application")

# Input text
input_text = st.text_input("Input: ", key="input")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None
if uploaded_file is not None:
    # Convert the uploaded file to a PIL Image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

# Submit button
submit = st.button("TELL ME ABOUT THE IMAGE")

if submit:
    if image is not None:
        # Get response from generative model
        response = get_gemini_response(input_text, image)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload an image.")
