import cv2
def displayThresholdedImage(im,threshold_value,max_value,type):
    cv2.imshow('thresholded',cv2.threshold(im,threshold_value,max_value,type)[1])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def displayAdaptiveThresholdedImage(im,file_name,max_value=255,block_size=11,c=2,type=cv2.THRESH_BINARY,adaptive_type=cv2.ADAPTIVE_THRESH_MEAN_C):
    im = cv2.adaptiveThreshold(im,max_value,adaptive_type,type,block_size,c)
    cv2.imwrite(file_name,im)
    cv2.imshow('adaptive threshold',im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
im = cv2.imread('arsenal-mesut-ozil.jpg',0)
im1 = cv2.imread('arsenal-mesut-ozil.jpg')
displayThresholdedImage(im,127,255,cv2.THRESH_BINARY)
displayThresholdedImage(im,127,255,cv2.THRESH_BINARY_INV)
displayThresholdedImage(im,127,255,cv2.THRESH_TOZERO)
displayAdaptiveThresholdedImage(im,'mozil_sketch1.png')
displayAdaptiveThresholdedImage(im,'mozil_sketch2.png',adaptive_type=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,)
