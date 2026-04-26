
# driver_drowsiness
AIML project
=======

# 🚗 Driver Drowsiness Detection System

## 📌 Overview

This project is a **real-time Driver Drowsiness Detection System** built using Python and OpenCV.
It monitors the driver's face through a webcam and detects signs of drowsiness such as **eye closure** and **yawning**, then alerts the user.

---

## 🎯 Features

* 👁️ Eye detection using Haar Cascade
* 😴 Detects prolonged eye closure (drowsiness)
* 😮 Yawn detection using mouth recognition
* 📊 Real-time drowsiness score tracking
* ⚠️ Warning alert when driver is sleepy
* 🎥 Live webcam monitoring

---

## 🛠️ Technologies Used

* Python
* OpenCV (`cv2`)
* NumPy

---

## 📂 Project Structure

```
project-folder/
│
├── drowsiness_detection.py   # Main Python file
├── README.md                 # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Install Python

Make sure Python (3.x) is installed.

### 2. Install Required Libraries

Open terminal in VS Code and run:

```
pip install opencv-python numpy
```

---

## ▶️ How to Run

1. Open project in VS Code
2. Open terminal
3. Run the file:

```
python drowsiness_detection.py
```

4. Webcam will start automatically

---

## ⛔ How to Stop

* Press **Q key** on keyboard
  or
* Press **Ctrl + C** in terminal

---

## 🧠 How It Works

* Detects face using Haar Cascade
* Splits face into:

  * Upper part → Eyes
  * Lower part → Mouth
* Tracks:

  * Eye closure duration
  * Mouth opening (yawning)
* Generates a **drowsiness score**
* Displays:

  * ALERT / WARNING / DROWSY status

---

## 📸 Output

* Green box → Alert
* Orange box → Warning
* Red box → Drowsy
* “WAKE UP!” alert when needed

---

## 🚀 Future Improvements

* Add alarm sound 🔊
* Improve accuracy using AI/ML models
* Mobile app integration
* Night vision support

---

## 👩‍💻 Author

Ayesha Ali


---

## 📜 License

This project is for educational purposes only.

