from elevenlabs import generate

def tts(text):
    audio = generate(text=text, voice="Bella")
    return audio
