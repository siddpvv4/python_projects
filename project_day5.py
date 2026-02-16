import os
import shutil

path = input("Enter folder path: ")
path = r"{}".format(path)

files = os.listdir(path)

# folder names
images = path + "\\Images"
docs = path + "\\Documents"
videos = path + "\\Videos"
music = path + "\\Music"
programs = path + "\\Programs"

# ---------- PHASE 1: CREATE FOLDERS ----------
for folder in [images, docs, videos, music, programs]:
    if not os.path.exists(folder):
        os.makedirs(folder)

print("Folders created successfully!")

# ---------- PHASE 2: MOVE FILES ----------
for file in files:

    full_path = os.path.join(path, file)

    # skip folders
    if os.path.isdir(full_path):
        continue

    name, ext = os.path.splitext(file)
    ext = ext.lower()

    # images
    if ext in ['.jpg', '.jpeg', '.png', '.webp']:
        shutil.move(full_path, images)

    # videos
    elif ext in ['.mp4', '.mkv']:
        shutil.move(full_path, videos)

    # documents
    elif ext in ['.pdf', '.pptx', '.docx', '.txt']:
        shutil.move(full_path, docs)

    # music
    elif ext in ['.mp3']:
        shutil.move(full_path, music)

    # programs
    elif ext in ['.exe', '.msix', '.zip']:
        shutil.move(full_path, programs)

print("Files organized successfully!")
