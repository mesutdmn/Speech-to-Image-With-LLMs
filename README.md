![speach_to_image](https://github.com/user-attachments/assets/4733564e-4378-4442-8ad8-30b2efb25334)
# Voice-to-Image Application

This application allows users to describe images using their voice, converting the audio input into text with the OpenAI Whisper-1 model, and then generating an image from that text using the DALL-E model. Users can also obtain descriptions of their generated images via GeminiAI.

### How does the App work?

![How does App work?](https://github.com/user-attachments/assets/b8f2cbd7-b88b-471f-9488-22a555f629d1)



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

### Demo Video

https://github.com/user-attachments/assets/87b3b821-2c35-4453-9fc0-a86ba393719d



