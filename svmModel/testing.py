import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pickle
import random
from sklearn.model_selection import  train_test_split
from PIL import Image
from sklearn.svm import SVC
#dir = 'C:\\test_set'

#categories = ['cats', 'dogs']

#data = []

#for category in categories:
#    path = os.path.join(dir,category)
#    label = categories.index(category)

#    for img in os.listdir(path):
#        imgpath = os.path.join(path,img)
#        print(imgpath)
#        pet_img = cv2.imread(imgpath,0)
#        try:
#            pet_img = cv2.resize(pet_img,(50, 50))
#            image = np.array(pet_img).flatten()

#            data.append([image,label])

#        except Exception as e:
#            pass




#print(len(data))

pick_in = open('data1.pickle', 'wb')
pickle.dump(data, pick_in)
pick_in.close()
