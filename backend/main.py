from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import pandas as pd
import joblib
import sys

# =====================================================
# PROJECT PATHS
# =====================================================

project_root = Path(__file__).resolve().parent.parent

url_model_folder = project_root / "ML" / "url_model"
message_model_folder = project_root / "ML" / "message_model"

# Import URL feature extractor
sys.path.append(str(url_model_folder))
from url_features import extract_url_features


# =====================================================
# CREATE FASTAPI APPLICATION
# =====================================================

app = FastAPI(
    title="TRACE API",
    description="AI-powered Digital Threat Intelligence Platform",
    version="1.0"
)


# =====================================================
# LOAD TRAINED ML MODELS
# =====================================================

url_model_path = url_model_folder / "url_model.pkl"
message_model_path = message_model_folder / "message_model.pkl"

url_model = joblib.load(url_model_path)
message_model = joblib.load(message_model_path)


# =====================================================
# REQUEST FORMATS
# =====================================================

class URLRequest(BaseModel):
    url: str


class MessageRequest(BaseModel):
    message: str


# =====================================================
# HOME ENDPOINT
# =====================================================

@app.get("/")
def home():
    return {
        "message": "TRACE API is running!",
        "modules": [
            "URL Intelligence",
            "Message Intelligence"
        ]
    }


# =====================================================
# URL INTELLIGENCE ENDPOINT
# =====================================================

@app.post("/analyze-url")
def analyze_url(request: URLRequest):

    try:
        url = request.url.strip()

        if not url:
            raise HTTPException(
                status_code=400,
                detail="Please provide a URL."
            )

        # Extract URL features
        features = extract_url_features(url)

        # Prepare model input
        input_data = pd.DataFrame([features])

        # Predict
        prediction = int(url_model.predict(input_data)[0])

        probabilities = url_model.predict_proba(input_data)[0]
        confidence = round(float(max(probabilities)) * 100, 2)

        result = (
            "PHISHING"
            if prediction == 0
            else "LEGITIMATE"
        )

        return {
            "url": url,
            "result": result,
            "prediction": prediction,
            "model_confidence": confidence,
            "features": features
        }

    except HTTPException:
        raise

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


# =====================================================
# MESSAGE INTELLIGENCE ENDPOINT
# =====================================================

@app.post("/analyze-message")
def analyze_message(request: MessageRequest):

    try:
        message = request.message.strip()

        if not message:
            raise HTTPException(
                status_code=400,
                detail="Please provide a message."
            )

        # Predict message category
        prediction = message_model.predict([message])[0]

        # Get model confidence
        probabilities = message_model.predict_proba([message])[0]
        confidence = round(float(max(probabilities)) * 100, 2)

        # Classify result
        result = (
            "SUSPICIOUS"
            if prediction == "spam"
            else "LEGITIMATE"
        )

        return {
            "message": message,
            "result": result,
            "prediction": prediction,
            "model_confidence": confidence
        }

    except HTTPException:
        raise

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )