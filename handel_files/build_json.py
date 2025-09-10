from handel_files.metadata import MetaData
from services.logger.logger import Logger

logger = Logger.get_logger()


class Json:
    def __init__(self, path):
        # logger.info(f"loading json from {path}")
        self.path = path
        # logger.info(f"getting metadata")
        self.metadata = MetaData(path).observing_metadata()

    def return_json(self):
        # logger.info("creating json file with metadata and absolute path")
        return {"meta data": self.metadata,
                "path": str(self.path)}
