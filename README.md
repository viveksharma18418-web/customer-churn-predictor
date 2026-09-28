# Customer Churn Predictor

## Overview

A machine learning application that predicts whether a customer is likely to **CHURN** or **STAY** based on customer service and usage features.

The project demonstrates a complete local workflow from training a machine learning model to serving predictions through a FastAPI API and running the API inside Docker.

## Features

* Logistic Regression classification
* Customer churn prediction
* Saved trained model using Joblib
* Python prediction script
* FastAPI REST API
* Interactive FastAPI Swagger documentation
* Docker containerization
* Local end-to-end testing

## Project Structure

```text
customer churn predictor/
│
├── app.py
├── data.csv
├── Dockerfile
├── model.pkl
├── predict.py
├── requirements.txt
├── train.py
└── .gitignore
```

## Machine Learning Features

The model uses six customer features:

* Monthly bill
* Internet speed
* Outage count
* Service quality
* Support calls
* Customer tenure

The target variable is:

```text
churn
```

where:

* `1` = CHURN
* `0` = STAY

## Machine Learning Workflow

```text
Customer Dataset
       ↓
Feature Selection
       ↓
Logistic Regression
       ↓
Model Training
       ↓
Save model.pkl
       ↓
Prediction
       ↓
FastAPI
       ↓
Docker
```

## Model

The project uses **Logistic Regression** from scikit-learn.

The trained model is saved as:

```text
model.pkl
```

using Joblib.

## Prediction Script

The `predict.py` script allows a user to enter customer information directly from the terminal.

Example input:

```text
Monthly bill: 1500
Internet speed: 20
Outage count: 12
Service quality: 3
Support calls: 8
Tenure: 2
```

Prediction:

```text
Customer likely to CHURN
```

## FastAPI

The trained model is exposed through a FastAPI REST API.

Start the API locally with:

```bash
uvicorn app:app --reload
```

Open the interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

The `/predict` endpoint accepts the six customer features and returns a churn prediction.

Example:

```text
GET /predict?monthly_bill=1500&internet_speed=20&outage_count=12&service_quality=3&support_calls=8&tenure=2
```

Response:

```json
{
  "prediction": "CHURN"
}
```

The API was tested successfully with an HTTP 200 response.

## Docker

The application is containerized using Docker.

Build the Docker image:

```bash
docker build -t churn-predictor .
```

Run the container:

```bash
docker run -d --name churn-api -p 8000:8000 churn-predictor
```

The running container exposes the FastAPI application on port `8000`.

Swagger documentation can then be accessed at:

```text
http://127.0.0.1:8000/docs
```

The Dockerized `/predict` endpoint was successfully tested and returned:

```json
{
  "prediction": "CHURN"
}
```

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Logistic Regression
* Joblib
* FastAPI
* Uvicorn
* Docker

## Project Status

The complete local workflow has been tested successfully:

```text
Model training          ✅
Model saving            ✅
CLI prediction          ✅
FastAPI startup         ✅
FastAPI prediction      ✅
Docker image build      ✅
Docker container        ✅
Docker API prediction   ✅
```

## Future Improvements

Possible future improvements include:

* Train/test evaluation metrics
* Feature scaling and preprocessing pipeline
* Automated testing
* CI/CD with GitHub Actions
* Model monitoring
* Data drift monitoring
* Cloud deployment
* Automated model retraining
