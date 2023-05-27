#!/bin/bash

bb=$(tput bold)
nn=$(tput sgr0)
bold=$(tput bold)
norm=$(tput sgr0)
red=$(tput setaf 1)
green=$(tput setaf 2)
yellow=$(tput setaf 3)

echo "${bb}Deploying the applications${nn}"

docker-compose up --build --force-recreate -d

echo "${bb}Setting user on Mongo DB${nn}"

sleep 5

docker exec -it mongodb bash -c '
    # Login with admin user
    mongo -u mongodbuser -p cl3v3rP9ssw0rd --authenticationDatabase admin <<EOF

    # Use the database
    use flaskdb

    # Add user to connect with flask container
    db.createUser({user: "flaskuser", pwd: "f19skp9ssw0rd", roles: [{role: "readWrite", db: "flaskdb"}]})

    # Exit from MongoDB shell
    exit
EOF
'