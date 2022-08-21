#!/bin/sh
#uvicorn main:app --host=0.0.0.0 --port 80
gunicorn app:app -w 4 --threads 2 -b 0.0.0.0:80