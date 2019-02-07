from collections import deque
import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the (optional) video file")
args = vars(ap.parse_args())

greenLower = (10, 10, 120)
greenUpper = (80, 80, 255)


if not args.get("video", False):
    camera = cv2.VideoCapture(0)

else:
    camera = cv2.VideoCapture(args["video"])
    camera.set(cv2.cv.CV_CAP_PROP_FPS, 10)
while True:
    (grabbed, frame) = camera.read()

    if args.get("video") and not grabbed:
        break

    frame = imutils.resize(frame, width=600)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(frame, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        if radius > 10:
            center = (int(x),int(y))
            pt2 = (int(x+int(radius)),int(y+int(radius)))
            print("radius = ",radius)
            cv2.circle(frame, center ,int(radius), (0, 0, 255), 4)
            cv2.circle(frame,center,1,(0,255,255),2)
            cv2.putText(frame, str(center), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 20, 200), 1)
            cv2.putText(frame, str(radius), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 20, 200), 1)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    #CVXCVXCVXCVXCVXCVXCVXCVLKFL;DF;DF
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()