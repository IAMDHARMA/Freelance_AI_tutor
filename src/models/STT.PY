import sounddevice as sd
from scipy.io.wavfile import write
from elevenlabs import ElevenLabs
import os
from dotenv import load_dotenv  
load_dotenv()

client = ElevenLabs(api_key=os.getenv("STT_API_KEY"))

fs = 44100  
seconds = 5  

print("Recording...")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()
write("record.wav", fs, recording)
print("Saved as record.wav")

with open("record.wav", "rb") as f:
    transcription = client.speech_to_text.convert(
        file=f,
        model_id="scribe_v2"
    )

print("\nYou said:")
print(transcription.text)
