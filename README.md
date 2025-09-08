
mu'azin  project


a pipeline project that 
get a wav files of podcasts
we extract all the metadata and the absolute path
than saving it to a json format 

kafka producer sanding the json one by one 
in a specific topic

all of that is warp in a 1 container by docker


phase2 
 
kafka consumer getting the massages by listening (forever)
to the topic in kafka 
at the same time it taking the massages 
creating a unique id based on the file name (hash)

and dividing it to two parts 
the metadata is sand it to index in elasticsearch 
and the path + the actual audio data it sands to
restored in mongo db in database called mu'azins
in a collection called audio files

and all of that it also warp in a container by docker


the file system 

mu'azins/ 
├── .gitignore 
├── docker-compose.yml 
├── elastic/ 
│ └── elastic_base.py 
├── handel_files/ 
│ ├── build_json.py 
│ │── metadata.py 
│ │── sand_to_kafka.py 
│ │── requirements.txt 
│ └── Dockerfile 
├── handling_topics/ 
│ ├── consuming_topic.py 
│ │── main.py 
│ │── requirements.txt
│ └── Dockerfile
├── kafka_pub_sub/ 
│ │── pub/ 
│ │  └── producer.py
│ └── sub/
│    └── consumer.py 
├── mongo/ 
│ ├── mongo_dal.py
│ └── write_to_mongo.py
└── manager.py

