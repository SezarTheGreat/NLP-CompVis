import numpy as np
import cv2

img = cv2.imread("pexels-alexquezada-28888994.jpg",0)
cv2.resize(img,(640,640))

#noise creation
noisy = img.copy()
prob = 0.1
rand = np.random.rand(*img.shape)
noisy[rand < prob] = 0
noisy[rand > 1-prob] = 255

#Apply median filtering
filtered = cv2.medianBlur(noisy,5)

cv2.imshow("Noisy Image: ",noisy)
cv2.imshow("Filtered Image: ",filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()