import cv2
import numpy as np
def blurWithConv(im,kernel_size = 3):
    kernel = (1.0/(kernel_size*kernel_size))*np.ones((kernel_size,kernel_size),dtype='float32')
    cv2.imshow('blurred image',cv2.filter2D(im,-1,kernel))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def medianBlur(im,kernel_size=5):
    cv2.imshow('medianBlured image',cv2.medianBlur(im,kernel_size))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def gaussianBlur(im,kernel_size=7):
    cv2.imshow('gaussianBlur',cv2.GaussianBlur(im,(kernel_size,kernel_size),0))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def fastDenoising(im):
    cv2.imshow('Fast',cv2.fastNlMeansDenoisingColored(im,6,6,7,21))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
im = cv2.imread('arsenal-mesut-ozil.jpg')
cv2.imshow('original image',im)
cv2.waitKey()
cv2.destroyAllWindows()
blurWithConv(im)
blurWithConv(im,7)
medianBlur(im)
gaussianBlur(im,7)
fastDenoising(im)
