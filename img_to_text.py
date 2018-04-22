import pytesseract
from PIL import Image
import cv2

def img_to_text(img):
    return pytesseract.image_to_string(Image.fromarray(img), lang="eng")