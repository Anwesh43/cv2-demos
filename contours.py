import cv2
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
def draw_contour_from_file(file_name):
    im = cv2.imread(file_name)
    grs = get_grayscale_image(im)
    edged = detect_edge(grs)
    contours = get_contours(edged)
    draw_contours(im,contours)
    print len(contours)
def main():
    draw_contour_from_file('arsenal-mesut-ozil.jpg')

if __name__ ==  "__main__":
    main()
