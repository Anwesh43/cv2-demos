import cv2
import numpy as np
import math
def getLinesMarkedFromImage(im):
    gr_im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    edge_im =cv2.Canny(im,20,300)
    lines = cv2.HoughLines(edge_im,1,np.pi/180,200)
    for rho,theta in lines[0]:
        x0 = rho*np.sin(theta)
        y0 = rho*np.cos(theta)
        x1 = int(x0-200*np.sin(theta))
        y1 = int(y0+200*np.cos(theta))
        x2 = int(x0+200*np.sin(theta))
        y2 = int(y0-200*np.cos(theta))
        cv2.line(im,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.circle(im,(x0,y0),5,(0,255,0),-1)
def drawLinesFromFile(file):
    im = cv2.imread(file)
    getLinesMarkedFromImage(im)
    cv2.imshow('marked lines',im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def main():
    drawLinesFromFile('clip_r.jpg')
if __name__ == "__main__":
    main()
