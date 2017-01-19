import cv2
def getUpperPyramids(im,n):
    cv2.imshow('image at {0}'.format(n),im)
    cv2.waitKey(0)
    if(n>0):
        getUpperPyramids(cv2.pyrUp(im),n-1)
    else:
        cv2.destroyAllWindows()

getUpperPyramids(cv2.imread('arsenal-mesut-ozil.jpg'),2)
