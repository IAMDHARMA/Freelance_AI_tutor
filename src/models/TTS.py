from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import os

load_dotenv()

client = ElevenLabs(
    api_key=os.getenv("TT_API_KEY") 
)

audio = client.text_to_speech.convert(
    text="i am a supernowa clone ai tutor. What can i do it for you?",
    voice_id="JBFqnCBsd6RMkjVDRZzb",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
)

play(audio)