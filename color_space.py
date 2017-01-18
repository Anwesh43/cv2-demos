import cv2
import numpy as np
def getChannelFromFileName(fn):
    return getChannel(cv2.imread(fn))
def getHSVChannelFromFileName(fn):
    im = cv2.imread(fn)
    im_hsv = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    cv2.imshow('hsv',im_hsv)
    return getChannel(im_hsv)
def getChannel(im):
    return cv2.split(im)

B,G,R = getChannelFromFileName('arsenal-mesut-ozil.jpg')
print B.shape
zeros = np.zeros(B.shape,dtype='uint8')
print zeros.shape
cv2.imshow('Blue image',cv2.merge([B,zeros,zeros]))
cv2.imshow('Green image',cv2.merge([zeros,G,zeros]))
cv2.imshow('Red image',cv2.merge([zeros,zeros,R]))
cv2.imshow('Blue Amplified Image',cv2.merge([B+100,G,R]))
cv2.imshow('Green Amplified Image',cv2.merge([B,G+100,R]))
cv2.imshow('Red Amplified Image',cv2.merge([B,G,R+100]))
H,S,V = getHSVChannelFromFileName('arsenal-mesut-ozil.jpg')
cv2.imshow('Hue',H)
cv2.imshow('Saturation',S)
cv2.imshow('Value',V)
cv2.waitKey(0)
cv2.destroyAllWindows()
