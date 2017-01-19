import cv2
def resizeWithFScale(im,x,y,interp):
    cv2.resize(im,None,fx=x,fy=y,interpolation=interp)

def resizeWithSize(im,w,h,interp):
    cv2.resize(im,(w,h),interpolation=interp)
im = cv2.imread('arsenal-mesut-ozil.jpg')

im1 = resizeWithFScale(im,2,2,cv2.INTER_LINEAR)
cv2.imshow('half of the image',im1)
cv2.waitKey(0)
im2 = resizeWithSize(im,500,500,cv2.INTER_LINEAR)
cv2.imshow('500*500',im2)
cv2.waitKey(0)
cv2.destroyAllWindows()
