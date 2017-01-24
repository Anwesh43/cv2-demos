import cv2
def cannyEd(im,lower=10,upper=70):
    im_can = cv2.Canny(im,lower,upper)
    cv2.imshow('canny edge detector',im_can)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
cannyEd(cv2.imread('arsenal-mesut-ozil.jpg',0))
