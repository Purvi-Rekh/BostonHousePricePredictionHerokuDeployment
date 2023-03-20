import pickle
from flask import Flask,request,app,jsonify,url_for,render_template

import numpy as np
import pandas as pd

app = Flask(__name__)
# because we are running from venv/bin, give relative path from venv/bin to refmodel and scaling - 2 dict back
#python app.py
model = pickle.load(open("../../regmodel.pkl","rb"))
scaler = pickle.load(open("../../scaling.pkl","rb"))
@app.route('/')

def home():
    return render_template("home.html")

@app.route("/predict_api",methods=["POST"])

def predict_api():

    data=request.json["data"]

    print(data)
    listData = list(data.values())
    print(np.array(listData).reshape(1,-1)) #single data point or row with mtiple columns
    newData = scaler.transform(np.array(listData).reshape(1,-1))
    output = model.predict(newData)
    print(output[0])
    return jsonify(output[0])
@app.route("/predict",methods=["POST"])

def predict():


    data = [float(x) for x in request.form.values()]

    final_input = scaler.transform(np.array(data).reshape(1,-1))

    output = model.predict(final_input)[0]

    return render_template("home.html",prediction_text = "The house price prediction is {}".format(output))
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000,debug=True)

