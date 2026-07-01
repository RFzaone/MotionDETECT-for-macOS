# MotionDETECT-for-macOS

# Surveillance Matrix (Mac Motion Detection System)

`MotionDETECT-for-macOS` is a lightweight Python-based motion detection system built specifically for macOS using OpenCV. It monitors webcam input, detects movement through frame comparison, and triggers local automated alerts like text-to-speech notifications or instant system lockouts.

## 🚀 Features
* **Real-time webcam motion detection** via OpenCV.
* **Pixel-based analysis** optimized for stability and low CPU usage.
* **macOS text-to-speech alerts** using the native system `say` command.
* **Optional screen lock integration** via AppleScript for instant security.
* **Automated event logging** saved directly to a local text file.
* **Headless design** requiring no complex graphical user interface (GUI).

## 📋 Requirements
Your system needs the following Python package installed:
```bash
pip install opencv-python
```

The system relies on these built-in macOS native tools:
* `say` (Native text-to-speech engine)
* `osascript` (AppleScript automation engine)

## 📁 Project Structure
Ensure your files are organized exactly like this. The `main.py` file **must stay outside** of the `src` directory.

```text
MACburncore/
│
├── main.py
└── src/
    ├── engine.py
    ├── bridge.py
    ├── compute.py
    └── overlay.py (optional, not used in final version)
```

> **Note:** Create a folder named `src` and place `engine.py`, `bridge.py`, `compute.py`, and `overlay.py` inside it. Your `main.py` should be in the root folder, **NOT** inside the `src` folder.

## 💻 How to Run

1.  download the project:
   go to each file and click download 'dont download license or readme you dont need to'

## ⚙️ How It Works
1. The webcam initializes and captures a baseline environmental frame.
2. Each subsequent frame is compared against the previous frame using pixel difference analysis.
3. If the movement threshold is crossed, the system executes three tasks:
   * Logs the timestamped event to a local file.
   * Triggers the native macOS voice alert.
   * Executes the optional system screen lockout.

### Customizing Voice Alerts
The script leverages the built-in macOS speech architecture:
```bash
say "Intruder detected"
```
You can modify your Python script to use specific system voices (like Samantha):
```python
import os
os.system("say -v Samantha 'Intruder detected'")
```

### Automatic Screen Lock (Optional)
To lock your Mac instantly when motion is detected, the script fires an AppleScript command:
```bash
osascript -e 'tell application "System Events" to keystroke "q" using {control down, command down}'
```
*Note: This specific feature requires you to grant **Accessibility** permissions to your Terminal or IDE inside macOS System Settings.*

## 🔧 Sensitivity Tuning
You can tweak the detection thresholds directly inside `src/engine.py`:
```python
if motion_score > 5000:
```
* **3000:** Highly sensitive (picks up minor lighting shifts or shadows).
* **5000:** Balanced default (recommended for most indoor environments).
* **8000+:** Low sensitivity (only triggers for large, obvious movements).

## ⚠️ Important Notes
* Designed exclusively for **macOS** environments.
* Requires hardware webcam access permissions.
* Environmental performance depends heavily on ambient lighting conditions.
* This project is a developer tool and is not intended as a production-grade commercial security platform.

