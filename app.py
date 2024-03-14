from flask import Flask, request, render_template
from ultralytics import YOLO
import cv2
import numpy as np
from face_capture import capture
from id_recognition import id_capture
from text_extraction import pancard,aadharcard

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'button1' in request.form:
            # Button 1 was clicked
            a=capture()
            print(a)
        elif 'button2' in request.form:
            b=id_capture()
            print(b)
        elif 'button3' in request.form:
            c=pancard()
            d=aadharcard()
            print(c+" "+d)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
