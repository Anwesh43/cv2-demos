import cv2
import sys
import numpy as np
def main():
    arguments = sys.argv[1:]
    numArray = map(int,arguments)
    if len(numArray) == 9:
        kernel1D = np.array(numArray)
        kernel = kernel1D.reshape((3,3))
        im = cv2.imread('arsenal-mesut-ozil.jpg')
        im_conv = cv2.filter2D(im,-1,kernel)
        cv2.imshow('Convolved Image',im_conv)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print 'please enter 9 integers'
if __name__ == "__main__":
    main()
