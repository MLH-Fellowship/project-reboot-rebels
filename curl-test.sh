#!/bin/bash

curl -request POST http://127.0.0.1:5000/api/timeline_post -d 'name=Roa&email=brahimiroa@gmail.com&content=Testing!' && curl --request GET http://127.0.0.1:5000/api/timeline_post | jq '.'