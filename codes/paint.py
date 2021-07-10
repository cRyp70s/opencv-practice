import cv2
import numpy as np
import random
drawing = False
mode = True
r = g = b = 255
thickness = 1
def nothing(x):
    pass


def draw_circle(event, x, y,  flags, param):
    global drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (x,y),(x+thick,y+thick),(b,g,r), -1)
            else:
                cv2.circle(img, (x,y), thick, (b,g,r), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img, (x,y),(x+thick,y+thick), (b,g,r), -1)
        else:
            cv2.circle(img, (x,y), thick, (b,g,r), -1)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('paint')
cv2.setMouseCallback('paint', draw_circle)

cv2.createTrackbar('R', 'paint', 255, 255, nothing)
cv2.createTrackbar('G', 'paint', 255, 255, nothing)
cv2.createTrackbar('B', 'paint', 255, 255, nothing)
cv2.createTrackbar('Thickness', 'paint', 1, 255, nothing)

while True:
    cv2.imshow('paint', img)
    r = cv2.getTrackbarPos('R','paint')
    g = cv2.getTrackbarPos('G','paint')
    b = cv2.getTrackbarPos('B','paint')
    thick = cv2.getTrackbarPos('Thickness','paint')

    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == ord('c'):
        img = np.zeros((512,512,3), np.uint8)
    elif k == ord('s'):
        fname = str(random.randrange(1000, 10000000000))+".png"
        cv2.imwrite(fname, img)
        print("Saved image to " + fname)
    elif k == 27:
        break

cv2.destroyAllWindows()
