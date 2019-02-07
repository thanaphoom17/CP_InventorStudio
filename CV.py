import cv2
import numpy as np
cap = cv2.VideoCapture(0)  # รับวิดีโอจากกล้อง
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
while (1):
    # รับข้อมูลจากเว็บแคม
    _, frame = cap.read()
    # แปลงสี BGR ไปยัง HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # ช่วงของสีเหลืองในระบบ HSV
    lower_yellow = np.array([0,  0, 150], dtype=np.uint8) ##BGR
    upper_yellow = np.array([80,80, 255], dtype=np.uint8)

    pts = deque(maxlen=args["buffer"])
    counter = 0
    (dX, dY) = (0, 0)
    direction = ""
    # จำกดภาพ HSV รับเฉพาะสีเหลิอง
    yellow = cv2.inRange(frame, lower_yellow, upper_yellow)
    # Bitwise-AND mask และภาพต้นฉบับ
    mask = cv2.bitwise_and(frame, frame, mask=yellow)
    cv2.imshow('frame', frame)
    cv2.imshow('red', yellow)
    cv2.imshow('mask', mask)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()