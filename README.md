# Flasker
A boilerplate of flask Restful API + MongoDB + Nginx + Docker 

## :bookmark: Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://www.docker.com/)

## :triangular_flag_on_post: Starting

```bash
#Clone the project
git clone https://github.com/arielroque/memory-safety.git

#Enter in the folder 
cd memory-safety

## Tl;dr

```bash
# Deploy 
./deploy.sh
```

## :building_construction: For deployment

#### Build the Containers with Docker Compose

```bash
# Build
sudo docker-compose up --build --force-recreate

# Build recreating the containers
#sudo docker-compose up --build --force-recreate 
```

#### Configure the credenctials to conect Flask with Mongo database container

```bash
#Go to mongodb container
 docker exec -it mongodb bash
 
#Login with admin user
mongo -u mongodbuser -p cl3v3rP9ssw0rd

#Use the  database
use flaskdb

#Add user to connect with flask container
db.createUser({user: 'flaskuser', pwd: 'f19skp9ssw0rd', roles: [{role: 'readWrite', db: 'flaskdb'}]})
exit
```

## :microscope: Making Requests

```bash
# Add a new user
curl -v -X POST -H "Content-Type: application/json" -d '{"name":"John Doe","email":"johndoe@example.com"}' localhost:80/user

# Get the users
curl -v localhost:80/user

# Get an user by id
curl -v localhost:80/user/<id>

# Update an user
curl -v -X PUT -H "Content-Type: application/json" -d '{"name":"John","email":"johndoe@example.com"}' localhost:80/user/<id>

# Delete an user
curl -v -X DELETE localhost:80/user/<id>
```

## :confused: Uninstall

```bash
docker-compose down
```