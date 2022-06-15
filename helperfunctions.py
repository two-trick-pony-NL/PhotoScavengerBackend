def ReadLabels(): #Reading the file with all the objects the AI can detect and converting it to a list
    file = open("objectlabels.txt", "r")
    objectlabels = [(line.strip()) for line in file]
    file.close()
    
    #The  file with objectlabels is not aligned with the trained model. 
    #I have to sort this out, for now I hardcoded this list that is known
    objectlabels = ["background", "earoplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
    return(objectlabels)