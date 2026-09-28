import joblib
import pandas as pd

model = joblib.load("model.pkl")

monthly_bill = float(input("Monthly bill: "))
internet_speed = float(input("Internet speed: "))
outage_count = float(input("Outage count: "))
service_quality = float(input("Service quality (1-10): "))
support_calls = float(input("Support calls: "))
tenure = float(input("Tenure (months): "))

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

if prediction[0] == 1:
    print("Customer likely to CHURN")
else:
    print("Customer likely to STAY")