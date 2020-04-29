import cv2
import numpy as np

face = cv2.CascadeClassifier('Cas.xml')

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('image',frame)
    if cv2.waitKey(1) & 0XFF==ord('e'):
        break
cap.release()
cv2.destroyAllWindows()