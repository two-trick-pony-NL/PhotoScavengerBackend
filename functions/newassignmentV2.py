from random import random, choice, randint
from functions.calculateassignment import readassignment



def new_assignmentV2(score: int):
    #Taking the score to determine the difficulty of objects
    if score < 3000: 
        options = readassignment("easy")
    elif score < 6000:
        options = readassignment("medium")
    elif score < 9000:
        options = readassignment("hard")
    else:
        options = readassignment("impossible")

    keysandemojisV2 = {"background":"❓", "earoplane": "✈️","airplane": "✈️", "bicycle":"🚲", "bird": "🦅", "boat":"🚤", "bottle":"🍾", "bus": "🚌", "car":"🚗", "cat": "🐈", "chair": "🪑", "cow":"🐄", "diningtable": "","dining table": "", "dog": "🐕", "horse": "🐎", "motorbike": "🏍","motorcycle": "🏍", "person": "👱‍♂️", "pottedplant":"🪴","potted plant":"🪴", "sheep":"🐑", "sofa": "🛋", "train": "🚂", "tvmonitor": "📺", "truck":"🛻", "traffic light": "🚦", "fire hydrant": "", "stop sign": "🛑", "parking meter": "🅿️", "bench": "", "elephant": "🐘", "bear":"🐻", "zebra": "🦓", "giraffe": "🦒", "backpack":"🎒", "umbrella":"🌂", "handbag": "👜", "tie":"👔", "suitcase":"🧳", "frisbee":"🥏", "skis":"🎿", "snowboard":"🏂", "sports ball":"🏀", "kite":"🪁", "baseball bat": "⚾️", "baseball glove": "⚾️", "skateboard":"🛹", "surfboard":"🏄🏻", "tennis racket":"🎾", "wine glass":"🍷", "cup":"🥛", "fork":"🍴", "knife":"🍴", "spoon":"🥄", "bowl":"🥣", "banana":"🍌", "apple":"🍎", "sandwich":"🥪", "orange":"🍊", "broccoli":"🥦", "carrot":"🥕", "hot dog":"🌭", "pizza":"🍕", "donut":"🍩", "cake":"🍰", "couch":"🛋", "bed":"🛌","toilet":"🚽", "tv":"📺", "laptop":"💻", "mouse":"🖱", "remote":"📺", "keyboard":"⌨️", "cell phone":"📱", "microwave":"☢️", "oven":"♨️", "toaster":"", "sink":"🚰", "refrigerator":"🥶", "book":"📚", "clock":"⏱", "vase":"🏺", "scissors":"✂️", "teddy bear":"🧸", "hair drier":"💨", "toothbrush":"🪥"}

    NumberOfItems = len(options)-1
    randomnumber = randint(0,NumberOfItems)
    assignment = options[randomnumber]
    emoji = keysandemojisV2[assignment]
    #emoji = 1
    return {assignment: emoji}