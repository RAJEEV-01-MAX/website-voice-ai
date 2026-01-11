import noisereduce as nr
import numpy as np

def reduce_noise(audio, sr):
    """
    Reduces noise from audio using noisereduce library.
    """
    reduced_audio = nr.reduce_noise(y=audio, sr=sr)
    return reduced_audio
