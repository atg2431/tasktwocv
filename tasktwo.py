import cv2 as cv
import numpy as np

bg=cv.imread('newsrcone.png')
img=cv.resize(bg,(640,480),interpolation = cv.INTER_AREA)
cap = cv.VideoCapture(0)

while True:
    isTrue, frame = cap.read()
    if isTrue:
        hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

        lb=np.array([0,0,100])
        ub=np.array([255,30,255])
        wmask=cv.inRange(hsv,lb,ub)

        rnot=cv.bitwise_not(wmask)

        masked=cv.bitwise_and(img,img,mask=wmask)
        wnmask=cv.bitwise_and(frame,frame,mask=rnot)

        fmask=cv.bitwise_or(masked,wnmask)
        cv.imshow('Cloak',fmask)

        if cv.waitKey(20) & 0xff == ord('d'):
            break
cap.release()
cv.destroyAllWindows()  
# cv.imshow('Image',img)
# print(img.shape[:2])
# print(frame.shape[:2])         