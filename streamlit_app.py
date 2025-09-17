import streamlit as st
import requests

st.title("Empathy Engine")

text = st.text_area("Enter text: ")

if st.button("Generate Emotional Speech"):
    if text.strip():
        try:
            response = requests.post(
                "http://127.0.0.1:8000/speak",
                json={"text": text}
            )

            if response.status_code == 200:
                emotion = response.headers.get("X-Emotion", "unknown")
                intensity = response.headers.get("X-Intensity", "0")

                st.success(f"Detected Emotion: {emotion}, Intensity: {intensity}")
                st.audio(response.content, format="audio/mp3")
            else:
                st.error(f"Error {response.status_code}: {response.text}")

        except Exception as e:
            st.error(f"Request failed: {e}")

