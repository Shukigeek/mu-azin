import speech_recognition as sr
from logger.logger import Logger
logger = Logger.get_logger()


class AudioToText:
    def __init__(self,path):
        self.r = sr.Recognizer()
        self.path = path
    def convert_audio(self):
        #converting audio to text
        with sr.AudioFile(self.path) as source:
            audio = self.r.record(source)

        try:
            text = self.r.recognize_google(audio)
            logger.info("audio convert successfully to text")
            return text
        except sr.UnknownValueError:
            logger.error("Could not understand the audio")



if __name__ == '__main__':

    att = AudioToText("C:/podcasts/download (1).wav")
    att.convert_audio()










