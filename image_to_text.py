import PIL.Image


def gemini_vision_img_to_text(client, image_path):
    """ Convert an image to text using Google's Gemini Vision model """
    prompt = """Take this image and describe it in every detail. 
                This detail should be as detailed as possible."""

    source_image = PIL.Image.open(image_path) # Open the source image

    response = client.generate_content(
        [
            source_image, prompt
        ]
    ) # Generate content and resolve the response, wait for the response to be ready, and return the result

    return response.text # Return the generated text