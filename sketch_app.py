import cv2
from Sketch import *
def getFrame(cap):
    return cap.read()[1]
cap = cv2.VideoCapture(0)
while True:
    frame = getFrame(cap)
    frame = sketch(frame)
    cv2.imshow('captured image',frame)
    if cv2.waitKey(1) == 13:
        break
cap.release()
cv2.destroyAllWindows()
