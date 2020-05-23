myfile = open ("fruits.txt")
content = myfile.read()
myfile.close()

print(content)

with open ('cancer.txt') for file:
    content = file.read()


import time
import os

while True:
    if os.path.exists("files/vegetables.txt"):
        with open('files/vegetables.txt') as file:
            print(file.read())
            time.sleep(10)
    else:
        print("File does not exist.")
    time.sleep(10)

while True:
    if os.path.exists("files/temps_today.csv"):
        data = pandas.read_csv("files/temps_today.csv")
        print(data.mean()["st1"])
    else:
        print("File does not exist.")
    time.sleep(10)
