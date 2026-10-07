from pathlib import Path
from fastapi import FastAPI, HTTPException
from backend.prediction_service import PredictionService
from backend.schemas import CustomerData, PredictionResponse
from backend.exceptions import PredictionError
from backend.exceptions import PredictionError

app = FastAPI(title="Customer Churn Prediction API")


# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "final_logistic_regression_model.pkl"
PREPROCESSOR_PATH = BASE_DIR / "preprocessor.pkl"

# Initialize prediction service
prediction_service = PredictionService(
    MODEL_PATH,
    PREPROCESSOR_PATH
)


@app.get("/")
def home():
    return {"message": "Customer Churn API is running"}


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        **prediction_service.health_status()
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(data: CustomerData):
    try:
        return prediction_service.predict(data)
    except PredictionError as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )