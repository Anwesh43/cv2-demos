import cv2
import numpy as np
def get_detector():
    return cv2.SimpleBlobDetector()

def get_keypoints(file_name):
    im = cv2.imread(file_name,0)
    detector = get_detector()
    return detector.detect(im)

def draw_keypoints_from_file_name(file_name):
    keypoints = get_keypoints(file_name)
    im = cv2.imread(file_name,0)
    blobs = cv2.drawKeypoints(im,keypoints,np.zeros((1,1)),(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow('keypoints',blobs)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    draw_keypoints_from_file_name('sunflower.jpeg')
