import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Load data
df = pd.read_csv("data.csv")

# Features
X = df[
    [
        "monthly_bill",
        "internet_speed",
        "outage_count",
        "service_quality",
        "support_calls",
        "tenure"
    ]
]

# Target
y = df["churn"]

# Create model
model = LogisticRegression()

# Train model
model.fit(X, y)
print("Coefficients:")
print(model.coef_)

print("Intercept:")
print(model.intercept_)
# Save model
joblib.dump(model, "model.pkl")

print("Model trained successfully!")