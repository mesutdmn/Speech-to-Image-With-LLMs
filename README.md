![speach_to_image](https://github.com/user-attachments/assets/4733564e-4378-4442-8ad8-30b2efb25334)
# Voice-to-Image Application

This application allows users to describe images using their voice, converting the audio input into text with the OpenAI Whisper-1 model, and then generating an image from that text using the DALL-E model. Users can also obtain descriptions of their generated images via GeminiAI.

### How does App work?

![How does app work](https://github.com/user-attachments/assets/3f427fff-0093-4c10-9d8b-333f1fde1c03)



### Features

- **Whisper-1 Model**: Utilizes the OpenAI Whisper-1 model to convert audio recordings into text.
- **DALL-E Model**: Employs the DALL-E model to generate images from text.
- **Description Retrieval**: Users can click the "Describe" button to obtain descriptions of their generated images.

### Usage Instructions

1. **API Keys**: Enter your OpenAI and GoogleAI API keys in the left-side menu.
2. **Record Audio**: Use the application interface to record your voice.
3. **Check Audio**: Click the "Check" button to review your recorded audio.
4. **Send to AI**: You can either send the audio or use the direct send option.

### Libraries
```python
openai==1.48.0
streamlit==1.38.0
Wave==0.0.2
google-generativeai==0.8.2
streamlit-audiorec
```
### Requirements

- OpenAI API Key
- GoogleAI API Key

### Notes

- This application is developed for individual experiences and is not a commercial product.

### Contributing

If you have any suggestions or feedback regarding errors, please feel free to reach out to me on LinkedIn.

### Main Page
![app-main-page](https://github.com/user-attachments/assets/eb601c08-4498-4782-a200-1a072f0172a7)
