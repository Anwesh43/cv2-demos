import cv2
def draw_line(im,x1,y1,x2,y2,color,line_width):
    cv2.line(im,(x1,y1),(x2,y2),color,line_width)

def draw_rect(im,x,y,w,h,color,line_width):
    cv2.rectangle(im,(x,y),(w,h),color,line_width)

def draw_circle(im,x,y,r,color,line_width):
    cv2.circle(im,(x,y),r,color,line_width)
im = cv2.imread('arsenal-mesut-ozil.jpg')
draw_line(im,10,10,300,300,(50,200,50),5)
draw_rect(im,0,100,200,200,(50,200,50),5)
draw_rect(im,0,200,100,100,(50,200,50),-1)
draw_circle(im,350,350,50,(50,50,200),-1)
cv2.imshow('with_line',im)
cv2.waitKey(0)
cv2.destroyAllWindows()
