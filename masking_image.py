import cv2
import numpy as np
def showImage(titleImagesArray):
    for titleImage in titleImagesArray:
        title,image = titleImage
        cv2.imshow(title,image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
def mask_with_circle(im):
    circle_im = np.zeros(im.shape,dtype='uint8')
    w = im.shape[1]
    h = im.shape[1]
    r = w/2
    if h<w:
        r = h/2
    cv2.circle(circle_im,(w/2,h/2),r,(255,255,255),-1)
    masked_and_image = cv2.bitwise_and(im,circle_im)
    masked_or_image = cv2.bitwise_or(im,circle_im)
    masked_xor_image = cv2.bitwise_xor(circle_im,im)
    masekd_not_image = cv2.bitwise_not(masked_and_image)
    showImage([('circle',circle_im),('original',im),('and image',masked_and_image),('or image',masked_or_image),('xor image',masked_xor_image),('not image',masekd_not_image)])
mask_with_circle(cv2.imread('arsenal-mesut-ozil.jpg'))
