import os

# count the number of collisions for every experiments

def filenum(index):
    path = './'+str(index)
    files = os.listdir(path)
    num = len(files)
    return num

for index in range(0,600):
    print index, filenum(index)-1
