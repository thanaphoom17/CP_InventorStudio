import numpy as np
import cv2

# Load the Haar cascade file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
while(True):
    # จับภาพแบบ frame by frame
    ret, frame = cap.read()
        # ตรงนี้ผมจะแสดงภาพออกมาเป็นขาวดำ โดยคำนวนผ่าน function cvtColor
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_rects = face_cascade.detectMultiScale(gray, 1, 5)

    for (x,y,w,h) in face_rects:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    # แสดงผล frame ที่ถูกครอบด้วยสี่เหลี่ยมบนใบหน้าแล้ว
    cv2.imshow('face_detector', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): # หน้าจอ จะปิดก็ต่อเมื่อ ผมกด q
        break

cap.release()
cv2.destroyAllWindows()