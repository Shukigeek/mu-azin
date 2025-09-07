from read_recoreds.audio_to_text import AudioToText
from read_recoreds.metadata import MetaData


class Json:
    def __init__(self,path):
        self.path = path
        self.data = AudioToText(path).convert_audio()
        self.metadata = MetaData(path).observing_metadata()
    def return_json(self):
        return {"data":self.data,
                "meta data":self.metadata,
                "path":self.path}

