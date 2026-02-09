from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import os

load_dotenv()

client = ElevenLabs(
    api_key=os.getenv("TT_API_KEY") 
)

audio = client.text_to_speech.convert(
    text="నేను నిన్ను ప్రేమిస్తున్నాను.",
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

play(audio)