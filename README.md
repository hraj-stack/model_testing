# model_testing

A Flask-based machine learning application that uses a Random Forest classifier to predict customer purchase behavior.

## Overview

This project demonstrates a complete ML pipeline including:
- Data loading and preprocessing from a MySQL database
- Model training using scikit-learn
- REST API deployment with Flask

## Features

- **Machine Learning Model**: Random Forest Classifier for binary classification
- **REST API**: Flask-based endpoint for making predictions
- **Database Integration**: MySQL connection for data retrieval
- **Model Serialization**: Trained model saved using joblib

## Project Structure
model_testing/ ├── app.py # Flask application with prediction endpoint ├── sqll_connect.py # Database connection and model training script ├── rf_model.pkl # Trained Random Forest model ├── requirements.txt # Python dependencies └── README.md # Project documentation


## Dependencies

- numpy
- pandas
- flask
- mysql-connector-python
- scikit-learn

## Installation

1. Clone the repository:
```bash
git clone https://github.com/hraj-stack/model_testing.git
cd model_testing

2.Install dependencies:
pip install -r requirements.txt


3.Update database credentials in sqll_connect.py:
conn = pymysql.connect(
    host="local_host",
    user="root",
    password="123456789@",)


Training the Model
python sqll_connect.py

Start the Flask application:
python app.py

Making Predictions
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"input": [20, 50000]}'


response
{
  "prediction": 1
}


Dataset
The model uses the Social Network Ads dataset with features:

Age
EstimatedSalary
Gender (dropped during preprocessing)
User ID (dropped during preprocessing)
Target: Purchased (binary classification)
Model Performance
Algorithm: Random Forest Classifier
Train/Test Split: 80/20
Random State: 42
Notes
The model file rf_model.pkl is pre-trained and ready for use
Error handling is implemented in the prediction endpoint
Debug mode is enabled in Flask for development
Future Improvements
Add model evaluation metrics (accuracy, precision, recall)
Implement authentication for the API
Add data validation for input features
Deploy to production environment
