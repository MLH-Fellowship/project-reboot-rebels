#!/bin/bash

cd ./cyber-sapiens
git fetch && git reset origin/main --hard

#docker compose
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build