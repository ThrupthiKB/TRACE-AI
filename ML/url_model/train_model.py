import pandas as pd
import joblib

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

print("Loading prepared dataset...")

data_path = Path(__file__).parent / "url_training_data.csv"

data = pd.read_csv(data_path)

X = data.drop("label", axis=1)
y = data["label"]

print("Dataset loaded:", len(data), "records")

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))

# Create Random Forest model
print("\nTraining Random Forest model...")

model = RandomForestClassifier(
    n_estimators=150,
    random_state=42,
    n_jobs=-1,
    class_weight="balanced"
)

model.fit(X_train, y_train)

print("Training completed!")

# Evaluate model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

# Save trained model
model_path = Path(__file__).parent / "url_model.pkl"

joblib.dump(model, model_path)

print("\nModel saved successfully!")
print("Location:", model_path)