import sys
import cv2
import sort_contours
if len(sys.argv) == 2 and __name__ == "__main__":
    n = int(sys.argv[1])
    sorted_contours = sort_contours.get_sorted_contour('arsenal-mesut-ozil.jpg')
    im = cv2.imread('arsenal-mesut-ozil.jpg')
    cv2.drawContours(im,sorted_contours,n,(0,255,0),3)
    cv2.imshow('largest contour of index n',im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
