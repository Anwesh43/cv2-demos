import cv2
import numpy as np
def handle_click(event,x,y,params,flag):
    img = np.zeros((60,60,3),'uint8')
    console.log()
    cv2.circle(img,(x,y),30,(255,0,0),-1)
cv2.namedWindow('image')
cv2.setMouseCallback('image',handle_click)
cv2.imshow('image',cv2.imread('arsenal-mesut-ozil.jpg'))
cv2.waitKey(0)
cv2.destroyAllWindows()
