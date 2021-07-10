import cv2
import numpy as np
img1 = cv2.imread('0-a.png',0)
img2 = cv2.imread('0-b.png',0)
img3 = cv2.imread('0-c.png', 0)
img4 = cv2.imread('a-0.png', 0)
ret, thresh = cv2.threshold(img1, 127, 255,0)
ret, thresh2 = cv2.threshold(img2, 50, 255,0)
ret, thresh3 = cv2.threshold(img3, 127, 255,0)
ret, thresh4 = cv2.threshold(img4, 127, 255,0)
contours,hierarchy = cv2.findContours(thresh,2,1)
cnt1 = contours[0]
contours,hierarchy = cv2.findContours(thresh2,2,1)
cnt2 = contours[0]
contours,hierarchy = cv2.findContours(thresh3,2,1)
cnt3 = contours[0]
contours,hierarchy = cv2.findContours(thresh4,2,1)
cnt4 = contours[0]

ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
print("0-a with 0-b",ret)
ret = cv2.matchShapes(cnt1,cnt3,1,0.0)
print("0-a with 0-c", ret)
ret = cv2.matchShapes(cnt2,cnt3,1,0.0)
print("0-b with 0-c",ret)
ret = cv2.matchShapes(cnt1,cnt4,1,0.0)
print("0-a with a-0",ret)
ret = cv2.matchShapes(cnt2,cnt4,1,0.0)
print("0-b with a-0",ret)
ret = cv2.matchShapes(cnt3,cnt4,1,0.0)
print("0-c with a-0",ret)



