from datetime import datetime
from fileinput import filename
from unittest import result
from fastapi import FastAPI, File, UploadFile
from ImageDetector import detector
import uuid
import os

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# This endpoint triggers for this API call: 127.0.0.1:8000/uploadfile/cat. 
#Add a image to your call in the body, and set a expected object in the URL. 
#The function then runs the AI model to see if the picture contains the expected object
@app.post("/uploadfile/{expectedobject}")
async def UploadImage(expectedobject, file: bytes = File(...)):
    uniqueid = str(uuid.uuid4())
    with open('image'+uniqueid+'.jpg','wb') as image:
        rawimage = 'image'+uniqueid+'.jpg'
        os.chdir('static')
        image.write(file)
        image.close()
        os.chdir('..')
        results = detector(rawimage, expectedobject)
        objectfound = results[1]
        otherobjectsdetected = results[2]
        filename = results[0]
        os.remove('image'+uniqueid+'.jpg')
    return {'Searchedfor:': expectedobject, 'Wasfound': objectfound, 'OtherObjectsDetected': otherobjectsdetected, 'Processed_FileName': filename}