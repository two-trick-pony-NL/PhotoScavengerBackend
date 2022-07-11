from random import random, choice, randint
from click import option
from fastapi import FastAPI, File, UploadFile, Request
from ImageDetector import detector
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uuid
import os

app = FastAPI()
#Setting up static folder and templates in case we want to host a landing page in the future
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

#This is just a test enpoint, that should be removed later. But it allows me to verify the backend is running, if the image detector is down. 
@app.get("/")
def read_root():
    return {"How to use:": "Send a POST request with an image as file/body to: http://scangamebackend.herokuapp.com/uploadfile/boat and replace boat for an object you think is in the image."}



@app.get("/exampleresponse")
def exampleresponse():
    return {"Searchedfor:":"boat","Wasfound":"NO","OtherObjectsDetected":["person","person","person","person","bicycle","motorbike","bicycle","motorbike","bicycle"],"Processed_FileName":"scanned_image54e46fb8-93f8-43ad-a8ec-99eb83f260af.jpg","file_url":"image54e46fb8-93f8-43ad-a8ec-99eb83f260af.jpg","listofobjectsWithConfidence":[{"person":100},{"person":100},{"person":100},{"person":100},{"bicycle":97},{"motorbike":91},{"bicycle":75},{"motorbike":48},{"bicycle":28}]}


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
        #results = "'scanned_imaged36f9ea0-b059-4217-838d-c2f1b9cc58e9.jpg', False, ['pottedplant', 'pottedplant']"
        print(results)
        objectfound = results[1]
        otherobjectsdetected = results[2]
        listofobjectsWithConfidence = results[3]
        filename = results[0]
        os.remove('image'+uniqueid+'.jpg')

    return {'Searchedfor:': expectedobject, 'Wasfound': objectfound, 'OtherObjectsDetected': otherobjectsdetected, 'Processed_FileName': filename, 'file_url': rawimage, 'listofobjectsWithConfidence': listofobjectsWithConfidence}
    #return templates.TemplateResponse("index.html", {"request": None, "id": id, 'Searchedfor:': expectedobject, 'Wasfound': objectfound, 'OtherObjectsDetected': otherobjectsdetected, 'Processed_FileName': filename, 'file_url': rawimage})

@app.get("/newassignment")
def new_assignment():
    keysandemojis = {"background":"❓", "earoplane": "✈️", "bicycle":"🚲", "bird": "🦅", "boat":"🚤", "bottle":"🍾", "bus": "🚌", "car":"🚗", "cat": "🐈", "chair": "🪑", "cow":"🐄", "diningtable": "❓", "dog": "🐕", "horse": "🐎", "motorbike": "🏍", "person": "👱‍♂️", "pottedplant":"🪴", "sheep":"🐑", "sofa": "🛋", "train": "🚂", "tvmonitor": "📺"}
    options = ["earoplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
    #Shortened the list for easier photographing during testing
    #options = ["bottle", "cat", "chair", "diningtable", "person", "pottedplant", "sofa", "tvmonitor"]
    NumberOfItems = len(options)-1
    randomnumber = randint(0,NumberOfItems)
    assignment = options[randomnumber]
    emoji = keysandemojis[assignment]
    return {assignment: emoji}
