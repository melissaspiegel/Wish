import time
import os
import datetime
import subprocess
import tkinter as tk
from tkinter import simpledialog

# Directory to store logs
LOG_DIR = os.path.expanduser("~/standup_logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Timer interval (in minutes)
INTERVAL = 30  # Change to your preferred time

def send_mac_notification(title, message):
    """Send a native macOS notification using AppleScript."""
    script = f'display notification "{message}" with title "{title}"'
    subprocess.run(["osascript", "-e", script])

def log_standup():
    """Prompt the user to log what they are working on."""
    now = datetime.datetime.now()
    today_log = os.path.join(LOG_DIR, f"standup_{now.date()}.txt")

    print(f"[{now.strftime('%H:%M:%S')}] Triggering standup reminder...")

    # macOS Native Notification
    try:
        send_mac_notification("Standup Reminder", "What are you working on?")
        print("✅ Notification sent!")
    except Exception as e:
        print(f"❌ Notification failed: {e}")

    # GUI Input Prompt
    try:
        root = tk.Tk()
        root.withdraw()
        entry = simpledialog.askstring("Standup Log", "What are you doing right now?")
        root.destroy()
    except Exception as e:
        print(f"❌ Input dialog failed: {e}")
        entry = None

    # Save entry if provided
    if entry:
        with open(today_log, "a") as file:
            file.write(f"[{now.strftime('%H:%M')}] {entry}\n")
        print("✅ Entry saved!")

# Run the timer in the background
if __name__ == "__main__":
    print("🚀 Standup logger started...")
    while True:
        log_standup()
        time.sleep(INTERVAL * 60)  # Convert minutes to seconds