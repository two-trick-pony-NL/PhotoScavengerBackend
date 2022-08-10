

<img src="https://user-images.githubusercontent.com/71013416/183674037-eca7cc9b-4a19-494c-a449-af638fdd869c.png" width="250">



![Download_on_the_App_Store_Badge svg](https://user-images.githubusercontent.com/71013416/183876659-380ec479-f8b1-473d-83e4-6becaa8583cd.png)(https://apps.apple.com/nl/app/photo-scavenger/id1637234234?l=en)


# Photoscavenger App
This is the FastAPI backend that supports my PhotoScavenger Apps. It can detect certain objects from pictures. This API serves my iOS/Android apps for the game here: https://photoscavenger.petervandoorn.com

Here is a in-game screenshot: <br>
![ezgif com-gif-maker](https://user-images.githubusercontent.com/71013416/178448499-3f547173-43ab-41b2-967a-a1f9ae8dd9a0.gif)

- API  [documentation](https://photoscavenger.vdotvo9a4e2a6.eu-central-1.cs.amazonlightsail.com/docs).
- App on [appstore](https://apps.apple.com/nl/app/photo-scavenger/id1637234234?l=en)

# What does it do:
This backend can check images to see if a certain object is on the picture. For instance: you can check if there is a cat on a particular photo. The backend will then return a false or true for that object depending on whether it was found. It will also return a list objects it managed to find. This allows you validate in case of false negatives, to see what the model thought was on the picture. See an example below. 

# How does it work: 
you make a POST request with a image in the formdata (content type 'file'). 
For instance this image: 

![Schermafbeelding 2022-06-18 om 11 26 33](https://user-images.githubusercontent.com/71013416/175918302-bd99786a-9d4f-49d7-a90c-9bbbff847035.png)

and it returns an image with the detected objects:
![scanned_imagee0dee0c1-3512-4617-8a3d-4d19b80c85e7](https://user-images.githubusercontent.com/71013416/177133306-d0eab947-6013-4925-94ce-dccb3106af1a.jpg)

# How to run: 

Simply clone the repo and run: 
```
gh repo clone two-trick-pony-NL/ScanGameBackend && cd ScanGameBackend
```
 
```
uvicorn main:app --host 0.0.0.0 --port 80 --reload
```

# V1 vs V2 
The V1 API has 18 objects to be detected and V2 can detect 80 different objects 
Their endpoinsta are: 
- V1: https://photoscavenger.vdotvo9a4e2a6.eu-central-1.cs.amazonlightsail.com/uploadfile/person
- V2: https://photoscavenger.vdotvo9a4e2a6.eu-central-1.cs.amazonlightsail.com/v2/uploadfile/person 



# Request / Response -- Local

Call
```
http://localhost:80/v2/uploadfile/bicycle
```

or 
```
http://localhost:80/uploadfile/person
```

Response (for bicycle)
```
{
    "Searchedfor:": "person",
    "Wasfound": "YES",
    "OtherObjectsDetected": [
        "person",
        "person",
        "person",
        "person",
        "chair",
        "person",
        "chair",
        "boat",
        "bird",
        "person",
        "person"
    ],
    "Processed_FileName": "imagecfb104fe-8347-4ef5-b733-2a0d3d8e6b88.jpg"
}
```
Supported objects in V1
```
["background", "earoplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
```

Supported objects in V2 
```
person
bicycle
car
motorcycle
airplane
bus
train
truck
boat
traffic light
fire hydrant
stop sign
parking meter
bench
bird
cat
dog
horse
sheep
cow
elephant
bear
zebra
giraffe
backpack
umbrella
handbag
tie
suitcase
frisbee
skis
snowboard
sports ball
kite
baseball bat
baseball glove
skateboard
surfboard
tennis racket
bottle
wine glass
cup
fork
knife
spoon
bowl
banana
apple
sandwich
orange
broccoli
carrot
hot dog
pizza
donut
cake
chair
couch
potted plant
bed
dining table
toilet
tv
laptop
mouse
remote
keyboard
cell phone
microwave
oven
toaster
sink
refrigerator
book
clock
vase
scissors
teddy bear
hair drier
toothbrush
```

# Getting a new assignment
Note: Corrospond the right assignment API with the correct image detector API. As the V1 version will only know the 18 classes that AI model has. Also, the integer at the end of the call is the score the player currently has. The higher the score the more difficult the object is to find. 

### V1
```
http://localhost:8000/newassignment/2000
```

### V2
```
http://localhost:8000/v2/newassignment/2000
```

response:
```
{"dog":"🐕"}
```


