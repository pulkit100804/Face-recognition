import cv2
import os
import pickle
import face_recognition
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("C:\\Users\\Asus\OneDrive\Desktop\\Pulkit_AIML\\Machine learning Train\\Facial Recognition\\face-recog-attendance-6c441-firebase-adminsdk-q505x-43239c714b.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://face-recog-attendance-6c441-default-rtdb.firebaseio.com/",
    'storageBucket': "face-recog-attendance-6c441.appspot.com"
})
bucket=storage.bucket()
modetype=0
counter=0
ids=-1
imgst=[]
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
    imgbg[44:44+633,808:808+414]=imgmode[modetype]
    for EncoFace, Faceloc in zip(CurEncode,faceCurrent):
        matches=face_recognition.compare_faces(encode,EncoFace)
        facedis=face_recognition.face_distance(encode,EncoFace)
        #print(matches)
       # print(facedis)

        matched_index = None
        for idx, match in enumerate(matches):
            if match:
                matched_index = idx
                break

        if matched_index is not None:
            ids=Stid[matched_index]
            if counter == 0:
                counter =1
                modetype=1
    if counter != 0:
        if counter == 1:
            blob=bucket.get_blob(f'Images/{ids}.png')
            array=np.frombuffer(blob.download_as_string(),np.uint8)
            imgst=cv2.imdecode(array,cv2.COLOR_BGRA2BGR)
            studentinfo=db.reference(f'Students/{ids}').get()
            cv2.putText(imgbg,str(studentinfo['Attendnace']),(861,125),
                        cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
            cv2.putText(imgbg,str(studentinfo['Major']),(1006,550),
                        cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
            cv2.putText(imgbg,str(ids),(1006,493),
                        cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
            cv2.putText(imgbg,str(studentinfo['class']),(1025,625),
                        cv2.FONT_HERSHEY_COMPLEX,0.6,(100,100,100),1)
            (w,h),_= cv2.getTextSize(studentinfo['Name'],cv2.FONT_HERSHEY_COMPLEX,1,1)
            offest=(414-w)//2
            cv2.putText(imgbg,str(studentinfo['Name']),(808+offest,465),
                        cv2.FONT_HERSHEY_COMPLEX,1,(55,55,55),1)
            imgbg[175:175+622,909:909+493]=imgst
            
        counter=+1

    cv2.imshow("face attendance", imgbg)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cp.release()
cv2.destroyAllWindows()
