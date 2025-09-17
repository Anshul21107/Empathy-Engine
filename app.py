from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import io
from emotion_detector import detect_emotion
from tts_engine import generate_audio

app = FastAPI(title="Empathy Engine")

class TextRequest(BaseModel):
    text: str

@app.post("/speak")
def speak(request: TextRequest):
    text = request.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    emotion, intensity = detect_emotion(text)
    audio_bytes = generate_audio(text, emotion, intensity)

    return StreamingResponse(
        io.BytesIO(audio_bytes),   
        media_type="audio/wav",    
        headers={
            "X-Emotion": emotion,
            "X-Intensity": str(intensity)
        }
    )


if __name__ == "__main__":
    import uvicorn
    local_url = "http://127.0.0.1:8000"
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
