import cv2
import pickle
import face_recognition
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("C:\\Users\\Asus\OneDrive\Desktop\\Pulkit_AIML\\Machine learning Train\\Facial Recognition\\face-recog-attendance-6c441-firebase-adminsdk-q505x-43239c714b.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://face-recog-attendance-6c441-default-rtdb.firebaseio.com/",
    'storageBucket': "face-recog-attendance-6c441.appspot.com"
})

folderpath1='Images'
modepath1=os.listdir(folderpath1)
stID = []
imgmode1=[]
for path1 in modepath1:
    imgmode1.append(cv2.imread(os.path.join(folderpath1,path1)))
    stID.append(os.path.splitext(path1)[0])
    fileName=f'{folderpath1}/{path1}'
    bucket=storage.bucket()
    blob= bucket.blob(fileName)
    blob.upload_from_filename(fileName)
print(stID)

def encodes(imagelist):
    encodedlist=[]
    for img in imagelist:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodedlist.append(encode)
    return encodedlist
print("encoding started")
KnownEncode=encodes(imgmode1)
KnownEncodeID=[KnownEncode,stID]
print("Encoding completed")

file=open("Encodelist.p","wb")
pickle.dump(KnownEncodeID,file)
file.close()
print("File saved")