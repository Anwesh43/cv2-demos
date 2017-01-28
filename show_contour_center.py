import cv2
from sort_contour_area import sort_contours_according_to_area
def draw_center_of_contour_from_file(file):
    (contours,im) = sort_contours_according_to_area(file)
    x = 0
    y = 0
    for contour in contours:
        M = cv2.moments(contour)
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])
        break
    if(len(contours) > 0):
        contour = contours[0]
        print contour
        print x
        print y
        cv2.drawContours(im,[contour],-1,(0,255,0),3)
        cv2.putText(im,"C",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
        cv2.imshow('centroid of the image',im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    draw_center_of_contour_from_file('arsenal-mesut-ozil.jpg')
