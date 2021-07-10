import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # List of lower thresholds
    lowers = [np.array([110,50,50]), np.array([50,50, 50])] 
    # List of upper thresholds
    uppers = [np.array([130,255,255]), np.array([70,255, 255])]
    masks = []
    tracked = []
    for i in range(len(lowers)):
        mask = cv2.inRange(hsv, lowers[i], uppers[i])
        masks.append(mask)
        tracked.append(cv2.bitwise_and(frame,frame, mask= mask))
    mask = masks[0]
    # Join the individual masks together
    for i in masks:
        mask = np.bitwise_or(mask, i)
    track = tracked[0]
    # Join the filtered images together
    for i in tracked:
        track = np.bitwise_or(track, i)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',track)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
