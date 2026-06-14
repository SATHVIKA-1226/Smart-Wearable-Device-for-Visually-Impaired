import cv2
import numpy as np
import pyttsx3
import math

# Initialize the TTS engine
engine = pyttsx3.init()

# Load the MobileNet SSD model
net = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt', 'MobileNetSSD_deploy.caffemodel')

# Define the classes for object detection (MobileNet SSD)
classNames = { 0: 'background', 1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat', 5: 'bottle', 
               6: 'bus', 7: 'car', 8: 'cat', 9: 'chair', 10: 'cow', 11: 'diningtable', 12: 'dog', 
               13: 'horse', 14: 'motorbike', 15: 'person', 16: 'pottedplant', 17: 'sheep', 
               18: 'sofa', 19: 'train', 20: 'tvmonitor'}

# Set up the camera
cap = cv2.VideoCapture(0)

# Focus parameters for depth estimation (tune these based on your camera and experiment)
focal_length = 650  # Example focal length in pixels
real_width = 15.0   # Real-world width of the object in cm (e.g., a person)

# Distance threshold for "Danger" and "Safe" messages (in cm)
danger_distance = 50.0  # If an object is closer than this, we say "Danger"
safe_distance = 100.0   # If an object is farther than this, we say "Safe"

while True:
    # Read the frame from the camera
    ret, frame = cap.read()
    if not ret:
        break

    # Prepare the image for MobileNet SSD
    blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    # Iterate through the detections
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.2:  # Confidence threshold
            class_id = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
            (x1, y1, x2, y2) = box.astype("int")

            # Draw the bounding box around the object
            label = f"{classNames[class_id]}: {confidence:.2f}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Depth Estimation: Calculate distance based on object width and focal length
            object_width = x2 - x1  # Width of the detected object in pixels
            distance = (real_width * focal_length) / object_width  # Depth formula (distance in cm)

            # Display the distance on the frame
            distance_text = f"Distance: {distance:.2f} cm"
            cv2.putText(frame, distance_text, (x1, y2 + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Check if the object is too close or safe
            if distance < danger_distance:
                warning_message = f"Warning: {classNames[class_id]} is too close!"
                cv2.putText(frame, warning_message, (x1, y2 + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                # TTS: Say "Danger" if too close
                engine.say(f"Danger: {classNames[class_id]} is too close, distance is {distance:.2f} centimeters.")
            elif distance > safe_distance:
                # TTS: Say "Safe" if the object is at a safe distance
                engine.say(f"{classNames[class_id]} is at a safe distance, {distance:.2f} centimeters.")
            else:
                # TTS: If the object is in the "safe" zone but not too far
                engine.say(f"{classNames[class_id]} is at a moderate distance, {distance:.2f} centimeters.")
            engine.runAndWait()

    # Show the output frame
    cv2.imshow("Object Detection and Distance Estimation", frame)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources and close windows
cap.release()
cv2.destroyAllWindows()
