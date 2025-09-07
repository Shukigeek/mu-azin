from handel_files.metadata import MetaData


class Json:
    def __init__(self,path):
        self.path = path
        self.metadata = MetaData(path).observing_metadata()
    def return_json(self):
        return {"meta data":self.metadata,
                "path":self.path}
if __name__ == '__main__':
    j = Json("../podcasts/download (1).wav")
    print(j.return_json())



