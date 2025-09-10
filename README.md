# mu'azin  project

## handel files

``
runs from the docker file in handel files directory
``

a pipeline project that 
get a wav files of podcasts
we extract all the metadata and the absolute path
than saving it to a json format 

kafka producer sanding the json one by one 
in a specific topic

all of that is warp in a 1 container by docker


## handling topics
``
runs from docker file in handling topics dirctory
``
 
kafka consumer getting the massages by listening (forever)
to the topic in kafka 
at the same time it taking the massages 
creating a unique id based on the file name (hash)
and saving the name also that we got out of 
the metadata

and dividing it to two parts 
the metadata is sand it to index in elasticsearch 
and the path + the actual audio data it sands to
restored in mongo db in database called mu'azins
in a collection called audio files

and all of that it also warp in a container by docker


## Explosive mission

``
all loggs in code is from the logger dyrctory
``

logging added to all the cone line and functions
and the logging is also saved to index log in 
elasticsearch


## speach to text

``
runs from the docker file in stt dirctory
``

the app is a server runs by docker container 
thet takes all id + data (bytes) 
from mongodb by sanding it from mongo
in kafka topic that we going to have trak what is already 
inserted to mongo 
and converting each doc binary-text to a readable text 
than updating elastic search with another filed to
by index (this is of course the must important filed)
by its unique ID


the reason I chose to do it in another server that takes 
much longer process and resources and not to do so 
while consuming the data to convert it to text

it because for my understanding kafka is a high speed
stream of data and I do not want to slow the all process
to convert to text that takes vary long time 
and also if the converting isn't working 
at the all metadata + raw audio (in byte) is saved to   
mongodb in vary high speed past
and I can convert all audio to get the text
after a while that all is working
this is inspired by the Asynchrony idea!!
all the data flow is by kafka first to make sure 
that we're not losing anything and not doing the same 
operation un the same data twice

## content_classification


``
run from the docker file in content_classsifiction dirctory
``

this app is consuming id from kafka of all the 
docs in elastic that have already a text box updated in them
and by doing calculation on the data we conclude each 
podcast if is a bds supported and hostile level and then writing it 
back to the index in elastic


(now I did a calculation that let's say we have 
3 - vary hostile words
3 - less hostile words
out of a 50 words podcast
(so 6/53 is two times bigger than 3/53 )
I'm added 3 in order not to be bigger than 100 % if all words are 
very hostile)

## endpoints

``
runs from docker file in endpoints dirctory
``

I gave the user a chance to use elastic
by entering a word or sentence and 
a list of podcast that have that 
going to show from high score (matching) to low.



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
│
├── STT/
│ ├── read_from_mongo.py
│ ├── audio_to_text.py
│ ├── main.py
│ ├── Dockerfile
│ └── requirements.txt
│
├── docker-compose.yml
└── README.md

