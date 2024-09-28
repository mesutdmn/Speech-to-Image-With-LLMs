import PIL.Image
import requests
import time
from openai import OpenAI
from io import BytesIO
import os

def text_to_img_with_dall(client, text):
    """ Convert text to an image using OpenAI's DALL-E model """

    image_url = client.images.generate(
        model="dall-e-3", # Model to use
        size="1024x1024", # Size of the image
        quality="hd", # Quality of the image
        n=1, # Number of images to generate
        response_format="url", # Format of the response
        prompt=text # Text prompt
    ).data[0].url # Get the URL of the image from the response

    response = requests.get(image_url) # Get the image from the URL
    image_bytes = BytesIO(response.content) # Convert the image to bytes

    timestamp = str(int(time.time())) # Get the current timestamp

    image_path = f"./img/{timestamp}.png" # Create the path to save the image

    if not os.path.exists("./img"): # If the img directory does not exist
        os.makedirs("./img") # Create the img directory

    with open(image_path, "wb") as image_file: # Open the image file in write binary mode
        image_file.write(image_bytes.read()) # Write the image to the file

    return image_path # Return the path to the image

