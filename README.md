#Designed to cleanup desktop files with Python

import os
import shutil

audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")


def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_image(file):
    return os.path.splitext(file)[1] in img

def is_video(file):
    return os.path.splitext(file)[1] in video
def is_screenshot(file):
    name, ext = os.path.splitext(file)
    return (ext in img) and "screenshot" in name.lower()


os.chdir("C:/Users/arnol/Desktop")

for file in os.listdir():
    if is_audio(file):
        shutil.move(file,"C:/Users/arnol/Music")
    elif is_video(file):
        shutil.move(file,"C:/Users/arnol/Video")
    elif is_image(file):
        if is_screenshot(file):
            shutil.move(file, "C:/Users/arnol/Pictures/Saved Pictures")
        else:
            shutil.move(file,"C:/Users/arnol/Pictures/Screenshots")
    else:
        shutil.move(file, "C:/Users/arnol/Documents/Misc")
print("File cleanup was successful!")
