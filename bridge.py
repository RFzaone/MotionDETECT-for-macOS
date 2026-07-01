import os
import datetime
import multiprocessing

class MacSystemArchitectureBridge:
    """System helper layer (sound, logs, lock)."""

    def execute_async_audio_siren(self, text: str) -> None:
        os.system(f"say '{text}' &")

    def dispatch_system_lockout(self) -> None:
        os.system("pmset displaysleepnow")

    def write_forensic_manifest(self, score: float) -> None:
        path = os.path.join(
            os.path.expanduser("~"),
            "Desktop",
            "bunkeros_log.txt"
        )

        log = f"""
=== INCIDENT LOG ===
Time: {datetime.datetime.now()}
Score: {score}
CPU Cores: {multiprocessing.cpu_count()}
====================
"""

        with open(path, "a") as f:
            f.write(log)
