import pandas as pd
import joblib

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# ==========================================
# PATH CONFIGURATION
# ==========================================

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = (
    BASE_DIR.parent
    / "dataset"
    / "message_dataset"
    / "message_dataset.csv"
)

MODEL_PATH = BASE_DIR / "message_model.pkl"

# ==========================================
# LOAD DATASET
# ==========================================

print("Loading message dataset...")

df = pd.read_csv(DATA_PATH)

df = df.dropna(subset=["message", "label"])

df["message"] = df["message"].astype(str)

print("\nDataset loaded successfully!")
print("Total messages:", len(df))

print("\nLabel distribution:")
print(df["label"].value_counts())

# ==========================================
# PREPARE DATA
# ==========================================

X = df["message"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining messages:", len(X_train))
print("Testing messages:", len(X_test))

# ==========================================
# BUILD ML PIPELINE
# ==========================================

print("\nBuilding message classification model...")

model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 2),
            min_df=2,
            sublinear_tf=True
        )
    ),
    (
        "classifier",
        LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
            random_state=42
        )
    )
])

# ==========================================
# TRAIN MODEL
# ==========================================

print("\nTraining model...")

model.fit(X_train, y_train)

print("Training completed!")

# ==========================================
# MODEL EVALUATION
# ==========================================

print("\nEvaluating model...")

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, predictions))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

# ==========================================
# SAVE MODEL
# ==========================================

joblib.dump(model, MODEL_PATH)

print("\nModel saved successfully!")
print("Model location:", MODEL_PATH)