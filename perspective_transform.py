import cv2
import numpy as np
def transform(im,x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8):
    M = cv2.getPerspectiveTransform(np.float32([[x1,y1],[x2,y2],[x3,y3],[x4,y4]]),np.float32([[x5,y5],[x6,y6],[x7,y7],[x8,y8]]))
    (w,h,d) = im.shape
    im = cv2.warpPerspective(im,M,(w,h))
    cv2.imshow('transformed image',im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
im = cv2.imread('clip_r.jpg')
w = im.shape[0]
h = im.shape[1]
print im.shape
transform(im,7*w/10,0,w,3*h/10,3*w/10,h,0,7*h/10,0,0,w,0,w,h,0,h)
