import cv2
import sys
def cropImage(im,startX,endX,startY,endY):
    return im[startX:endX,startY:endY]

im = cv2.imread('arsenal-mesut-ozil.jpg')
arguments = sys.argv[1:]
if(len(arguments) == 4):
    coordinates = map(int,arguments)
    cv2.imshow('cropped image',cropImage(im,coordinates[0],coordinates[1],coordinates[2],coordinates[3]))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
