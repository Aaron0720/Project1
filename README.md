# Project  Analyzing Millions of NYC Parking Violations

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
