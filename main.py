import time
import multiprocessing

from src.bridge import MacSystemArchitectureBridge
from src.engine import SurveillanceMatrixController
from src.overlay import EmergencyOverlay
from src.compute import PerformanceOverloadController


def main():
    print("====================================")
    print("   Surveillance System Starting     ")
    print("====================================")

    bridge = MacSystemArchitectureBridge()
    overlay = EmergencyOverlay()
    compute = PerformanceOverloadController()

    engine = SurveillanceMatrixController(bridge, overlay, compute)

    print("[*] Boot delay...")

    for i in range(3, 0, -1):
        print(f"Starting in {i}...")
        time.sleep(1)

    engine.run()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
