import cv2
import pickle
import face_recognition
import os
 
folderpath1='Images'
modepath1=os.listdir(folderpath1)
ID = []
imgmode1=[]
for path1 in modepath1:
    imgmode1.append(cv2.imread(os.path.join(folderpath1,path1)))
    ID.append(os.path.splitext(path1)[0])
print(ID)

def encodes(imagelist):
    encodedlist=[]
    for img in imagelist:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodedlist.append(encode)
    return encodedlist
print("encoding started")
KnownEncode=encodes(imgmode1)
print(KnownEncode)
print("Encoding completed")
