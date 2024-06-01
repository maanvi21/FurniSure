from flask import Flask, request, render_template, send_file
import cv2
import numpy as np
from PIL import Image
import io

app = Flask(__name__)



@app.route('/scan')
def scan():
    return render_template("scan.html")

@app.route('/productdesc')
def productdesc():
    return render_template("productdesc.html")

@app.route('/confirm')
def confirmImage():
    return render_template("confirmImage.html")

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    text = request.form.get('text')
    #if file checks if the image what actually uploaded
    if file:
        # Read the image file into a numpy array of pixels 
        image = np.array(Image.open(file.stream))
        
        # Use OpenCV to add text to the image
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, text, (10, 50), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

        # Save the image to a BytesIO object
        _, img_encoded = cv2.imencode('.png', image)
        img_bytes = img_encoded.tobytes()
        img_stream = io.BytesIO(img_bytes)

        return send_file(img_stream, mimetype='image/png')




if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True)