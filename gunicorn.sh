#!/bin/sh
uvicorn main:app --host=0.0.0.0 --port 80 --workers 2
#gunicorn main:app -w 4 --threads 2 -b 0.0.0.0:80