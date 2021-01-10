from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
from tensorflow.keras import backend
from tensorflow.keras.models import load_model
import joblib

app = Flask(__name__)

@app.before_first_request
def load_model_to_app():
    app.predictor = joblib.load("static/model/svc.pkl")
    
    
@app.route("/")
def index():
    return render_template('index.html', pred = 0)
    
@app.route('/predict', methods=['POST'])
def predict():
    data = [request.form['nscore'],
            request.form['escore'],
            request.form['oscore'], 
            request.form['ascore'],
            request.form['cscore'],
            request.form['impulsive'],
            request.form['ss']
            ]

    data = np.array([np.asarray(data, dtype=float)])

    predictions = app.predictor.predict(data)
    print('INFO Predictions: {}'.format(predictions))

    class_ = np.where(predictions == np.amax(predictions, axis=1))[1][0]

    return render_template('index.html', pred=class_)
    
def main():
    """Run the app."""
    app.run(host='0.0.0.0', port=3333, debug=False)  # nosec


if __name__ == '__main__':
    main()