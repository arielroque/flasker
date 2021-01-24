# Flasker
A boilerplate of flask Restful API + MongoDB + Docker 

## For deployment

#### Build the Containers with Docker Compose

```bash

# Build!
sudo docker-compose up
```

#### Configure the credenctials to conect Flask with Mongo database container

```bash
#Go to mongodb container
 docker exec -it mongodb bash
 
#Login with admin user
mongo -u mongodbuser -p cl3v3rP9ssw0rd

#Use the  database
use 

#Add user to connect with flask container
db.createUser({user: '', pwd: '', roles: [{role: 'readWrite', db: ''}]})
```

## For development

#### Requirements
