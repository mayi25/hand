import pyaudio
import wave
import whisper

class ASR():
    def __init__(self):
        print("Loading whisper model...")
        self.model = whisper.load_model("tiny")

    def record_audio_to_file(self, filename="output.wav", record_seconds=5):
        """Records audio from the microphone for a specified duration and saves it to a file."""
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print(f"* recording for {record_seconds} seconds...")

        frames = []

        for i in range(0, int(RATE / CHUNK * record_seconds)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(filename, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        print(f"Audio saved to {filename}")

    def transcribe_audio_with_whisper(self, audio_path="output.wav"):
        """Transcribes audio from a file using the tiny whisper model."""
        print("Transcribing audio...")
        result = self.model.transcribe(audio_path)
        return result["text"]
