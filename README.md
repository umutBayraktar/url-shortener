# url-shortener

This is a really simple URL shortener project. It has 2 endpoints. One of them uses for creating shorted urls, the other one uses for going to the original url.
The system consists of 3 parts.  URL Shorterer is a Django Project. It takes urls as parameters and hashes them using the md5 hashing algorithm then It saves hash values and original URLs to PostgreSQL database. Also, it uses Redis for caching to decrease database queries.

## Creating Short Urls

**Endpoint**	
	[POST]   short/ 

   Endpoint uses for creating short URLs. It takes one parameter in the request body and it creates a shorted URL

  **Request Body**

    {
	
	"url":"https://example.com/"
	}
	

## Using Shoted Urls

  **Endpoint**

    [GET] /short/<shorted-url-hash>/
    
for instance
	
		/short/ac509b064b/

	
# Start Docker Compose
## Fork and Clone The Project
	git clone git@github.com:umutBayraktar/url-shortener.git
go to the docker folder

	cd docker
run docker compose file

	docker-compose -f compose/docker-compose-local.yaml up --build

  

if you have postgresql connection error probably you need to create a database

## Creating Database

1- Start project with docker-compose

	docker-compose -f compose/docker-compose-local.yaml up

2- Open second terminal and connect postgresql container

	docker exec -it urlshortener-postgres /bin/bash

3- login database

	su - postgres

	psql

4 -create database

	create database urlshorter;

It will connect automatically. If it doesn't, you can kill the docker-compose with Ctrl + C and restart again with 

	docker-compose -f compose/docker-compose-local.yaml up	
command


## Running  Unit Tests

Start Project

		docker-compose -f compose/docker-compose-local.yaml up	

Open second terminal and connect urlshorterer app

	docker exec -it urlshortener-app /bin/bash
Run test command

	python manage.py test

