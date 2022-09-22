import wget
import csv
import os

try:
    os.mkdir("fotolar")
except:
    pass

list_basarisiz = []
with open("lastss.txt","r") as f:
    line = csv.reader(f)

    for i in line:
        try:
          wget.download(i[0],"fotolar")
        except:
            list_basarisiz.append(i)
