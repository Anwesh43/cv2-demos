import cv2
def sketch(im):
    im_gr = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    im_gaus = cv2.GaussianBlur(im_gr,(5,5),0)
    im_ed = cv2.Canny(im_gaus,30,100)
    ret,im_inv = cv2.threshold(im_ed,120,255,cv2.THRESH_BINARY_INV)
    cv2.imshow('sketched image',im_inv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
sketch(cv2.imread('arsenal-mesut-ozil.jpg'))
