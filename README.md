# Flasker
A boilerplate of flask Restful API + MongoDB + Docker 

## For deployment

#### Build the Containers with Docker Compose

```bash

# Build!
sudo docker-compose up --build --force-recreate 
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

#### Requests

```bash
# Post
curl -v -X POST -H "Content-Type: application/json" -d '{"name":"John Doe","email":"johndoe@example.com"}' localhost:80/user

# Get
curl -v localhost:80/user

# Get by id
curl -v localhost:80/user/<id>

# Update user
curl -v -X PUT -H "Content-Type: application/json" -d '{"name":"John","email":"johndoe@example.com"}' localhost:80/user/<id>

# Delete
curl -v -X DELETE localhost:80/user/<id>
```

## For development

#### Requirements
