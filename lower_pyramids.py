import cv2
def getLowerPyramid(im,n):
    cv2.imshow('Lower pyramid at {0}'.format(n),im)
    cv2.waitKey(0)
    if(n > 0):
        getLowerPyramid(cv2.pyrDown(im),n-1)
    cv2.destroyAllWindows()
getLowerPyramid(cv2.imread('arsenal-mesut-ozil.jpg'),4)
