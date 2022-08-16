from click import option
from apilytics.fastapi import ApilyticsMiddleware
from fastapi import FastAPI, File, UploadFile, Request
from ImageDetectorV1 import detectorV1
from ImageDetectorV2 import detectorV2
from newassignmentV1 import new_assignmentV1
from newassignmentV2 import new_assignmentV2

from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

import uuid
import os

app = FastAPI()
app.add_middleware(ApilyticsMiddleware, api_key="fab9786a-ec56-4743-9d57-a41a53816e86"



#This is just a test enpoint, that should be removed later. But it allows me to verify the backend is running, if the image detector is down. 
@app.get("/", response_class=HTMLResponse)
def read_root():
    return"""
    <html>
        <head>
            <title>PhotoScavenger API </title>
        </head>
        <body>
        <img src="https://user-images.githubusercontent.com/71013416/179624009-d72ba019-3639-438d-8857-dbc061f675a3.png" width="200" height="200" alt="PhotoScavengerLogo">
            <h1> Welcome to the photoscavenger API <h1>
            <hr>
            <h2>How to detect objects using PhotoScavenger API</h2>
                <ul>
                <li>1. Prepare a POST request with an image as file/body </li>
                <li>2. Send that request to to: http://scangame.herokuapp.com/uploadfile/boat or  http://scangame.herokuapp.com/v2/uploadfile/boat</li>
                <li>3. replace boat for an object you think is in the image.</li>
                </ul>
                <hr>
                <h2>How to get an example response</h2>
                <p>Send a call to http://scangame.herokuapp.com/exampleresponse
                <hr>
                <h2> Where to find the documentation? </h2>
                <p>check: https://scangamebackend.herokuapp.com/docs for documentation</p>
                <p>Or check github : https://github.com/two-trick-pony-NL/PhotoScavengerBackend</p>
        </body>
    </html> 
    """


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
        results = detectorV1(rawimage, expectedobject)
        objectfound = results[1]
        otherobjectsdetected = results[2]
        listofobjectsWithConfidence = results[3]
        filename = results[0]
        #remove uploaded image
        os.remove(rawimage)

    return {'Searchedfor:': expectedobject, 'Wasfound': objectfound, 'OtherObjectsDetected': otherobjectsdetected, 'Processed_FileName': filename, 'file_url': rawimage, 'listofobjectsWithConfidence': listofobjectsWithConfidence}
    #return templates.TemplateResponse("index.html", {"request": None, "id": id, 'Searchedfor:': expectedobject, 'Wasfound': objectfound, 'OtherObjectsDetected': otherobjectsdetected, 'Processed_FileName': filename, 'file_url': rawimage})

@app.post("/v2/uploadfile/{expectedobject}")
async def UploadImage(expectedobject, file: bytes = File(...)):
    #Receiving the image the image
    uniqueid = str(uuid.uuid4())
    with open('image'+uniqueid+'.jpg','wb') as image:
    ##Saving te raw image
        rawimage = 'image'+uniqueid+'.jpg'
        image.write(file)
    #Calling the detector
        results = detectorV2(rawimage, expectedobject)
    #Parsing the different results
        objectfound = results[1]
        filename = results[0]
        otherobjectsdetected = results[2]
        #Removing the image uploaded so we don't store any data
        os.remove(rawimage)
    return {'Searchedfor:': expectedobject, 'Wasfound': objectfound, 'OtherObjectsDetected': otherobjectsdetected, 'Processed_FileName': filename}


@app.get("/newassignment/{score}")
def new_assignment(score: int):
    assignment = new_assignmentV1(score)
    return assignment

@app.get("/v2/newassignment/{score}")
def new_assignment(score: int):
    assignment = new_assignmentV2(score)
    return assignment
    


