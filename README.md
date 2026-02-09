# 🔊 ElevenLabs TTS + STT Python Project

This project demonstrates **both Text-to-Speech (TTS)** and
**Speech-to-Text (STT)** using the ElevenLabs Python SDK.\
It includes:

-   🎤 **Record audio** and convert speech → text\
-   🗣️ **Convert text → natural AI voice**\
-   💾 Save audio files\
-   ⚙️ Clean, modular Python code

------------------------------------------------------------------------

## 🚀 Features

### ✅ Speech-to-Text (STT)

-   Records 5 seconds of audio\
-   Saves to `record.wav`\
-   Converts speech → text using **scribe_v2**

### ✅ Text-to-Speech (TTS)

-   Converts user text to audio\
-   Uses **eleven_multilingual_v2**\
-   Saves output as `output.wav`\
-   Optional playback using FFmpeg

------------------------------------------------------------------------

# 📂 Project Structure (Recommended)

    freelance/
    │
    ├── main.py
    ├── src/
    │   ├── models/
    │   │     ├── STT.py
    │   │     ├── TTS.py
    │   │     └── config.py
    │   └── utils/
    │
    └── README.md

------------------------------------------------------------------------

# 📦 Installation

### 1️⃣ Install Python dependencies

``` bash
uv pip install elevenlabs sounddevice scipy python-dotenv
```

### 2️⃣ Install FFmpeg (Required for audio playback)

Download Windows build:\
https://www.gyan.dev/ffmpeg/builds/

Add to PATH:

    C:\ffmpeg\bin

------------------------------------------------------------------------

# 🔑 Environment Setup

Create a `.env` file:

    ELEVENLABS_API_KEY=YOUR_API_KEY_HERE

Or hardcode in code:

``` python
client = ElevenLabs(api_key="YOUR_API_KEY_HERE")
```

------------------------------------------------------------------------

# 🎤 Speech-to-Text (STT) Code

``` python
import sounddevice as sd
from scipy.io.wavfile import write
from elevenlabs import ElevenLabs

client = ElevenLabs(api_key="YOUR_API_KEY_HERE")

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
```

------------------------------------------------------------------------

# 🗣️ Text-to-Speech (TTS) Code

``` python
from elevenlabs import ElevenLabs, play

client = ElevenLabs(api_key="YOUR_API_KEY_HERE")

text = "Hello! This is an ElevenLabs test."

audio = client.text_to_speech.convert(
    text=text,
    voice_id="pNInz6obpgDQGcFmaJgB",  # Example voice ID
    model_id="eleven_multilingual_v2"
)

# Save audio
with open("output.wav", "wb") as f:
    for chunk in audio:
        f.write(chunk)

print("Saved as output.wav")
```

------------------------------------------------------------------------

# ▶️ How to Run

### Run Speech-to-Text:

``` bash
uv run src/models/STT.py
```

### Run Text-to-Speech:

``` bash
uv run src/models/TTS.py
```

------------------------------------------------------------------------

# ⭐ Tips

-   STT model → `scribe_v2`\
-   TTS model → `eleven_multilingual_v2`\
-   Replace voice_id with any voice from your ElevenLabs dashboard\
-   Works best with FFmpeg installed

------------------------------------------------------------------------

# 📞 Support

If you need: - A fully structured project\
- Combined TTS + STT chatbot\
- Frontend UI\
- Packaging into EXE

Just ask!

------------------------------------------------------------------------

# 📜 License

Free to use for personal and freelance projects.
