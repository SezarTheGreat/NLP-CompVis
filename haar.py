import cv2

face_cascacde = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

img = cv2.imread('generic photo.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascacde.detectMultiScale(
    gray,
    scaleFactor = 1.1,
    minNeighbors = 5
)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h),(255,0,0),2)

cv2.imshow("Detected face",img)
cv2.waitKey(0)
cv2.destroyAllWindows()