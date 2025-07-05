import os
import ctypes
import sys
import time

def shutdown_now():
    os.system("shutdown /s /t 0")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == "__main__":
    block_duration = 60  # seconds
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()
    print(f"System will shut down now.")
    shutdown_now()

