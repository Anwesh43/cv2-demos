import cv2
import numpy as np
def getContoursFromFile(file):
    im = cv2.imread(file)
    im_gr = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    im_edge = cv2.Canny(im,100,250)
    contours,ret = cv2.findContours(im_edge,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    print type(contours)
    return (contours,im)
def sort_contours_according_to_area(file):
    (contours,im) = getContoursFromFile(file)
    sorted_contours = sorted(contours,key=cv2.contourArea,reverse=True)
    return (sorted_contours,im)
def drawContoursInImage(file):
    (contours,im) = sort_contours_according_to_area(file)
    for contour in contours:
        cv2.drawContours(im,[contour],-1,(0,255,0),3)
        cv2.imshow('contour image',im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
def drawContoursInBlankImage(file):
    (contours,im) = sort_contours_according_to_area(file)
    new_im = np.zeros(im.shape)
    for contour in contours:
        cv2.drawContours(new_im,[contour],-1,(255,255,255),3)
        cv2.imshow('sorted contour in blank image',new_im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
if __name__ == "__main__":
    #drawContoursInImage('clip_r.jpg')
    drawContoursInBlankImage('arsenal-mesut-ozil.jpg')
