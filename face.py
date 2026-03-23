import cv2

# Load image
img = cv2.imread("face.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load face detector
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Draw rectangle
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

# Show image
cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()