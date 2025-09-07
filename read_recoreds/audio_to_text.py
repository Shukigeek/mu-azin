from faster_whisper import WhisperModel










# with open("transcription.txt", "w", encoding="utf-8") as f:
#     for seg in segments:
#         line = f"[{seg.start:.2f}s -> {seg.end:.2f}s] {seg.text}\n"
#         f.write(line)
#         print(line, end="")

class AudioToText:
    def __init__(self,path):
        self.model = WhisperModel("base", device="cpu", compute_type="int8")
        self.path = path
    def convert_audio(self):
        segments, info = self.model.transcribe(self.path, beam_size=5)
        print("segment", segments)
        print("info", info)
        print("Language detected:", info.language)

if __name__ == '__main__':
    att = AudioToText("podcasts/download.wav")
    att.convert_audio()
