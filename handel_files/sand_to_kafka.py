from handel_files.build_json import Json
from services.kafka_pub_sub.pub.producer import Producer
import os
import wave
from pathlib import Path
from services.logger.logger import Logger

logger = Logger.get_logger(index="handel-files-logs")


class Manager:
    def __init__(self, topic=os.getenv("TOPIC", "podcasts"), path=None):
        self.topic = topic
        self.producer = Producer()
        logger.info(f"initializing path by defaulter or inserted")
        self.path = path or os.getenv("FILE_PATH")
        self.directory_path = Path(self.path)

    def produce_to_kafka(self):
        if self.path == self.path:
            for wav_file in self.directory_path.glob('*.wav'):
                try:
                    logger.info("data publish to kafka")
                    self.producer.publish_message(self.topic, Json(wav_file).return_json())
                except wave.Error as e:
                    logger.error(f"  Error opening WAV file {wav_file}: {e}")
                except Exception as e:
                    logger.error(f"  An unexpected error occurred with {wav_file}: {e}")
        # (this is if one day I would use this func for diff path)
        else:
            try:
                logger.info(f"producing to topic {self.topic} un a inserted file")
                self.producer.publish_message(self.topic, Json(f"{self.path}").return_json())
            except Exception as e:
                logger.error(f"path not valid: {e}")
                return f"path not valid: {e}"


if __name__ == '__main__':
    for wav_file in Path("C:/").glob('podcasts/*.wav'):
        print(Json(wav_file).return_json())
