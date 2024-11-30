import cv2
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces_coordinates = face_classifier.detectMultiScale(gray_frame)

    for (x, y, w, h) in faces_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Video', frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
