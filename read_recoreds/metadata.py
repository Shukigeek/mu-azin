from pathlib import Path
import datetime

class MetaData:
    def __init__(self,path):
        self.file_path = Path(path)
    def observing_metadata(self):
        # Get the stat_result object
        file_stats = self.file_path.stat()
        return {"File name":{self.file_path.split("/")[-1]},
                "File size": f"{file_stats.st_size} bytes",
                "Last modified": f"{datetime.datetime.fromtimestamp(file_stats.st_mtime)}",
                "Creation/Metadata change time": f"{datetime.datetime.fromtimestamp(file_stats.st_ctime)}",
                "Last accessed": f"{datetime.datetime.fromtimestamp(file_stats.st_atime)}"
                }

if __name__ == '__main__':
    md = MataData("podcasts/download (1).wav")
    print(md.observing_metadata())