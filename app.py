import streamlit as st
from time import sleep
import os
from st_audiorec import st_audiorec
import wave
from streamlit.components.v1 import html
import audio_to_text
import image_to_text
import text_to_image
from PIL import Image
from openai import OpenAI
import google.generativeai as genai

st.set_page_config(page_title="Voice to Image", page_icon="🎤", layout="wide")
st.image("./media/cover.webp", use_column_width=True)
img_folder = './img'
images = [f for f in os.listdir(img_folder) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

with st.sidebar:
    st.info("""Please enter your API keys below, API keys are required to use the OpenAI and Google GenerativeAI APIs. They are not saved or stored anywhere.
    \n * [Get an OpenAI API key](https://platform.openai.com/account/api-keys)
    \n * [Get an GoogleAI API key](https://console.cloud.google.com/apis/credentials)
    \n * [View the source code](https://github.com/mesutdmn/Speach-to-Image-With-LLMs)
    """)
    open_ai_key = st.text_input("OpenAI API Key", type="password", help="Get your API key from https://platform.openai.com/account/api-keys")
    gen_ai_key = st.text_input("Google GenerativeAI API Key", type="password", help="Get your API key from https://console.cloud.google.com/apis/credentials")

    if not open_ai_key:
        st.error("Please add your OpenAI API key to continue.")
    else:
        client_openai = OpenAI(api_key=open_ai_key)

    if not gen_ai_key:
        st.error("Please add your GoogleAI API key to continue.")
    else:
        genai.configure(api_key=gen_ai_key)
        client_genai = genai.GenerativeModel(model_name="gemini-1.5-flash")
    if len(images) > 0:
        st.sidebar.title("🖼️ Created Images")
        sidecol1, sidecol2 = st.columns([1, 1])
        for i, img_file in enumerate(images):
            img_path = os.path.join(img_folder, img_file)
            img = Image.open(img_path)

            if i % 2 == 0:
                sidecol1.image(img, caption=None, width=100)
                sidecol1.markdown(f"[{img_file}]({img_path})")
            else:
                sidecol2.image(img, caption=None, width=100)
                sidecol2.markdown(f"[{img_file}]({img_path})")

if "latest_image" not in st.session_state:
    st.session_state["latest_image"] = None
    st.session_state["messages"] = []

if "recording_status" not in st.session_state:
    st.session_state["recording_status"] = "🎙️ No record, please record an audio first."
    st.session_state["control"] = "✔️ Ready to record!"


def update_recording_status(status):
    st.session_state["control"] = status


def describe_image():
    if st.session_state["latest_image"] is not None:
        with col_image:
            with st.spinner("🔍 Describing image..."):
                image_description = image_to_text.gemini_vision_img_to_text(client_genai, st.session_state["latest_image"])
                st.session_state["messages"].append({"role": "bot", "content": image_description})
    else:
        update_recording_status("🚫 No image to describe!")

def save_audio():
    if wav_audio_data is not None:
        update_recording_status("✅ Audio is valid!")
        sound_file = wave.open("sound.wav", "wb")  # Open sound file in write binary mode
        sound_file.setnchannels(1)  # Set number of channels
        sound_file.setsampwidth(4)  # Set sample width
        sound_file.setframerate(44100)  # Set frame rate
        sound_file.writeframes(wav_audio_data)  # Write frames to file, because frames is list of bytes
        sound_file.close()
    else:
        update_recording_status("🔇 No audio recorded!")

def script():
    with open("./script.js", "r", encoding="utf-8") as scripts:
        open_script = f"""<script>{scripts.read()}</script> """
        html(open_script, width=0, height=0)

st.info("This app build for skill test, it allows you to convert your voice to an image. Then you can ask to Gemini Vision model to describe the image in every detail.")

col_audio, col_image = st.columns([1,3])

with col_audio:
    st.divider()
    st.info(st.session_state["recording_status"])
    st.warning(st.session_state["control"])
    st.divider()

    subcol_left, subcol_right = st.columns([1,1])

    with subcol_left:
        wav_audio_data = st_audiorec()
        check_audio = st.button(label="Check Audio", on_click=save_audio)
        send_to_whisper = st.button(label="Send to AI")
        describe = st.button(label="Describe Latest Image", on_click=describe_image)
    with subcol_right:
        recorded_audio = st.empty()
        if check_audio & (wav_audio_data is not None):
            recorded_audio.audio("sound.wav", format="audio/wav")

with col_image:
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

    if send_to_whisper & (wav_audio_data is not None):
        save_audio(file=wav_audio_data)
        update_recording_status("🤖 Sent to AI")
        with st.chat_message(name="user", avatar="👤"):
            with st.spinner("📑 Converting audio to text..."):
                voice_prompt = audio_to_text.whisper_to_text(client_openai,audio_path="sound.wav")
                st.success(voice_prompt)

        st.session_state["messages"].append({"role": "user", "content": voice_prompt})
        with st.spinner("📷 Converting text to image..."):
            image = text_to_image.text_to_img_with_dall(client_openai, voice_prompt)
            st.image(image, width=300)
        st.session_state["messages"].append({"role": "assistant", "content": image})
        st.session_state["latest_image"] = image
sleep(0.5)
script()