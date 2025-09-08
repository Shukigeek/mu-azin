from handling_topics.consuming_topic import Manager


"""
creating a unique id based on the file name (hash)

and dividing it to two parts 
the metadata is sand it to index in elasticsearch 
and the path + the actual audio data it sands to
restored in mongo db in database called mu'azins
in a collection called audio files
"""
m = Manager()
m.read_from_kafka_saving_elastic_mongo()