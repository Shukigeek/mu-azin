import whisper
import os



class AudioToText:
    def __init__(self,path):
        os.environ["PATH"] += os.pathsep + r"C:\ffmpeg-8.0-essentials_build\bin"
        self.path = path
    def convert_audio(self):
        model = whisper.load_model("small")
        result = model.transcribe(self.path)
        return result["text"]


if __name__ == '__main__':
    att = AudioToText("../podcasts/download.wav")
    print(att.convert_audio())



