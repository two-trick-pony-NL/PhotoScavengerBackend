#!/bin/sh
gunicorn -w 4 -k uvicorn.workers.UvicornWorker -host=-0.0.0.0 -port=80