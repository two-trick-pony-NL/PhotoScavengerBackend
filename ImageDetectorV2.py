

import torch
import pandas

min_confidence = float(0.2)

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5x')  # or yolov5n - yolov5x6, custom




def detectorV2(raw_image, expected_outcome):
    print("Detecting with V2 detector")
    # Images
    filename = str(raw_image)
    img = filename  # or file, Path, PIL, OpenCV, numpy, list

    # Inference
    results = model(img)

    # Results
    print("\n\n########################### \n\n")
    print("Raw detection results:")
    print(results.pandas().xyxy[0])  # im predictions (pandas)
    Detection = results.pandas().xyxy[0]
    #Detection results into a pandas dataframe 
    #      xmin    ymin    xmax   ymax  confidence  class    name
    # 0  749.50   43.50  1148.0  704.5    0.874023      0  person
    # 2  114.75  195.75  1095.0  708.0    0.624512      0  person
    # 3  986.00  304.00  1028.0  420.0    0.286865     27     ti

    #Removing the lower confindence items found
    remove_min_confidence = Detection['confidence'] > min_confidence
    Detection = Detection[remove_min_confidence]


    print("\n\n########################### \n\n")
    print("List of Objects -- Confidence > " +min_confidence)


    listofobjects = Detection['name'].tolist()
    print(listofobjects)
    if expected_outcome in listofobjects:
        ExpectedOutcomeDetected1 = 'YES'
    else:
        ExpectedOutcomeDetected1 = 'NO'
    
    filename = raw_image


    return filename, ExpectedOutcomeDetected1, listofobjects
