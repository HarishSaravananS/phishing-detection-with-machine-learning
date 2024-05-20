from flask import Flask, render_template, request

import warnings
import os
import datetime
import threading
import logging

from flask import Flask, request, jsonify, render_template
import joblib


import pickle
import logging
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load('phishing2_model.pkl')

# Instantiate PredictPipeline once


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    from utils.url_parser import URLParser
    try:
        # Extract URL from form data
        url = request.form['url']
        
        # Extract features from the URL
        parser = URLParser(url)

        # Match expected features
        

        # Reshape features for prediction
        prediction = model.predict(parser.np_array())
        
      

        # Convert prediction to human-readable format
        prediction = "phishing" if prediction == 1 else "legitimate"
        
        return render_template('result.html', url=url, prediction=prediction)
    
    except Exception as e:
        # Log the error
        app.logger.error(f"An error occurred: {str(e)}")
        # Return user-friendly error message
        error_message = "An error occurred while processing your request. Please try again later."
        return render_template('error.html', error_message=error_message)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)

