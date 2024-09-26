import pyaudio # PyAudio is required to record audio
import wave # Wave is required to save audio to file

def record_audio(recording, frames):
    """ Record audio and save it to a file """

    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=pyaudio.paInt16, # 16-bit int Audio format
        channels=1, # Mono channel, becouse mone channel record is enough
        rate=44100, # Sample rate, standard for audio
        input=True, # Input stream, becouse we are recording
        frames_per_buffer=1024 # Buffer size, need split audio to chunks
    )

    while recording.is_set(): # While record_active is True record audio
        data = stream.read(
                    num_frames=1024, # Number of frames to read
                    exception_on_overflow=False # Ignore overflow, don't stop recording
                )

        frames.append(data) # Append data to frames list

    stream.stop_stream() # Stop stream
    stream.close() # Close stream, free resources
    audio.terminate() # Terminate audio, free resources

    sound_file = wave.open("sound.wav", "wb") # Open sound file in write binary mode
    sound_file.setnchannels(1) # Set number of channels
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16)) # Set sample width
    sound_file.setframerate(44100) # Set frame rate
    sound_file.writeframes(b"".join(frames)) # Write frames to file, because frames is list of bytes
    sound_file.close() # Close file, free resources

