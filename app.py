from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route("/")
def home():
    return "Welcome to my ML prediction API!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({"prediction": float(prediction[0])})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
