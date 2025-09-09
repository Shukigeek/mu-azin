from STT.audio_to_text import AudioToText
from mongo.write_read_mongo import AudioToMongo
from elastic.elastic_base import ElasticBase
from logger.logger import Logger
logger = Logger.get_logger()
from io import BytesIO
import numpy as np


class STT:
    def __init__(self):
        self.es = ElasticBase()
        self.mongo = AudioToMongo()
    def convert_byte_to_audio(self,binary_data):
        try:
            binary_stream = BytesIO(binary_data)
            numpy_array_from_buffer = np.frombuffer(binary_stream.getvalue(), dtype=np.uint8)
            # returning it back like a file
            file_like_audio = BytesIO(numpy_array_from_buffer)
            logger.info('Converting byte to audio')
            return file_like_audio
        except Exception as e:
            logger.error(f"error converting bytes to data : {e}")


    def speach_to_text(self):
        all_docs = []
        try:
            for record in self.mongo.read_all_from_mongo():
                id = record["_id"]
                data = record["data"]
                file_like_data = self.convert_byte_to_audio(data)
                speach = AudioToText(file_like_data)
                logger.info("converting audio to text")
                text = speach.convert_audio()
                data = {"id": id, "text": text}
                all_docs.append(data)
            return all_docs
        except Exception as e:
            logger.error(f"error fetching data from mongodb : {e}")


if __name__ == '__main__':
    s = STT()
    with open("C:/podcasts/download (1).wav","rb") as f:
        audio_bytes = f.read()
        audio = s.convert_byte_to_audio(audio_bytes)

    a = AudioToText(audio)
    print(a.convert_audio())
