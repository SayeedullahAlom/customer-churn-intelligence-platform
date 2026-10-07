from pathlib import Path
from fastapi import FastAPI, HTTPException
from backend.prediction_service import PredictionService
from backend.schemas import CustomerData, PredictionResponse
from backend.exceptions import PredictionError


app = FastAPI(
    title="Customer Churn Prediction API",
    description="API for predicting customer churn probability and risk level using a trained machine learning model.",
    version="1.0.0"
)


# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "final_logistic_regression_model.pkl"
PREPROCESSOR_PATH = BASE_DIR / "preprocessor.pkl"

# Initialize prediction service
prediction_service = PredictionService(
    MODEL_PATH,
    PREPROCESSOR_PATH
)


@app.get(
    "/",
    summary="API welcome",
    description="Returns a simple message confirming that the Customer Churn API is running."
)
def home():
    return {"message": "Customer Churn API is running"}


@app.get(
    "/health",
    summary="Check API health",
    description="Returns the API status and confirms that the model and preprocessor are loaded."
)
def health_check():
    return {
        "status": "healthy",
        **prediction_service.health_status()
    }


@app.post(
    "/predict",
    response_model=PredictionResponse,
    summary="Predict customer churn",
    description="Predicts the probability that a customer will churn and assigns a risk level.",
    responses={
        500: {
            "description": "Prediction failed due to a server-side error."
        }
    }
)
def predict(data: CustomerData):
    try:
        return prediction_service.predict(data)
    except PredictionError as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )