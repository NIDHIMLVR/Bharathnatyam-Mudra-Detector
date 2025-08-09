# HASTANTRIKA-Bharathnatyam-Mudra-Detector
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Click%20Here-brightgreen?style=for-the-badge)](https://bharathnatyam-mudra-detector.onrender.com/)

A real-time Bharatanatyam Hasta Mudra detection web app using **MediaPipe** and a trained **MLP model**, served with Flask and displayed in a responsive HTML/CSS/JavaScript frontend.  
## 📖 Table of Contents
1. [Overview](#overview)  
2. [Features](#features)  
3. [Tech Stack](#tech-stack)  
4. [Dataset](#dataset)  
5. [Installation](#installation)  
6. [Usage](#usage)  
7. [Screenshots](#screenshots)  
8. [Future Work](#future-work)  
9. [License](#license)  

## OVERVIEW
The Hastantrika App detects and classifies 5 Bharatanatyam hand gestures(Mudras) in real-time from webcam input.It uses MediaPipe Hands to extract landmarks, which are then passed to a trained MLP classifier to predict the mudra.The app also displays the mudra name and a description alongside an image reference.
## FEATURES
### 🎥 Real-time webcam detection of 5 Hasta Mudras.

<img width="600" height="500" alt="image" src="https://github.com/user-attachments/assets/17635da7-e0e9-4788-b40c-d5c6d3c62321" />


### 🖐 MediaPipe landmark extraction for accurate gesture recognition.
![WhatsApp Image 2025-08-09 at 18 35 56](https://github.com/user-attachments/assets/669eae49-b6ca-4dce-968f-c922cfb6a725)



### 🧠 MLP model trained on custom Bharatanatyam mudra dataset.

Input layer: 63 features (21 landmarks × 3 coordinates)

Hidden Layer 1: 128 neurons, ReLU

Hidden Layer 2: 64 neurons, ReLU

Output layer: 5 neurons, Softmax

### 🌐 Responsive frontend (works on mobile & tablet).

<img width="400" height="600" alt="image" src="https://github.com/user-attachments/assets/c518b697-7565-4095-a1d7-f8626578165b" />



### Mudra image & description display for learning purposes.
<img width="600" height="500" alt="image" src="https://github.com/user-attachments/assets/9564dfe2-2dd0-45a6-a605-6ad42e9df61b" />

## Tech Stack
**Frontend:** HTML, CSS, JavaScript  
**Backend:** Flask (Python)  
**ML:** MediaPipe, TensorFlow/Keras (MLP Model)  
**Others:** OpenCV, NumPy



