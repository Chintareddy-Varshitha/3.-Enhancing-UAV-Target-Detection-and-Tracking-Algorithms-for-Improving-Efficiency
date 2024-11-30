# Import OpenCV
import cv2

# Define haar cascade classifier for face detection
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read input image to recognize face
img = cv2.imread('face.jpeg')

# Convert image to gray scale OpenCV
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect face using haar cascade classifier
faces_coordinates = face_classifier.detectMultiScale(gray_img)

# Draw a rectangle around the faces
for (x, y, w, h) in faces_coordinates:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Saving the image
cv2.imwrite('face detection using haar cascade output.png', img)

# show output image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()