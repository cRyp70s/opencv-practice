import cv2
import os
import time

def get_images(dir):
    imgs = []
    for i in os.listdir(dir):
        f = os.path.join(dir, i)
        if os.path.isfile(f):
            if os.path.splitext(f)[1] in (".jpg", ".png"):
                imgs.append(f)
    return imgs
imgs=get_images(input("image directory: "))
print(imgs)
while True:
    for i in range(len(imgs)):
        cur = cv2.imread(imgs[i])
        next = cv2.imread(imgs[i+1])
        s1 = cur.shape[0:2]
        s2 = next.shape[0:2]
        if s1 != s2:
            x = min(s1[0], s2[0])
            y = min(s1[1], s2[1])
            cur = cur[0:x, 0:y]
            next = next[0:x, 0:y]
        cv2.imshow('slide', cur)
        time.sleep(2)
        from_weight = 1
        to_weight = 0
        while to_weight <  0.9:
            from_weight -= 0.1
            to_weight += 0.1
            dst = cv2.addWeighted(cur, from_weight, next, to_weight, 0)
            cv2.imshow('slide', dst)
            k = cv2.waitKey(300) & 0xFF
            if k == 27: break
cv2.destroyAllWindows()

