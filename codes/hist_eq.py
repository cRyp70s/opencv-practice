import cv2
import numpy as np

img = cv2.imread(input("Image path: "),0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
res = np.hstack((img,cl1)) #stacking images side-by-side
cv2.imwrite('res3.png',res)
