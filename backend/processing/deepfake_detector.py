from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np

encoder = VoiceEncoder()

def is_fake_voice(reference_audio, test_audio):
    """
    Compares embeddings. Returns True if fake, False if real.
    """

    ref_emb = encoder.embed_utterance(reference_audio)
    test_emb = encoder.embed_utterance(test_audio)

    similarity = np.dot(ref_emb, test_emb) / (np.linalg.norm(ref_emb) * np.linalg.norm(test_emb))

    # Threshold: lower similarity = fake
    return similarity < 0.75
