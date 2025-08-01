# -*- coding: utf-8 -*-
"""Model Training ML Project Sid.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1upjA-7BrBhrT1S0EBv3dCU8QbJR05JsK
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
import joblib
import os

# Set file paths
input_path = "/content/drive/MyDrive/PW Assignments/engineered_crypto_data.csv"
model_dir = "/content/drive/MyDrive/PW Assignments/models"
os.makedirs(model_dir, exist_ok=True)

# Load the dataset
df = pd.read_csv(input_path)

# Strip column names (just in case)
df.columns = df.columns.str.strip()

# Define features and target based on what exists
features = ['total_volume', 'market_cap', 'liquidity_ratio',
            'price_change_ratio']  # skipping volatility_range and cap_per_supply as placeholder

target = 'liquidity_level'

# Split into X and y
X = df[features]
y = df[target]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("Model trained.")
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Save model and scaler
joblib.dump(model, os.path.join(model_dir, "trained_model.pkl"))
joblib.dump(scaler, os.path.join(model_dir, "scaler.pkl"))

print(f"Model saved to: {model_dir}/trained_model.pkl")
print(f"Scaler saved to: {model_dir}/scaler.pkl")