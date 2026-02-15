from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import os
from datetime import datetime

load_dotenv()

client = ElevenLabs(
    api_key=os.getenv("TT_API_KEY") 
)

# Take input
user_text = input("Enter Text: ")

audio_generator = client.text_to_speech.convert(
    text=user_text,
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

audio_bytes = b"".join(audio_generator)

# Folder path (⚠ avoid special characters like & & in folder names)
folder_path = r"R:\freelance\src\ttf text audio"
os.makedirs(folder_path, exist_ok=True)

# Timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

audio_filename = os.path.join(folder_path, f"conversation_{timestamp}.mp3")
text_filename = os.path.join(folder_path, f"conversation_{timestamp}.txt")

# Save audio
with open(audio_filename, "wb") as f:
    f.write(audio_bytes)

# Save input text
with open(text_filename, "w", encoding="utf-8") as f:
    f.write(user_text)

# Play audio
play(audio_bytes)

print(f"Audio saved in {audio_filename}")
print(f"Text saved in {text_filename}")
