import os
import numpy as np
import matplotlib.pyplot as plt

import pickle
import random
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from PIL import Image
import csv

dir = "C:\\ISIC_2019_Training_Input"

#with open('Book1.csv') as file_obj:
#    reader_obj = csv.reader(file_obj)

#    for row in reader_obj:
 #       rowee.append(row[0:2])

tuplesList = []
melanoma = []
nv = []
bcc = []
ak = []
bkl = []
df = []
vasc = []
scc = []
unk = []
with open('ISIC_2019_Training_GroundTruth (3).csv') as file_une:
    file_deux = csv.reader(file_une)

    for row in file_deux:
        tuplesList.append(row)

print(len(tuplesList))
for i in tuplesList:
    if i[10]=='1':
        melanoma.append(f"{i[0]}.jpg")
    elif i[10]=='2':
        nv.append(f"{i[0]}.jpg")
    elif i[10]=='3':
        bcc.append(f"{i[0]}.jpg")
    elif i[10]=='4':
        ak.append(f"{i[0]}.jpg")
    elif i[10]=='5':
        bkl.append(f"{i[0]}.jpg")
    elif i[10]=='6':
        df.append(f"{i[0]}.jpg")
    elif i[10]=='7':
        vasc.append(f"{i[0]}.jpg")
    elif i[10]=='8':
        scc.append(f"{i[0]}.jpg")
    elif i[10]=='9':
        unk.append(f"{i[0]}.jpg")

    #print(i[0],i[10], end="\n")

"""
print("Melanoma : \n"+"total imgs : "+ f"{len(melanoma)}"+"\n")

print(melanoma)

print("Nevus : \n"+"total imgs : "+f"{len(nv)}"+"\n")
#print(nv)

print("BCC : \n"+"total imgs : "+ f"{len(bcc)}"+"\n")
#print(bcc)

print("AK : \n"+"total imgs : "+f"{len(ak)}"+"\n")
#print(ak)

print("BKL : \n"+"total imgs : "+f"{len(bkl)}"+"\n")
#print(bkl)

print("DF : \n"+"total imgs : "+f"{len(df)}"+"\n")
#print(df)

print("VASC : \n"+"total imgs : "+f"{len(vasc)}"+"\n")
#print(vasc)

print("SCC : \n"+"total imgs : "+f"{len(scc)}"+"\n")
#print(scc)

print("UNK : \n"+"total imgs : "+f"{len(unk)}"+"\n")
#print(unk)

print(len(melanoma)+len(nv)+len(bcc)+len(ak)+len(bkl)+len(df)+len(vasc)+len(scc)+len(unk))
        # if rowee[1] == '0':

        # print(rowee[1])
#print(rowee[][1])
#os.mkdir('melanoma')
#os.mkdir('nv')
#os.mkdir('bcc')
os.mkdir('ak')
os.mkdir('bkl')
os.mkdir('df')
os.mkdir('vasc')
os.mkdir('scc')
"""
#print(nv)
countList = []
#j = 0
for j in range(0,25001,1000):

    countList.append(j)

#print(countList)

i = 0

for imgs in os.listdir(dir):
    imgpath = os.path.join(dir, imgs)
    i=i+1
    img = Image.open(imgpath)
    if imgs in melanoma:
        img.save('C:\\SCDProject\\svmModel\\MEL\\' + imgs)
    elif imgs in nv:
        img.save('C:\\SCDProject\\svmModel\\NV\\' + imgs)
    elif imgs in bcc:
        img.save('C:\\SCDProject\\svmModel\\BCC\\' + imgs)
    elif imgs in ak:
        img.save('C:\\SCDProject\\svmModel\\AK\\' + imgs)
    elif imgs in bkl:
        img.save('C:\\SCDProject\\svmModel\\BKL\\' + imgs)
    elif imgs in df:
        img.save('C:\\SCDProject\\svmModel\\DF\\' + imgs)
    elif imgs in vasc:
        img.save('C:\\SCDProject\\svmModel\\VASC\\' + imgs)
    elif imgs in scc:
        img.save('C:\\SCDProject\\svmModel\\SCC\\' + imgs)
    elif imgs in unk:
        img.save('C:\\SCDProject\\svmModel\\UNK\\' + imgs)

    if i in countList:
        print(f"{i} images completed")
