
from pathlib import Path
from typing import Literal

import joblib

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .database import (
    initialize_database,
    save_prediction,
    get_predictions,
    update_review
)


# -----------------------------------
# PROJECT PATHS
# -----------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    BASE_DIR
    / "models"
    / "multilingual_routing_system.joblib"
)


# -----------------------------------
# LOAD ML MODEL
# -----------------------------------

if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"Model not found: {MODEL_PATH}"
    )

routing_system = joblib.load(MODEL_PATH)

model = routing_system["model"]

CONFIDENCE_THRESHOLD = routing_system[
    "confidence_threshold"
]

DEPARTMENTS = routing_system["departments"]


# -----------------------------------
# FASTAPI INITIALIZATION
# -----------------------------------

app = FastAPI(
    title="MultiLingua AI",
    description="Multilingual Campus Support Classification API",
    version="1.0.0"
)


@app.on_event("startup")
def startup():

    initialize_database()

    print("Database initialized!")
    print("ML model loaded successfully!")


# -----------------------------------
# INPUT SCHEMAS
# -----------------------------------

class PredictionRequest(BaseModel):

    message: str = Field(
        min_length=2,
        max_length=2000
    )

    language: Literal[
        "English",
        "Hindi",
        "Hinglish",
        "Punjabi"
    ]


class ReviewRequest(BaseModel):

    prediction_id: int = Field(gt=0)

    corrected_department: Literal[
        "IT",
        "Accounts",
        "Examination",
        "Hostel",
        "General"
    ]


# -----------------------------------
# HEALTH CHECK
# -----------------------------------

@app.get("/")
def home():

    return {
        "message": "Welcome to MultiLingua AI API",
        "status": "running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "confidence_threshold": CONFIDENCE_THRESHOLD
    }


# -----------------------------------
# PREDICTION ENDPOINT
# -----------------------------------

@app.post("/predict")
def predict(request: PredictionRequest):

    message = request.message.strip()

    if len(message) < 2:
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty"
        )

    model_input = (
        f"[{request.language}] {message}"
    )

    probabilities = model.predict_proba(
        [model_input]
    )[0]

    best_index = probabilities.argmax()

    department = model.classes_[best_index]

    confidence = float(
        probabilities[best_index]
    )

    if confidence >= CONFIDENCE_THRESHOLD:

        status = "AUTO_ROUTED"

    else:

        status = "HUMAN_REVIEW"

    prediction_id = save_prediction(
        message,
        request.language,
        department,
        confidence,
        status
    )

    return {

        "prediction_id": prediction_id,

        "message": message,

        "language": request.language,

        "predicted_department": department,

        "confidence": round(confidence, 4),

        "status": status,

        "confidence_threshold": CONFIDENCE_THRESHOLD

    }


# -----------------------------------
# PREDICTION HISTORY
# -----------------------------------

@app.get("/history")
def history():

    records = get_predictions()

    return {
        "total_records": len(records),
        "records": records
    }


# -----------------------------------
# HUMAN REVIEW QUEUE
# -----------------------------------

@app.get("/reviews")
def reviews():

    records = get_predictions(
        status="HUMAN_REVIEW"
    )

    return {
        "pending_reviews": len(records),
        "records": records
    }


# -----------------------------------
# HUMAN REVIEW SUBMISSION
# -----------------------------------

@app.post("/review")
def review(request: ReviewRequest):

    updated = update_review(
        request.prediction_id,
        request.corrected_department
    )

    if updated == 0:

        raise HTTPException(
            status_code=404,
            detail="Pending prediction not found"
        )

    return {

        "message": "Human review completed successfully",

        "prediction_id": request.prediction_id,

        "corrected_department": request.corrected_department

    }
