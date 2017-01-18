import cv2
def getBGROfPixel(im,x,y):
    return im[y,x]
def getPixelFromFileName(fn,x=0,y=0):
    im = cv2.imread(fn)
    w = im.shape[1]
    h = im.shape[0]
    if x<w and y<h:
        pixel = getBGROfPixel(im,x,y)
        return (pixel[0],pixel[1],pixel[2])
    else:
        print "one or both the coordinates are not inside the image"
        return (-1,-1,-1)
def getGrayScalePixelFromFileName(fn,x=0,y=0):
    im = cv2.imread(fn)
    w = im.shape[1]
    h = im.shape[0]
    im_gs = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    if x<w and y<h:
        pixel = getBGROfPixel(im_gs,x,y)
        return pixel
    else:
        print "one or both coordinates are not inside the image"
        return -1
#getting first pixel
print getPixelFromFileName('arsenal-mesut-ozil.jpg')
#getting pixel at 20,30
print getPixelFromFileName('arsenal-mesut-ozil.jpg',20,30)
#getting pixel at 100,3000
print getPixelFromFileName('arsenal-mesut-ozil.jpg',100,300)
#getting pixel at 1500 1700
print getPixelFromFileName('arsenal-mesut-ozil.jpg',1500,1700)
#GrayScale Image
#getting first pixel
print getGrayScalePixelFromFileName('arsenal-mesut-ozil.jpg')
#getting pixel at 20,30
print getGrayScalePixelFromFileName('arsenal-mesut-ozil.jpg',20,30)
#getting pixel at 100,3000
print getGrayScalePixelFromFileName('arsenal-mesut-ozil.jpg',100,300)
#getting pixel at 1500 1700
print getGrayScalePixelFromFileName('arsenal-mesut-ozil.jpg',1500,1700)
