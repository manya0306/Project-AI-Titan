from datetime import datetime
import os
import subprocess
import webbrowser
import shutil


def open_target(target: str) -> bool:
    try:
        target = target.strip()

        if target.startswith("http://") or target.startswith("https://"):
            webbrowser.open(target)
            return True

        if os.path.exists(target):
            subprocess.Popen(target)
            return True

        exe_path = shutil.which(target)
        if exe_path:
            subprocess.Popen(exe_path)
            return True

        os.system(f'start "" "{target}"')
        return True

    except Exception as e:
        print("OPEN ERROR:", repr(e))
        return False


def get_time():
    return datetime.now().strftime("%I:%M %p")

def get_date():
    return datetime.now().strftime("%d-%m-%Y")

def google_search(query: str) -> bool:
    try:
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        return True
    except Exception as e:
        print("SEARCH ERROR:", repr(e))
        return False