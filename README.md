# 🎤 Speech-to-Text (STT) using ElevenLabs + Python

This project records audio from your microphone, saves it as a WAV file,
and sends it to ElevenLabs' Speech-to-Text API for transcription.

## 🚀 Features

-   Record audio using your microphone\
-   Save audio as `.wav`\
-   Convert speech → text using **ElevenLabs Scribe v2**\
-   Simple & clean Python code\
-   Works in Windows, Mac, Linux

## 📦 Installation

### 1️⃣ Install dependencies

``` bash
uv pip install sounddevice scipy elevenlabs
```

You also need FFmpeg:\
Windows: https://www.gyan.dev/ffmpeg/builds/\
Add FFmpeg to PATH: `C:\ffmpeg\bin`

## 🔑 Set Your ElevenLabs API Key

Edit `STT.py`:

``` python
client = ElevenLabs(api_key="YOUR_API_KEY_HERE")
```

Or use `.env`.

## 📝 STT Code

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

## ▶️ Run

``` bash
uv run STT.py
```

## ⭐ License

Free for personal and freelance use.
