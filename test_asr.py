""" The main app for the robot hand """
import time
from asr import ASR

asr = ASR()

def main():
    """
    Main function to record audio, transcribe it, and then query the llm.
    """
    audio_filename = "recorded_audio.wav"
    # Transcribe audio
    count = 0
    while True:
        count += 1
        transcribed_text = asr.transcribe_audio_with_whisper(audio_filename)
        print(f"Transcribed text: {transcribed_text}, count: {count}")

main()
