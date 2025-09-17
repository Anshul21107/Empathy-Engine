from textblob import TextBlob

def detect_emotion(text: str):
    
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "happy", min(1.0, polarity)
    elif polarity < -0.1:
        return "sad", min(1.0, abs(polarity))
    else:
        return "neutral", 0.0

