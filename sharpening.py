import cv2
import numpy as np
def sharpenImageWithConv(im):
    kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
    im_sharpened = cv2.filter2D(im,-1,kernel)
    cv2.imshow('Sharpened Image',im_sharpened)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
sharpenImageWithConv(cv2.imread('arsenal-mesut-ozil.jpg'))
