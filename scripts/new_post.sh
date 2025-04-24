#! /bin/bash

POST_TITLE=$1
POST_DATE=$(date +'%Y-%m-%d')

hugo new content home/$POST_TITLE.md
