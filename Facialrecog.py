import cv2
import os

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

while True:
    success, img = cp.read()
    imgbg[162:162+480,55:55+640]=img
    imgbg[44:44+633,808:808+414]=imgmode[1]
    cv2.imshow("face attendance", imgbg)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cp.release()
cv2.destroyAllWindows()
