#!/bin/bash

cd `dirname $0`

python3 manage.py runserver 0.0.0.0:8080
