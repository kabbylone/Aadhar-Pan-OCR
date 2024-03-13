import cv2
import os
import time

# Load Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize video capture from webcam
cap = cv2.VideoCapture(0)

# Create a directory to save captured images
if not os.path.exists('captured_images'):
    os.makedirs('captured_images')

# Get the current time
start_time = time.time()

while True:
    ret, frame = cap.read()  # Read a frame from the webcam
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert frame to grayscale
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)  # Detect faces
    
    # Draw rectangles around detected faces and crop the image
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cropped_img = frame[y:y+h, x:x+w]  # Crop the image to include only the detected face
    
    # Display the frame with face detection
    cv2.imshow('Face Detection', frame)
    
    # Check if a face is detected and 5 seconds have passed
    if len(faces) > 0 and time.time() - start_time >= 5:
        # Save the captured image
        cv2.imwrite('captured_images/captured_image.jpg', cropped_img)
        print("Image captured and saved!")
        break
    
    # Check for key press (q to quit)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()


