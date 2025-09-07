from mongo.mongo_dal import Connection
from bson.binary import Binary

class WriteToMongo:
    def __init__(self):
        self.conn = Connection()
        self.client = self.conn.connect()
        self.db = self.client[self.conn.db]
        self.collection = self.db["audio files"]
    def write(self, path,name,ID):
        with open(path, "rb") as f:
            wav_data = f.read()

        # Store the binary data
        document = {"_id":ID,"filename": name, "data": Binary(wav_data)}
        self.collection.insert_one(document)
        print(f"File 'audio.wav' uploaded successfully.")

if __name__ == '__main__':
    w = WriteToMongo()
    w.write("../podcasts/download (1).wav","audio.wav",98765)

