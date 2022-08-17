from click import option
from fastapi import FastAPI, File, UploadFile, Request
from ImageDetectorV1 import detectorV1
from ImageDetectorV2 import detectorV2
from newassignmentV1 import new_assignmentV1
from newassignmentV2 import new_assignmentV2
from fastapistats import Stats
import json
from fastapi.templating import Jinja2Templates
import os


from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
templates = Jinja2Templates(directory=os.path.abspath(os.path.expanduser('templates')))


import uuid
import os

app = FastAPI()
update = Stats.update_stats


@app.get('/', response_class=HTMLResponse)
@update(name='Homepage') 
def read_root(request: Request):
    f = open('stats.json')
    data = json.load(f)
    length_of_data = len(data)
    values = list(data.values())
    keys = list(data.keys())
    return templates.TemplateResponse('index.html', {'request': request, 'data': data, 'keys':keys, 'values':values, 'length':length_of_data})


@app.get('/exampleresponse')
@update(name='ExampleResponse') 
def exampleresponse():
    return {'Searchedfor:':'boat','Wasfound':'NO','OtherObjectsDetected':['person','person','person','person','bicycle','motorbike','bicycle','motorbike','bicycle'],'Processed_FileName':'scanned_image54e46fb8-93f8-43ad-a8ec-99eb83f260af.jpg','file_url':'image54e46fb8-93f8-43ad-a8ec-99eb83f260af.jpg','listofobjectsWithConfidence':[{'person':100},{'person':100},{'person':100},{'person':100},{'bicycle':97},{'motorbike':91},{'bicycle':75},{'motorbike':48},{'bicycle':28}]}


# This endpoint triggers for this API call: 127.0.0.1:8000/uploadfile/cat. 
#Add a image to your call in the body, and set a expected object in the URL. 
#The function then runs the AI model to see if the picture contains the expected object
@app.post('/uploadfile/{expectedobject}')
@update(name='uploadfileV1') # if the name kwarg is not passed it will default to the function name
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
    #return templates.TemplateResponse('index.html', {'request': None, 'id': id, 'Searchedfor:': expectedobject, 'Wasfound': objectfound, 'OtherObjectsDetected': otherobjectsdetected, 'Processed_FileName': filename, 'file_url': rawimage})

@app.post("/v2/uploadfile/{expectedobject}")
@update(name='uploadfileV2')
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


@app.get('/newassignment/{score}')
@update(name='NewAssignmentV1') # if the name kwarg is not passed it will default to the function name
def new_assignment(score: int):
    assignment = new_assignmentV1(score)
    return assignment

@app.get('/v2/newassignment/{score}')
@update(name='NewAssignmentV2') # if the name kwarg is not passed it will default to the function name
def new_assignment(score: int):
    assignment = new_assignmentV2(score)
    return assignment
    
@app.get('/healthcheck')
@update(name='Healtcheck by AWS')
def healthcheck():
    return 'Server is up'