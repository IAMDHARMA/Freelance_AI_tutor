import sounddevice as sd
from scipy.io.wavfile import write
from elevenlabs import ElevenLabs
import os
from dotenv import load_dotenv  

load_dotenv()

client = ElevenLabs(api_key=os.getenv("STT_API_KEY"))

fs = 44100  
seconds = 60  

# Folder path
folder_path = "src/models/stt audio"
os.makedirs(folder_path, exist_ok=True)

file_path = os.path.join(folder_path, "record.wav")

print("Recording...")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()

write(file_path, fs, recording)
print(f"Saved as {file_path}")

with open(file_path, "rb") as f:
    transcription = client.speech_to_text.convert(
        file=f,
        model_id="scribe_v2"
    )

print("\nYou said:")
print(transcription.text)
