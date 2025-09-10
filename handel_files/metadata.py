from pathlib import Path
import datetime
from services.logger.logger import Logger

logger = Logger.get_logger(index="handel-files-logs")


class MetaData:
    def __init__(self, path):
        logger.info(f"loading json from {path}")
        self.file_path = Path(path)

    def observing_metadata(self):
        # Get the stat_result object
        logger.info('Observing metadata')
        file_stats = self.file_path.stat()
        logger.info("file stat and name are packed in dict")
        return {"File name": self.file_path.name.replace("C:","app"),
                "File size": f"{file_stats.st_size} bytes",
                "Last modified": f"{datetime.datetime.fromtimestamp(file_stats.st_mtime)}",
                "Creation/Metadata change time": f"{datetime.datetime.fromtimestamp(file_stats.st_ctime)}",
                "Last accessed": f"{datetime.datetime.fromtimestamp(file_stats.st_atime)}"
                }
