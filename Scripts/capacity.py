print("Set the capacity of the Backend at AWS")


set_nodes = input("How many duplicate nodes do you want to run?\n\n")
set_notes = str(set_nodes)

set_power = input("What Power do you want to use pick from: nano $7 | micro $10 | small $15 | medium $40 | large $80 | xlarge $160\n\n")
set_power = str(set_power)

#import subprocess
#result = subprocess.run(, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


import os

os.system("aws lightsail update-container-service --service-name photoscavenger --scale " +set_nodes+" --power "+set_power)