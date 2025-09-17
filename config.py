EMOTION_MAP = {
    "happy": {
        "base_rate": 220,          # Faster than neutral
        "min_rate_change": 20,     
        "max_rate_change": 80,     
        "base_volume": 0.9,        # Louder than neutral
        "min_volume_change": 0.1,
        "max_volume_change": 0.3,
    },
    "sad": {
        "base_rate": 160,          # Slower than neutral
        "min_rate_change": -20,    
        "max_rate_change": -60,    
        "base_volume": 0.7,       
        "min_volume_change": -0.1,
        "max_volume_change": -0.25,
    },
    "neutral": {
        "base_rate": 180,          # Normal speed
        "min_rate_change": 0,
        "max_rate_change": 0,
        "base_volume": 0.8,        # Balance
        "min_volume_change": 0,
        "max_volume_change": 0,
    }
}
