import multiprocessing
import time

def worker_loop(worker_id: int):
    print(f"[Worker {worker_id}] started")
    x = 1.0

    while True:
        x = (x * 1.0001) % 999999


class PerformanceOverloadController:
    """Simple CPU worker controller."""

    def __init__(self):
        self.processes = []
        self.core_count = max(1, multiprocessing.cpu_count() - 1)

    def start(self):
        print(f"[*] Starting {self.core_count} workers...")

        for i in range(self.core_count):
            p = multiprocessing.Process(target=worker_loop, args=(i,))
            p.daemon = True
            p.start()
            self.processes.append(p)

    def stop(self):
        print("[*] Stopping workers...")

        for p in self.processes:
            p.terminate()
