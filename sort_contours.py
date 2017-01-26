import cv2
import contours
import time
def sort_contours(conts):
    def compareLenOfContour(contourA,contourB):
        return len(contourB)-len(contourA)
    conts.sort(compareLenOfContour)
def get_sorted_contour(file_name):
    im,conts = contours.get_contours_from_file(file_name)
    sort_contours(conts)
    return conts
def main(file_name='arsenal-mesut-ozil.jpg'):
    for cont in get_sorted_contour(file_name):
        print len(cont)

if __name__ == "__main__":
    main()
