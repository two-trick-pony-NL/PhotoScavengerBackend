# ScanGameBackend
This is the FastAPI backend that supports my ScanGame Apps, check them out here: https://github.com/two-trick-pony-NL/ScanGameApps

# What does it do:
This backend takes a POST request for an image and an expected object on that image (e.g. "Cat") then the backend will return a JSON response that tells you if it found the objects in that image. 

# How does it work: 

Call
```
http://localhost:80/uploadfile/bicycle
```

Response
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
