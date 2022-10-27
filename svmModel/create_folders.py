import os
import csv

path = "C:\\SCDProject\\svmModel"
tuplesList = []
with open('C:\\SCDProject\\ISIC_2019_Training_GroundTruth (3).csv') as file_une:
    file_deux = csv.reader(file_une)

    for row in file_deux:
        tuplesList.append(row[1:10])
print(tuplesList[0])
for type in tuplesList[0]:
    os.mkdir(path+f"\\{type}")
