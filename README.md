# Smart Wearable Device for Visually Impaired

## Overview

This project presents a Smart Wearable Device designed to assist visually impaired individuals in navigating their surroundings safely and independently. The system combines Raspberry Pi, Ultrasonic Sensors, Camera Module, and Voice Assistance to detect obstacles and provide real-time audio feedback to the user.

The device continuously monitors the environment, identifies obstacles, measures their distance, and alerts the user through voice instructions, enhancing mobility and safety.

---

## Technologies Used

### Hardware
- Raspberry Pi 3 Model B
- Ultrasonic Sensor (HC-SR04)
- USB Camera
- Speaker / Earphones
- Power Supply Unit
- SD Card

### Software
- Python
- OpenCV
- Raspberry Pi OS (Raspbian)
- Deep Learning Models
- WiringPi

---

## Key Features

- Real-time obstacle detection
- Distance measurement using ultrasonic sensors
- Object recognition using camera and image processing
- Voice-based feedback system
- Wearable and portable design
- Safe navigation assistance for visually impaired users

---

## System Architecture

1. Camera captures real-time video.
2. Ultrasonic sensor measures obstacle distance.
3. Raspberry Pi processes sensor and image data.
4. Object detection model identifies nearby objects.
5. Voice instructions are generated.
6. Audio feedback is provided through earphones/speaker.
7. Continuous monitoring ensures real-time assistance.

---

## Hardware Components

### Raspberry Pi
Acts as the central processing unit of the system and coordinates all sensor inputs and outputs.

### Ultrasonic Sensor
Measures the distance between the user and nearby obstacles.

**Specifications**
- Detection Range: 3 cm – 4 m
- Operating Voltage: 5V
- Frequency: 40 KHz

### USB Camera
Captures live video for object detection and recognition.

### Speaker / Earphones
Provides voice alerts and navigation assistance.

---

## Working Principle

The system starts by initializing the Raspberry Pi, camera, and ultrasonic sensor.

- The ultrasonic sensor continuously checks for nearby obstacles.
- The camera captures live images.
- Object detection algorithms identify objects in the path.
- Distance and object information are processed.
- Audio instructions are delivered to the user.

This cycle runs continuously, enabling real-time navigation assistance.

---

## Project Workflow

1. Power ON Raspberry Pi
2. Initialize Camera and Ultrasonic Sensor
3. Capture Real-Time Video
4. Measure Distance to Obstacles
5. Detect and Identify Objects
6. Process Data
7. Generate Voice Feedback
8. Guide User Safely
9. Repeat Continuously

---

## Applications

- Assistance for visually impaired individuals
- Indoor navigation
- Outdoor navigation
- Obstacle avoidance systems
- Smart assistive technologies

---

## Future Enhancements

- GPS-based navigation
- Mobile application integration
- AI-powered object classification
- Emergency alert system
- Battery status notifications
- Face recognition capabilities

---

## Results

The system successfully detects nearby obstacles and provides real-time voice feedback, helping visually impaired users navigate independently and safely.

---

## Learning Outcomes

Through this project, I gained experience in:

- Raspberry Pi Development
- Embedded Systems
- Sensor Integration
- Computer Vision
- OpenCV
- Python Programming
- Object Detection
- Voice Assistance Systems
- Assistive Technology Development

---

## Author

**Sathvika Lingamolla**

Embedded Systems | Computer Vision | IoT Developer
