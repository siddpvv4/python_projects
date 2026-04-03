import sounddevice as sd
import numpy as np
import speech_recognition as sr
import webbrowser
import os
import scipy.io.wavfile as wav
import time

# --- YOUR CUSTOM PHRASES ---
# Replace the "LINK_HERE" with your actual YouTube URLs
VIDEOS = {
    "i am iron man": "https://youtu.be/dD12aw5KYug?si=sIx7iNJuxxNat3re",
    "bankai": "https://youtu.be/Er-6Mscj7Bo?si=fwKGsXG1x-vCIh7F",
    "wake up daddy's home": "https://www.youtube.com/watch?v=W54Y0cn78NY",
    "domain expansion": "https://youtu.be/Qzorv4lK10I?si=Io7ZG0HQNXI71kaj"

}

THRESHOLD = 40.0  # Loudness to trigger the mic (Clap or "Hey!")
DURATION = 4      # Seconds to record (increased for longer phrases)
FS = 44100        # Sample rate

def start_jarvis():
    recognizer = sr.Recognizer()
    
    print("--- JARVIS: STANDBY MODE ---")
    print(f"Waiting for a clap or loud sound to wake up...")

    # PHASE 1: Wait for the "Wake Sound"
    with sd.InputStream() as stream:
        while True:
            data, _ = stream.read(1024)
            volume = np.linalg.norm(data) * 10
            if volume > THRESHOLD:
                print(f"🎤 [ACTIVE] Listening for your command... (4 Seconds)")
                # PHASE 2: Record your voice
                recording = sd.rec(int(DURATION * FS), samplerate=FS, channels=1)
                sd.wait() 
                wav.write("temp_voice.wav", FS, (recording * 32767).astype(np.int16))
                break

    # PHASE 3: Recognize the words
    try:
        print("🔍 Processing speech...")
        with sr.AudioFile("temp_voice.wav") as source:
            audio = recognizer.record(source)
            # Using Google's free web API
            text = recognizer.recognize_google(audio).lower()
            print(f"💬 You said: '{text}'")

            # PHASE 4: Match the phrase
            found = False
            for phrase, url in VIDEOS.items():
                if phrase in text:
                    print(f"✅ Match Found: {phrase}. Opening Video...")
                    webbrowser.open(url)
                    found = True
                    break
            
            if not found:
                print("❌ No matching phrase found.")
            
            # Cleanup and Exit
            if os.path.exists("temp_voice.wav"):
                os.remove("temp_voice.wav")
            
            print("🎬 Task complete. Script shutting down.")
            os._exit(0)

    except sr.UnknownValueError:
        print("⚠️ Jarvis couldn't understand the audio. Shutting down.")
        os._exit(0)
    except Exception as e:
        print(f"⚠️ Error: {e}")
        os._exit(0)

if __name__ == "__main__":
    start_jarvis()