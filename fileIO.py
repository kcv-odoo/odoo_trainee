import json

contents = {"aa": 12, "bb": 21}
with open("myfile1.txt", "w+") as file:
    file.write(str(contents))       

with open("myfile2.txt", "w+") as file:
    file.write(json.dumps(contents))    #python dictionary to json variable
    #json.dump  - (load data from python variable to json file)
with open('myfile1.txt', "r+") as file:
    contents = file.read()         
print(contents)
with open('myfile2.txt', "r+") as file:
    contents = json.load(file)       #load data from json file into python dictionary
    #json.loads - (load data from json variable into python dictionary)
print(contents)
