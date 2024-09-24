import google.generativeai as genai
from PIL import Image
import streamlit as st

google_api_key = 'AIzaSyA_Pd5ELYJI39fFt60EJOLxCZe3IHvgoSo'
genai.configure(api_key=google_api_key)

def get_gemini_response(image, prompt):
  model = genai.GenerativeModel('gemini-1.5-flash')
  response = model.generate_content([image[0], prompt])
  return response.text


def input_image_setup(uploaded_file):

  if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()

    image_parts = [
      {
        "mime_type": uploaded_file.type,
        "data": bytes_data
      }
    ]
    return image_parts
  else:
    raise FileNotFoundError("No file uploaded")


##initialize our streamlit app

st.set_page_config(page_title="Gemini Image demo")

st.header("Gemini Image Based Applications")
input = st.text_input("Input Prompt: ", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("explain the image to me 👇 ")

prompt = f'''
You are an AI system tasked with generating detailed test cases for app functionalities. Based on the provided screenshots and any optional text, your goal is to produce a step-by-step guide for testing the features of the app, including:

optional text : {input}

Feature Description: Briefly describe what the feature being tested does.
Pre-conditions: Outline any setup or prerequisites required before testing the feature.
Testing Steps: Provide clear, numbered steps that a tester should follow.
Expected Results: Specify the expected outcome after each step if the feature is functioning correctly.

'''

if submit:
  image_data = input_image_setup(uploaded_file)
  response = get_gemini_response(image_data, prompt)
  st.subheader("Here The Response is")
  st.write(response)
