# HASTANTRIKA-Bharathnatyam-Mudra-Detector
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Click%20Here-brightgreen?style=for-the-badge)](https://bharathnatyam-mudra-detector.onrender.com/)

A real-time Bharatanatyam Hasta Mudra detection web app using **MediaPipe** and a trained **MLP model**, served with Flask and displayed in a responsive HTML/CSS/JavaScript frontend.  
## 📖 Table of Contents
1. [Overview](#overview)  
2. [Features](#features)  
3. [Tech Stack](#tech-stack)  
4. [Dataset](#dataset)  
5. [Running Locally](#running-locally)  
6. [Usage](#usage)  
7. [Future Work](#future-work)  
 

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

## DATASET

The dataset used for training the Mudra Detector model consists of:

- **My own captured and augmented hand mudra images**, and
- **A subset of hand gesture images from a public Kaggle dataset**, used for educational and non-commercial purposes.

Only **5 relevant Bharatanatyam mudras** were selected from the Kaggle dataset, even though it contains many other hand gestures.

🔗 Kaggle Dataset Source:  
[Mudra Hand Gestures Dataset – Kaggle](https://doi.org/10.34740/kaggle/ds/5499681)
License: CC BY-SA 4.0 © Original Author(s)

⚠️ The complete dataset is not included in this repository due to size and license restrictions.  
 Please download the dataset manually from the above link and place the selected images in the `dataset/` folder.

 ## Running Locally 

You can run the app locally if you wish to test or modify it:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/HASTANTRIKA-Bharathnatyam-Mudra-Detector.git
   cd HASTANTRIKA-Bharathnatyam-Mudra-Detector
2. Create virtual environment:
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
4. Install dependencies:
   pip install -r requirements.txt
5. Run python flask server:
   python app.py

## Usage
Online Demo: Visit the Live App here:-https://bharathnatyam-mudra-detector.onrender.com/, and allow camera permissions.

Local Run:
Open the app in your browser after running python app.py.
Ensure your webcam is connected and enabled.
Perform one of the 5 supported Bharatanatyam mudras.
The app will display detected mudra name

## Future Work
Support for other single hand mudras and two-hand combined mudras.



