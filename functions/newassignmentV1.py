from random import random, choice, randint


def new_assignmentV1(score: int):
    #Taking the score to determine the difficulty of objects
    if score < 500: 
        options = ["chair", "bottle", "sofa", "tvmonitor"]
    elif score < 2000:
        options = [ "bicycle",  "car",  "diningtable",  "person", "pottedplant", "sofa", "train"]
    elif score < 4000:
        options =  ["bird", "bottle", "bus", "car", "cat", "chair", "dog", "motorbike", "person", "tvmonitor"]
    else:
        options = ["earoplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

    keysandemojis = {"background":"❓", "earoplane": "✈️", "bicycle":"🚲", "bird": "🦅", "boat":"🚤", "bottle":"🍾", "bus": "🚌", "car":"🚗", "cat": "🐈", "chair": "🪑", "cow":"🐄", "diningtable": "", "dog": "🐕", "horse": "🐎", "motorbike": "🏍", "person": "👱‍♂️", "pottedplant":"🪴", "sheep":"🐑", "sofa": "🛋", "train": "🚂", "tvmonitor": "📺"}
    NumberOfItems = len(options)-1
    randomnumber = randint(0,NumberOfItems)
    assignment = options[randomnumber]
    emoji = keysandemojis[assignment]
    print(score)
    return {assignment: emoji}