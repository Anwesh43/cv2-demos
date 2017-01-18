from cv2 import *
def merge_image(im,x,y,x1,y1,w,h):
    im[x:x+w,y:y+h] = im[x1:x1+w,y1:y1+h]
    return im
im = imread('arsenal-mesut-ozil.jpg')

imshow('image',merge_image(im,0,0,30,620,150,120))
imshow('image',merge_image(im,100,100,30,620,150,120))
imshow('image',merge_image(im,200,200,30,620,150,120))
imshow('image',merge_image(im,300,300,30,620,150,120))
waitKey(0)
destroyAllWindows()
