#!/bin/sh
uvicorn main:app -w 2 --access-logfile - --threads 2 -b 0.0.0.0:80