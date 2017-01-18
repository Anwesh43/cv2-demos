import cv2
def use_cvt(fn):
    im = cv2.imread(fn)
    return cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

def use_regular(fn):
    return cv2.imread(fn,0)
def cvt_exper(fn,cvt_num=3):
    im = cv2.imread(fn)
    return cv2.cvtColor(im,cvt_num)
cv2.imshow('cvt_method',use_cvt('arsenal-mesut-ozil.jpg'))
cv2.imshow('regular_method',use_regular('arsenal-mesut-ozil.jpg'))
cv2.imshow('experiment',cvt_exper('arsenal-mesut-ozil.jpg',4))
cv2.waitKey(0)
cv2.destroyAllWindows()
