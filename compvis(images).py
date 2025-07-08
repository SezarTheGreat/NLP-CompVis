import cv2
image1 = cv2.imread("images.jpg")

resize_image = cv2.resize(image1,(640,640))

cv2.imshow("The picture is:",image1)
cv2.imshow("resize",resize_image)

cv2.imwrite("ccc.jpg",resize_image)
cv2.waitKey(0)
cv2.destroyAllWindows()