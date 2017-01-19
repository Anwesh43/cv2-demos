import numpy as np
import cv2
def draw_line(im,x1,y1,x2,y2,color,line_width):
    cv2.line(im,(x1,y1),(x2,y2),color,line_width)

def draw_rect(im,x,y,w,h,color,line_width):
    cv2.rectangle(im,(x,y),(w,h),color,line_width)

def draw_circle(im,x,y,r,color,line_width):
    cv2.circle(im,(x,y),r,color,line_width)

def draw_polyline(im,points,color,line_width):
    coordinates = np.array(points).reshape(-1,1,2)
    cv2.polylines(im,[coordinates],True,color,line_width)
def draw_text(im,text,x,y,font,font_size,color,thickness):
    cv2.putText(im,text,(x,y),font,font_size,color,thickness)
def draw_ellipse(im,x,y,axis_x,axis_y,deg,start,end,color,thickness):
    cv2.ellipse(im,(x,y),(axis_x,axis_y),deg,start,end,color,thickness)
im = cv2.imread('arsenal-mesut-ozil.jpg')
draw_line(im,10,10,300,300,(50,200,50),5)
draw_rect(im,0,100,200,200,(50,200,50),5)
draw_rect(im,0,200,100,100,(50,200,50),-1)
draw_circle(im,350,350,50,(50,50,200),-1)
draw_polyline(im,[[600,400],[700,400],[650,600]],(0,255,0),5)
draw_text(im,"Mesut Ozil",im.shape[1]/2-100,im.shape[0]/2-50,cv2.FONT_HERSHEY_PLAIN,3,(150,200,100),2)
draw_ellipse(im,600,600,100,50,30,0,360,(150,100,175),-1)
cv2.imshow('with_line',im)
cv2.waitKey(0)
cv2.destroyAllWindows()
