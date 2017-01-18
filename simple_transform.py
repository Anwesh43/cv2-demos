import cv2
import numpy as np
def transform(im,matrix):
    return cv2.warpAffine(im,matrix,(im.shape[1],im.shape[0]))
def rotate(im,deg):
    return transform(im,cv2.getRotationMatrix2D((im.shape[1]/2,im.shape[0]/2),deg,1))
def translate(im,tx,ty):
    return transform(im,np.array([[1,0,tx],[0,1,ty]],dtype='float32'))

im = cv2.imread('arsenal-mesut-ozil.jpg')
im1 = im.copy()
im = translate(im,300,300)
cv2.imshow('translation',im)
im1 = rotate(im1,45)
cv2.imshow('rotation',im1)
cv2.waitKey(0)
cv2.destroyAllWindows()
