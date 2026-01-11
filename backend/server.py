import websockets
import asyncio
import soundfile as sf
from processing.noise_reduction import reduce_noise
from processing.deepfake_detector import is_fake_voice
from processing.asr import transcribe
from processing.ai_agent import generate_reply
from processing.tts import tts

print("🔵 Starting WebSocket server on ws://0.0.0.0:8000 ...")

async def handle_audio(websocket):
    print("🟢 Client connected!")
    while True:
        audio_bytes = await websocket.recv()

        # Save incoming audio
        with open("input.wav", "wb") as f:
            f.write(audio_bytes)

        # Noise reduction
        clean_audio = reduce_noise(audio_bytes)
        sf.write("clean.wav", clean_audio, 16000)

        # Deepfake detection
        status = is_fake_voice("clean.wav")
        print("Deepfake status:", status)

        if status == "spoof":
            reply_audio = tts("Warning: AI generated voice detected.")
            await websocket.send(reply_audio)
            continue

        # Speech to text
        text = transcribe("clean.wav")
        print("User said:", text)

        # AI response
        reply = generate_reply(text)
        print("AI response:", reply)

        # Convert to speech
        reply_audio = tts(reply)
        await websocket.send(reply_audio)

async def main():
    print("🟡 Setting up server...")
    async with websockets.serve(handle_audio, "0.0.0.0", 8000):
        print("🟢 Server is running! Waiting for client connection...")
        await asyncio.Future()  # keep server alive forever

asyncio.run(main())
