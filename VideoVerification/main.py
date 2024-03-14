from ultralytics import YOLO
import cv2
import numpy as np
from face_capture import capture
from id_recognition import id_capture
from text_extraction import pancard,aadharcard
def face_cap():
    return capture()
def id_recog():
    return id_capture()
def ocr():
    x=pancard()
def main():
    print(ocr())
main()