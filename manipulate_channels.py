import cv2
import numpy as np
class ChannelManipulator:
    def __init__(self,image_file):
        self.im = cv2.imread(image_file)
        self.r,self.g,self.b = cv2.split(self.im)
        self.shape = self.r.shape
    def __showImage(self,im):
        cv2.imshow(im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def showRedChannelOnly(self):
        imr = cv2.merge((np.zeros(self.shape,np.uint8),np.zeros(self.shape),self.r))
        self.__showImage(imr)
    def showBlueChannelOnly(self):
        imb = cv2.merge((self.b,np.zeros(self.shape),np.zeros(self.shape)))
        self.__showImage(imb)
    def showGreenChannelOnly(self):
        img = cv2.merge((np.zeros(self.shape),self.g,np.zeros(self.shape)))
        self.__showImage(img)

channelManipulator = ChannelManipulator('arsenal-mesut-ozil.jpg')
channelManipulator.showRedChannelOnly()
# channelManipulator.showBlueChannelOnly()
# channelManipulator.showGreenChannelOnly()
