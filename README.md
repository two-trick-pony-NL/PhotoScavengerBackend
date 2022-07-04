# ScanGameBackend
This is the FastAPI backend that supports my ScanGame Apps. It can detect certain objects 

# Companion apps: 
- This API serves my React Native apps for the game here: https://github.com/two-trick-pony-NL/ScanGameApps

![IMG_2749](https://user-images.githubusercontent.com/71013416/177129166-3392465b-48cd-4d37-a28c-4201054d5c33.PNG)


# What does it do:
This backend can check images to see if a certain object is on the picture. For instance: you can check if there is a cat on a particular photo. The backend will then return a false or true for that object depending on whether it was found. It will also return a list objects it managed to find. This allows you validate in case of false negatives, to see what the model thought was on the picture. See an example below. 

# How does it work: 
you make a POST request with a image in the formdata (content type 'file'). 
For instance this image: 

![Schermafbeelding 2022-06-18 om 11 26 33](https://user-images.githubusercontent.com/71013416/175918302-bd99786a-9d4f-49d7-a90c-9bbbff847035.png)

and it returns an image with the detected objects:
![scanned_imagee0dee0c1-3512-4617-8a3d-4d19b80c85e7](https://user-images.githubusercontent.com/71013416/177133306-d0eab947-6013-4925-94ce-dccb3106af1a.jpg)


# Request / Response

Call
```
http://localhost:80/uploadfile/bicycle
```

or 
```
http://localhost:80/uploadfile/person
```

Response (for bicycle)
```
{
    "Searchedfor:": "bicycle",
    "Wasfound": true,
    "OtherObjectsDetected": [
        "person",
        "person",
        "person",
        "person",
        "bicycle",
        "motorbike",
        "bicycle",
        "motorbike",
        "bicycle"
    ],
    "Processed_FileName": "scanned_imagec463b876-f050-43f6-b6a8-9c0235f5691d.jpg",
    "file_url": "imagec463b876-f050-43f6-b6a8-9c0235f5691d.jpg"
}
```
Supported objects
```
["background", "earoplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
```

