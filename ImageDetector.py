import numpy as np 
import cv2
import os


def detector(raw_image, expected_outcome):
    # Setting up parameters
    image_path = str('')
    filename = str(raw_image)
    expected_outcome = expected_outcome
    image_path = str(image_path+filename)
    prototxt_path = 'models/MobileNetSSD_deploy.prototxt.txt'
    model_path = 'models/MobileNetSSD_deploy.caffemodel'
    min_confidence = 0.2
    classes = ["background", "earoplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
    np.random.seed(543210)
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    #Loading the pretrained SSD ModelNet
    net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
    image = cv2.imread(image_path)
    height, width = image.shape[0], image.shape[1]
    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300,300)), 0.007, (300,300), 130)

    #here we take the BLOB and apply the model to it
    net.setInput(blob)
    detected_objects = net.forward()
    
    #Drawing rectangles around the objects we detected
    listofobjects = []
    for i in range(detected_objects.shape[2]):
        confidence = detected_objects[0][0][i][2] #This is a nested list that takes different values try print([0][0][0]) to see the raw value
        if confidence > min_confidence:
            class_index = int(detected_objects[0][0][i][1])
            listofobjects.append(classes[class_index])
            upper_left_x = int(detected_objects[0][0][i][3] * width)
            upper_left_y = int(detected_objects[0][0][i][4] * height)
            lower_right_x = int(detected_objects[0][0][i][5] * width)
            lower_right_y = int(detected_objects[0][0][i][6] * height)
            confidence1 = round(confidence*100)
            prediction_text = f"{classes[class_index]}: {confidence1}%"
            cv2.rectangle(image, (upper_left_x, upper_left_y), (lower_right_x, lower_right_y), colors[class_index],3)
            cv2.putText(image, prediction_text, (upper_left_x, 
                        upper_left_y -15 if upper_left_y > 30 else upper_left_y +15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, colors[class_index],2)
    #uncomment if you want to show the image with the rectangles   
    #cv2.imshow("Detected Objects", image)
    filename = "scanned_"+filename
    path = 'static/tempimages' #saving to temp images folder
    cv2.imwrite(os.path.join(path , filename), image)

    #calculating the outcome:
    ExpectedOutcomeDetected = expected_outcome in listofobjects
    return filename, ExpectedOutcomeDetected, listofobjects
