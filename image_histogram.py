import cv2
import numpy as np
import matplotlib.pyplot as plt
def calcHistByNp(im):
    hist = np.histogram(im.ravel(),256,[0,255])
    plt.hist(hist)
    plt.show()
def calcHistByCv(im):
    color = ('blue','green','red')
    for i,col in enumerate(color):
        hist = cv2.calcHist(im,[i],None,[255],[0,255])
        plt.plot(hist,color=col)
    plt.show()

#calcHistByNp(cv2.imread('arsenal-mesut-ozil.jpg'))
calcHistByCv(cv2.imread('arsenal-mesut-ozil.jpg'))
