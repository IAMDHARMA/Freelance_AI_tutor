import sounddevice as sd
from scipy.io.wavfile import write
from elevenlabs import ElevenLabs
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

client = ElevenLabs(api_key=os.getenv("STT_API_KEY"))

fs = 44100
seconds = 60

# Folder path
folder_path = r"R:\freelance\src\stt audio text"
os.makedirs(folder_path, exist_ok=True)

# Unique timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

audio_path = os.path.join(folder_path, f"record_{timestamp}.wav")
text_path = os.path.join(folder_path, f"record_{timestamp}.txt")

print("Recording...")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()

# Save audio
write(audio_path, fs, recording)
print(f"Audio saved as {audio_path}")

# Transcribe
with open(audio_path, "rb") as f:
    transcription = client.speech_to_text.convert(
        file=f,
        model_id="scribe_v2"
    )

print("\nYou said:")
print(transcription.text)

# Save transcription text
with open(text_path, "w", encoding="utf-8") as f:
    f.write(transcription.text)

print(f"Text saved as {text_path}")
