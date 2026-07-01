import cv2
import time
import os

class SurveillanceMatrixController:

    def __init__(self, bridge, overlay, compute):
        self.bridge = bridge
        self.overlay = overlay
        self.compute = compute
        self.cap = None

    def run(self):
        print("[*] Starting camera...")

        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            print("[-] Camera not accessible")
            return

        # quick stabilise (not slow)
        time.sleep(2)

        ret, frame1 = self.cap.read()
        if not ret:
            print("[-] Camera read failed")
            return

        gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)

        print("[+] Monitoring motion...")

        frame_id = 0

        while True:
            ret, frame2 = self.cap.read()
            if not ret:
                continue

            gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

            diff = cv2.absdiff(gray1, gray2)
            _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
            motion_score = cv2.countNonZero(thresh)

            # debug
            if frame_id % 10 == 0:
                print(f"Motion score: {motion_score}")

            # =========================
            # 🚨 TRIGGER
            # =========================
            if motion_score > 5000:
                print("\n[🚨] INTRUDER DETECTED")

                # log
                self.bridge.write_forensic_manifest(motion_score)

                # 🔊 FIXED SOUND (THIS WAS YOUR ISSUE)
                os.system("say 'Intruder detected'")

                # optional lock (safe macOS method)
                os.system(
                    "osascript -e 'tell application \"System Events\" to keystroke \"q\" using {control down, command down}'"
                )

                return

            gray1 = gray2
            frame_id += 1

            time.sleep(0.02)
