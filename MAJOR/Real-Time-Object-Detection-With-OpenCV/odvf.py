import cv2
import numpy as np
import time
import pyttsx3

# Load the pre-trained model and class labels
net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt", "MobileNetSSD_deploy.caffemodel")

# Define the class labels MobileNetSSD is trained on
CLASSES = ["background", "airplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair",
           "cow", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "train", "truck", "tvmonitor"]

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to announce objects using pyttsx3
def announce_object(object_name):
    engine.say(f"Detected object: {object_name}")
    engine.runAndWait()

# Open the video stream
cap = cv2.VideoCapture(0)

# Set the frame width and height (optional)
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Prepare the frame for object detection
    blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5, (0, 0, 0), False, crop=False)
    net.setInput(blob)
    detections = net.forward()

    # Process the detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.2:  # Threshold for detecting objects
            class_id = int(detections[0, 0, i, 1])
            label = CLASSES[class_id]
            confidence = round(confidence, 2)

            # Draw bounding box around the object
            box = detections[0, 0, i, 3:7] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
            (x1, y1, x2, y2) = box.astype("int")
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{label}: {confidence}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Announce the detected object
            announce_object(label)

    # Show the frame
    cv2.imshow("Object Detection", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video stream and close windows
cap.release()
cv2.destroyAllWindows()
