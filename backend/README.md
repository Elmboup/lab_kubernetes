# Employee backend api 
  
  This api is build with fastapi framework
  It's a small entreprise api that host employees informations in a postgres database
  
  This work is based on https://github.com/mbenguosta-inner-source/DevOps-Course.git
  
  Run locally
  ## Docker
  ```sh
docker build -t my-flash-app .
```
### Network creation
```sh
docker network create my-net
```
### Pull the postgres image
```sh
docker pull postgres
```

### create your database container
```sh
docker run -d -p 5433:5432 --name postgres_database \
  --network my-net \
  -v my-volume:/var/lib/postgresql/data \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=passer \
  -e POSTGRES_DB=mydatabase \
  postgres
```

### create the flask-app container
```sh
docker run -d -p8000:8000 --name FlaskApp \
--network my-net \
-e DATABASE_HOST=mydatabase \
-e DATABASE_PORT=5432 \ 
-e DATABASE_USER=user \
-e DATABASE_PASSWORD=passer  \
my-flask-app
```

Navigate to your app on localhost:8000 

## Docker compose
### Run compose

Go to your terminal and execute the following command : make sur to be in the docker-compile.yml 's directory

```sh
docker-compose up 
```
Make sur to be in the docker-compile.yml 's directory
