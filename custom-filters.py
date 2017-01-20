import cv2
import numpy as np
def applyConv(im,kernel):
    return cv2.filter2D(im,-1,kernel)
def displayImage(im,title):
    cv2.imshow(title,im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def applySobelFilter(im):
    gx = applyConv(im,np.array([[-1,0,1],[-2,0,2],[-1,0,1]]))
    gy = applyConv(im,np.array([[1,2,1],[0,0,0],[-1,-2,-1]]))
    g = np.sqrt(gx*gx,gy*gy)
    displayImage(gx,'gx')
    displayImage(gy,'gy')
    displayImage(g,'g')

applySobelFilter(cv2.imread('arsenal-mesut-ozil.jpg',0))
