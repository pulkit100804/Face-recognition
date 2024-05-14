import cv2
import pickle
import face_recognition
import os
 
folderpath1='Images'
modepath1=os.listdir(folderpath1)
imgmode1=[]
for path1 in modepath1:
    imgmode1.append(cv2.imread(os.path.join(folderpath1,path1)))
print(len(imgmode1))