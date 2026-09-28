from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("model.pkl")

@app.get("/")
def home():
    return {"message": "Customer Churn Predictor"}

@app.get("/predict")
def predict(
    monthly_bill: float,
    internet_speed: float,
    outage_count: float,
    service_quality: float,
    support_calls: float,
    tenure: float
):
    data = pd.DataFrame([[
        monthly_bill,
        internet_speed,
        outage_count,
        service_quality,
        support_calls,
        tenure
    ]], columns=[
        "monthly_bill",
        "internet_speed",
        "outage_count",
        "service_quality",
        "support_calls",
        "tenure"
    ])

    prediction = model.predict(data)

    return {
        "prediction":
        "CHURN" if prediction[0] == 1 else "STAY"
    }