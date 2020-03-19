# Project  Analyzing Millions of NYC Parking Violations
Part 1: Python Scripting

main.py

Dockerfile

requirements.txt

src-api.py

$ docker build -t bigdata1:1.0 .

$ docker run -v $(pwd):/app -e APP_KEY={my app_key} -it bigdata1:1.0 /bin/bash

$ docker run -v $(pwd):/app -e APP_KEY={my app_key} -it bigdata1:2.0 python -m main --page_size=3 --num_pages=1 

$ docker images

$ docker tag 660c5854d4de aaronhan0720/bigdata1:1.0

$ docker push aaronhan0720/bigdata1

$ ssh -i "lecture_2_in_class.pem" ubuntu@ec2-3-134-100-9.us-east-2.compute.amazons.com







Part 2: Loading into ElasticSearch

>Dockerfile

>docker-compose.yml

>main.py

>requirements.txt

>src
   >api.py

Elastic Search

$ docker-compose build pyth

$ docker-compose up -d

$ docker-compose run -e APP_KEY={my app_key} -v ${PWD}:/app pyth python -m main --page_size=1000 --num_pages=4 --elastic=True
