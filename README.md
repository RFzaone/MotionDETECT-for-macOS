# MotionDETECT-for-macOS

Surveillance Matrix (Mac Motion Detection System)

A lightweight Python-based motion detection system for macOS using OpenCV.
It monitors webcam input, detects movement through frame comparison, and triggers alerts such as audio notifications and optional system actions.

Features
Real-time webcam motion detection
Pixel-based motion analysis for stability
macOS text-to-speech alerts using system say command
Optional screen lock integration
Event logging to local file
Lightweight, no graphical interface required
Requirements

Install required Python package:

pip install opencv-python

macOS built-in tools used:

say (text-to-speech)
osascript (AppleScript automation)
Project Structure
MACburncore/
│
├── main.py
├── src/
│   ├── engine.py
│   ├── bridge.py
│   ├── compute.py
│   ├── overlay.py (optional, not used in final version)
│
└── README.md

Make sur eyou make a folder names src and put engine.py in it bridge.py , compute.py and overlay.py 
in the same src folder 

Your main.py should be OUTSIDE OF YOUR SCR FOLDER NOT IN IT 



How to Run

Clone or download the project:

git clone https://github.com/yourusername/surveillance-matrix.git
cd surveillance-matrix

Run the program:

python3 main.py
How It Works
The webcam initializes and captures a baseline frame
Each new frame is compared against the previous frame
Motion is detected using pixel difference analysis
If motion exceeds the defined threshold:
The event is logged
A voice alert is triggered
Optional system lock is executed
Voice Alert

macOS built-in speech system is used:

say "Intruder detected"

You can change the voice:

os.system("say -v Samantha 'Intruder detected'")
Screen Lock (Optional)
osascript -e 'tell application "System Events" to keystroke "q" using {control down, command down}'

Note: This requires Accessibility permissions enabled in macOS System Settings.

Sensitivity Tuning

Inside engine.py:

if motion_score > 5000:

Recommended values:

3000: highly sensitive
5000: balanced default
8000+: low sensitivity
Notes
Designed for macOS only
Requires webcam access
Performance depends on lighting conditions
Not intended as a production security system
