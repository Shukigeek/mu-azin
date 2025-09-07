file_path = "path/to/your/audio.wav"
with open(file_path, "rb") as f:
    wav_data = f.read()

# Store the binary data
document = {"filename": "audio.wav", "data": Binary(wav_data)}
collection.insert_one(document)
print(f"File 'audio.wav' uploaded successfully.")