"""
sudo apt-get update
sudo apt-get install tesseract-ocr
sudo apt-get install libtesseract-dev
"""
import cv2
import pytesseract


def photo_2_text(path_to_image):
    img = cv2.imread(path_to_image)
    text = pytesseract.image_to_string(img)
    if text == '':
        return 'can`t recognize'
    return text

# https://translate.yandex.com/ocr
"""
img = cv2.imread('ss.jpg')
text = pytesseract.image_to_string(img)
print(text)"""