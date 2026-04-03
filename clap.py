import sounddevice as sd
import numpy as np
import webbrowser
import os
import time

# --- THE "ONE-SHOT" CONFIG ---
THRESHOLD = 50.0       # High threshold to avoid ghosts
VIDEO_URL = "https://www.youtube.com/watch?v=W54Y0cn78NY"

def callback(indata, frames, time_info, status):
    # Calculate volume
    volume_norm = np.linalg.norm(indata) * 10
    
    if volume_norm > THRESHOLD:
        print(f"🚀 [CRITICAL HIT] Volume: {volume_norm:.2f}")
        print("🎬 Mission Accomplished. Opening video and exiting...")
        
        # 1. Open the video
        webbrowser.open(VIDEO_URL)
        
        # 2. Hard exit (Kills the script instantly so no second tab can open)
        os._exit(0) 

print("--- JARVIS: SINGLE-SHOT MODE ---")
print(f"Listening for ONE loud clap (>{THRESHOLD})...")

try:
    with sd.InputStream(callback=callback):
        while True:
            # The script just waits here until it hears the clap
            sd.sleep(1000)
except KeyboardInterrupt:
    print("\nManual stop.")