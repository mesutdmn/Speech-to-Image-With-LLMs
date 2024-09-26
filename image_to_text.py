import google.generativeai as genai
import PIL.Image
import requests
import os

from dotenv import load_dotenv

load_dotenv() # Load the .env file

api_key = os.getenv("GENAI_API_KEY") # Get the API key from the .env file

genai.configure(
    api_key=api_key # Set the API key
)

def gemini_vision_img_to_text(image_path):
    """ Convert an image to text using Google's Gemini Vision model """
    prompt = """Take this image and describe it in every detail. 
                This detail should be as detailed as possible."""


    client = genai.GenerativeModel(model_name="gemini-1.5-flash") # Create the Gemini Vision model

    source_image = PIL.Image.open(image_path) # Open the source image

    response = client.generate_content(
        [
            source_image, prompt
        ]
    ) # Generate content and resolve the response, wait for the response to be ready, and return the result

    return response.text # Return the generated text