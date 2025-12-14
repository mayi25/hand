""" The main app for the robot hand """
import time
from asr import ASR
import llm
import servo

asr = ASR()

def main():
    """
    Main function to record audio, transcribe it, and then query the llm.
    """
    audio_filename = "recorded_audio.wav"
    print(f"Start record in 2 seconds...")
    time.sleep(2)

    # Record audio
    asr.record_audio_to_file(audio_filename, 10)

    # Transcribe audio
    transcribed_text = asr.transcribe_audio_with_whisper(audio_filename)
    print(f"Transcribed text: {transcribed_text}")

    response = ""
    # Query the llm with the transcribed text
    if transcribed_text:
        response = llm.query_ollama('Try to answer the question in one letter. ' + transcribed_text)

    if response.strip().lower() == "a":
        servo.a()
        time.sleep(3)
        
    if response.strip().lower() == "b":
        servo.b()
        time.sleep(3)
        
    if response.strip().lower() == "c":
        servo.c()
        time.sleep(3)
        
    if response.strip().lower() == "d":
        servo.d()
        time.sleep(3)
        
    if response.strip().lower() == "e":
        servo.e()
        time.sleep(3)


    servo.og()
    time.sleep(3)

main()
