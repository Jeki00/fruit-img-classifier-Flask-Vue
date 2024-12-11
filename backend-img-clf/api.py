# import flast module
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from keras.models import load_model
from keras.layers import TFSMLayer
import tensorflow as tf
import os
from werkzeug.utils import secure_filename
import numpy as np

import cv2

# instance of flask application
app = Flask(__name__, template_folder='../views')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# model_path =   # Adjust the path if necessary
model = load_model("../models/fruit-clf-model (1).h5", compile=False)
# img_clf_model =load_model("/models/img_classifier.keras")
model.compile(loss='categorical_crossentropy', metrics=['acc'],optimizer='adam')

app.config['UPLOAD_FOLDER'] = "../img"



# home route that returns below text when root url is accessed
@app.route("/classifier",methods=['GET', 'POST'])
@cross_origin()
def classification():
    if request.method =="POST":
        file = request.files['image']
        # print(file)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        img = cv2.imread(f'../img/{filename}')
        img = cv2.resize(img, (200, 200))

        # img = np.array(img)/255.0


        img = np.expand_dims(img, axis=0)
        # img = np.array(img, dtype=np.float32)
        # print(img.shape)

        output = { 0:'apple',1:'banana',2:'mixed',3:'orange'}


        try:
            predict = model.predict(img)
            # print(predict)
            # print(output[np.argmax(predict)])
        except Exception as e:
            print(f"Error: {e}")
        # predict = model.predict(img)
        return jsonify({
            'msg':'berhasil',
            'data':filename,
            'prediction': output[np.argmax(predict)]
        })
    else:
        return render_template('index.html')


if __name__ ==  '__main__':
    app.run(debug = True)