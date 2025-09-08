from io import BytesIO

import whisper
import os
from logger.logger import Logger
logger = Logger.get_logger()


class AudioToText:
    def __init__(self,path):
        logger.info("initialize audio to text")
        logger.info("connecting to path (on the computer): {}".format(path))
        os.environ["PATH"] += os.pathsep + r"C:\ffmpeg-8.0-essentials_build\bin"
        self.path = path
    def convert_audio(self):
        #converting audio to text
        logger.info("convert audio to text")
        model = whisper.load_model("small")
        result = model.transcribe(self.path)
        logger.info("transcription successful")
        return result["text"]


if __name__ == '__main__':
    from bson.binary import Binary
    with open("C:/podcasts/download (1).wav","rb") as f:
        wav = f.read()

    att = AudioToText(Binary(wav))
    print(att.convert_audio())



