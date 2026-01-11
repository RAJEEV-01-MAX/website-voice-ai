import whisper

model = whisper.load_model("base")

def transcribe(audio_path):
    """
    Takes an audio file path and returns transcribed text.
    """
    result = model.transcribe(audio_path)
    return result["text"]
