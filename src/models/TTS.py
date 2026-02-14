from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import os
from datetime import datetime

load_dotenv()

client = ElevenLabs(
    api_key=os.getenv("TT_API_KEY") 
)

audio_generator = client.text_to_speech.convert(
    text=input("Give Text:"),
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

# Convert generator to bytes
audio_bytes = b"".join(audio_generator)


# Folder path
folder_path = "src/tts audio"
os.makedirs(folder_path, exist_ok=True)

# Create unique filename using timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = os.path.join(folder_path, f"conversation_{timestamp}.mp3")

# Save file
with open(filename, "wb") as f:
    f.write(audio_bytes)

# Play audio
play(audio_bytes)

print(f"Saved as {filename}")
