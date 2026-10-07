from typing import Literal
from pydantic import BaseModel, Field


class CustomerData(BaseModel):
    Country: str
    State: str
    Latitude: float = Field(ge=-90, le=90)
    Longitude: float = Field(ge=-180, le=180)
    Gender: Literal["Male", "Female"]
    Senior_Citizen: Literal["Yes", "No"]
    Partner: Literal["Yes", "No"]
    Dependents: Literal["Yes", "No"]
    Tenure_Months: int = Field(ge=0)
    Phone_Service: Literal["Yes", "No"]
    Multiple_Lines: Literal["Yes", "No", "No phone service"]
    Internet_Service: Literal["DSL", "Fiber optic", "No"]
    Online_Security: Literal["Yes", "No", "No internet service"]
    Online_Backup: Literal["Yes", "No", "No internet service"]
    Device_Protection: Literal["Yes", "No", "No internet service"]
    Tech_Support: Literal["Yes", "No", "No internet service"]
    Streaming_TV: Literal["Yes", "No", "No internet service"]
    Streaming_Movies: Literal["Yes", "No", "No internet service"]
    Contract: Literal["Month-to-month", "One year", "Two year"]
    Paperless_Billing: Literal["Yes", "No"]
    Payment_Method: Literal[
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
    Monthly_Charges: float = Field(ge=0)
    Total_Charges: float = Field(ge=0)


class PredictionResponse(BaseModel):
    prediction: int
    churn_probability: float
    risk_level: str
    message: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "prediction": 1,
                "churn_probability": 0.7989,
                "risk_level": "High",
                "message": "Customer is likely to churn."
            }
        }
    }