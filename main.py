from datetime import datetime
from fileinput import filename
from fastapi import FastAPI, File, UploadFile
from pymysql import Timestamp
from ImageDetector import detector
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
    timestamp = str(datetime.now())
    with open('image'+timestamp+'.jpg','wb') as image:
        rawimage = 'image'+timestamp+'.jpg'
        os.chdir('tempimages')
        image.write(file)
        image.close()
        os.chdir('..')
        print(rawimage)
        
        print(detector(rawimage, expectedobject))
    return {'got it', 'hello'}