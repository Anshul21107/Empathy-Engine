import pyttsx3
from config import EMOTION_MAP

def generate_audio(text: str, emotion: str = "neutral", intensity: float = 0.5):
    params = EMOTION_MAP.get(emotion, EMOTION_MAP["neutral"])
    rate_change = int(
        params["min_rate_change"] + intensity * (params["max_rate_change"] - params["min_rate_change"])
    )
    rate = params["base_rate"] + rate_change

    volume_change = (
        params["min_volume_change"] + intensity * (params["max_volume_change"] - params["min_volume_change"])
    )
    volume = max(0.0, min(1.0, params["base_volume"] + volume_change))

    engine = pyttsx3.init()
    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)

    temp_file = "temp_audio.wav"
    engine.save_to_file(text, temp_file)
    engine.runAndWait()

    with open(temp_file, "rb") as f:
        audio_bytes = f.read()

    return audio_bytes
