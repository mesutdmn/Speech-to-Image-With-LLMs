import streamlit as st
import threading
from time import sleep
import os

if "set_apis" not in st.session_state:
    os.environ["OPENAI_API_KEY"] = ""
    os.environ["GENAI_API_KEY"] = ""

import audio_recorder
import audio_to_text
import image_to_text
import text_to_image

if "recording" not in st.session_state:
    st.session_state['recording'] = threading.Event()
    st.session_state["recording_status"] = "Ready to record!"
    st.session_state["recording_completed"] = False
    st.session_state["latest_image"] = None
    st.session_state["messages"] = []
    st.session_state["frames"] = []
def start_recording():
    st.session_state["recording"].set()
    st.session_state["frames"] = []
    st.session_state["recording_status"] = ":red_circle: Recording..."
    st.session_state["recording_completed"] = False

    threading.Thread(
        target=audio_recorder.record_audio,
        args=(st.session_state["recording"],
              st.session_state["frames"])
    ).start()

def stop_recording():
    st.session_state["recording"].clear()
    st.session_state["recording_status"] = ":white_check_mark: Recording completed!"
    st.session_state["recording_completed"] = True

def describe_image():
    if st.session_state["latest_image"] is not None:
        image_description = image_to_text.gemini_vision_img_to_text(st.session_state["latest_image"])
        st.session_state["messages"].append({"role": "bot", "content": image_description})

st.set_page_config(page_title="Voice to Image", page_icon="🎤", layout="wide")

st.title("Voice to Image")
st.divider()
st.write("This app build for skill test, it allows you to convert your voice to an image. Then you can ask to Gemini Vision model to describe the image in every detail.")
with st.sidebar:
    st.info("Please enter your API keys below, API keys are required to use the OpenAI and Google GenerativeAI APIs. They are not saved or stored anywhere.")
    open_ai_key = st.text_input("OpenAI API Key", type="password", help="Get your API key from https://platform.openai.com/account/api-keys")
    gen_ai_key = st.text_input("Google GenerativeAI API Key", type="password", help="Get your API key from https://console.cloud.google.com/apis/credentials")
    if open_ai_key and gen_ai_key:
        os.environ["OPENAI_API_KEY"] = open_ai_key
        os.environ["GENAI_API_KEY"] = gen_ai_key

col_audio, col_image = st.columns([1,3])

with col_audio:

    st.subheader("Audio Record")
    st.divider()
    status_message = st.info(st.session_state["recording_status"])
    st.divider()

    subcol_left, subcol_right = st.columns([1,1])

    with subcol_left:
        start_button = st.button(label="Start Recording", on_click=start_recording, disabled=st.session_state["recording"].is_set())
        stop_button = st.button(label="Stop Recording", on_click=stop_recording, disabled=not st.session_state["recording"].is_set())
        describe = st.button(label="Describe Latest Image", on_click=describe_image)
    with subcol_right:
        recorded_audio = st.empty()

        sleep(1) # Sleep for 1 seconds to allow the recording to complete
        if st.session_state["recording_completed"]:
            recorded_audio.audio("sound.wav", format="audio/wav")


with col_image:
    st.subheader("Image Outputs")
    st.divider()

    for message in st.session_state["messages"]:
        if message["role"] == "assistant":
            with st.chat_message(name=message["role"], avatar="🤖"):
                st.image(image=message["content"], width=300)
        elif message["role"] == "user":
            with st.chat_message(name=message["role"], avatar="👤"):
                st.success(message["content"])
        elif message["role"] == "bot":
            with st.chat_message(name=message["role"], avatar="🤖"):
                st.info(message["content"])

    if stop_button:
        with st.chat_message(name="user", avatar="👤"):
            voice_prompt = audio_to_text.whisper_to_text("sound.wav")
            st.success(voice_prompt)

        st.session_state["messages"].append({"role": "user", "content": voice_prompt})
        with st.spinner("Converting text to image..."):
            image = text_to_image.text_to_img_with_dall(voice_prompt)
            st.image(image, width=300)
        st.session_state["messages"].append({"role": "assistant", "content": image})
        st.session_state["latest_image"] = image



