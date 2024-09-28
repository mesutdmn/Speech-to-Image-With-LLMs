
def whisper_to_text(client, audio_path):
    """ Convert audio to text using OpenAI's Whisper model """

    audio = open(audio_path, "rb") # Open audio file in read binary mode

    Aı_generated_text = client.audio.transcriptions.create(
        model="whisper-1", # Model to use
        file=audio, # Audio file
    ).text # Get the text from the response

    return Aı_generated_text # Return the generated text