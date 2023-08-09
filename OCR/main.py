import pytesseract
import cv2
import PIL.Image

myconfig = "--psm 6 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open("2.png"), config = myconfig)
print(text)