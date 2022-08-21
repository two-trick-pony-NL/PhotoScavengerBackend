#!/bin/sh
uvicorn main:app --host=0.0.0.0 --port 80 --workers 4