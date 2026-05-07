import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import os

# Load config
with open("config.json") as f:
    config = json.load(f)

# Load dataset
df = pd.read_csv("dataset/train.csv")
X = df.drop('label', axis=1)
y = df['label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=config.get("seed", 42)
)

# Train model
print("Training model...")
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)

# Save metrics
metrics = {
    "accuracy": float(accuracy),
    "precision": float(precision),
    "recall": float(recall),
    "f1_score": float(f1)
}

# Create models directory
os.makedirs("models", exist_ok=True)

# Save model
joblib.dump(model, "models/model.pkl")

# Save metrics
with open("models/metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)

print(f"\n✓ Model trained successfully!")
print(f"  Accuracy:  {accuracy:.4f}")
print(f"  Precision: {precision:.4f}")
print(f"  Recall:    {recall:.4f}")
print(f"  F1-Score:  {f1:.4f}")
print(f"\nModel saved to: models/model.pkl")
print(f"Metrics saved to: models/metrics.json")
