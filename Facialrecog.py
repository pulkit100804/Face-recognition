import cv2
import os
import pickle
import face_recognition
import numpy as np
imgbg=cv2.imread('Resources\\background.png')
folderpath='Resources\\Modes'
modepath=os.listdir(folderpath)
imgmode=[]
for path in modepath:
    imgmode.append(cv2.imread(os.path.join(folderpath,path)))
cp = cv2.VideoCapture(1)
if not cp.isOpened():
    print("Error: Failed to open camera.")
    exit()

cp.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cp.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
print("Loading.....")
file=open('Encodelist.p','rb')
KnownEncodeID=pickle.load(file)
encode,Stid=KnownEncodeID
print("File loaded.")
print(Stid)
while True:
    success, img = cp.read()
    imgS = cv2.resize(img, None, fx=0.25, fy=0.25)
    imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
    faceCurrent=face_recognition.face_locations(imgS)
    CurEncode=face_recognition.face_encodings(imgS,faceCurrent)
    imgbg[162:162+480,55:55+640]=img
    imgbg[44:44+633,808:808+414]=imgmode[1]
    for EncoFace, Faceloc in zip(CurEncode,faceCurrent):
        matches=face_recognition.compare_faces(encode,EncoFace)
        facedis=face_recognition.face_distance(encode,EncoFace)
        #print(matches)
       # print(facedis)

        matched=np.argmin(facedis)
        if matched in matches:
            print("known face detected")
        if matched not in matches:
            print("Unknown Face detetcted")
    cv2.imshow("face attendance", imgbg)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cp.release()
cv2.destroyAllWindows()
