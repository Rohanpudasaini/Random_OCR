#!/usr/bin/python3
import pytesseract
from PIL import Image
import os

os.chdir(r'/home/r0h8n/Desktop/Python/Tryhackme/')
i= 1
print("\n")
for f in os.listdir():
    if '.jpeg' in f:
        img = Image.open(f)
        text = pytesseract.image_to_string(img)
        fil = open("final.txt","a")
        fil.write(str(i))
        fil.write("\n")
        fil.write(text)
        fil.write("\n\n\n\n")
fil.close()
