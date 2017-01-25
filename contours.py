import cv2
import numpy as np
def detect_edge(im,l=80,u=190):
    return cv2.Canny(im,l,u)
def get_grayscale_image(im):
    return cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
def get_contours(im):
    return cv2.findContours(im,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)[0]
def draw_contours(im,contours,color=(0,255,0),n=-1):
    cv2.drawContours(im,contours,n,color,3)
    cv2.imshow('contours',im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def draw_largest_contour(im,contours,color=(156,133,144),thickness=3):
    index = 0
    largestContourIndex = -1
    maxLen = 0
    for contour in contours:
        if(len(contour)>maxLen):
            maxLen = len(contour)
            largestContourIndex = index
        index = index+1
    cv2.drawContours(im,contours,largestContourIndex,color,thickness)
    cv2.imshow('largest contour',im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def draw_contours_in_blank_image(im,contours,color=(0,255,0),thickness=3):
    blank_image = np.zeros(im.shape)
    cv2.drawContours(blank_image,contours,-1,(0,255,0),thickness)
    cv2.imshow('contours sketch',blank_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def get_contours_from_file(file_name):
        im = cv2.imread(file_name)
        grs = get_grayscale_image(im)
        edged = detect_edge(grs)
        contours = get_contours(edged)
        return (im,contours)
def draw_contour_from_file(file_name):
    im,contours = get_contours_from_file(file_name)
    draw_contours(im,contours)
def draw_largest_contour_from_file(file_name):
    im,contours = get_contours_from_file(file_name)
    draw_largest_contour(im,contours)
def draw_contours_in_blank_image_from_file(file_name):
    im,contours = get_contours_from_file(file_name)
    draw_contours_in_blank_image(im,contours)
def main(file_name='arsenal-mesut-ozil.jpg'):
    draw_contour_from_file(file_name)
    draw_largest_contour_from_file(file_name)
    draw_contours_in_blank_image_from_file(file_name)

if __name__ ==  "__main__":
    main()
    main('clip_r.jpg')
