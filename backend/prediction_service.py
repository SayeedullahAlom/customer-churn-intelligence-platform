import logging

import joblib
import pandas as pd

from backend.config import CHURN_THRESHOLD
from backend.exceptions import PredictionError

class PredictionService:

    def __init__(self, model_path, preprocessor_path):
        self.model = joblib.load(model_path)
        self.preprocessor = joblib.load(preprocessor_path)


    def health_status(self):
        return {
            "model_loaded": self.model is not None,
            "preprocessor_loaded": self.preprocessor is not None,
            "churn_threshold": CHURN_THRESHOLD
        }
    

    def prepare_input(self, data):
        return pd.DataFrame([{
            "Country": data.Country,
            "State": data.State,
            "Latitude": data.Latitude,
            "Longitude": data.Longitude,
            "Gender": data.Gender,
            "Senior Citizen": data.Senior_Citizen,
            "Partner": data.Partner,
            "Dependents": data.Dependents,
            "Tenure Months": data.Tenure_Months,
            "Phone Service": data.Phone_Service,
            "Multiple Lines": data.Multiple_Lines,
            "Internet Service": data.Internet_Service,
            "Online Security": data.Online_Security,
            "Online Backup": data.Online_Backup,
            "Device Protection": data.Device_Protection,
            "Tech Support": data.Tech_Support,
            "Streaming TV": data.Streaming_TV,
            "Streaming Movies": data.Streaming_Movies,
            "Contract": data.Contract,
            "Paperless Billing": data.Paperless_Billing,
            "Payment Method": data.Payment_Method,
            "Monthly Charges": data.Monthly_Charges,
            "Total Charges": data.Total_Charges
        }])
    

    def predict(self, data):
        try:
            input_data = self.prepare_input(data)
            processed_data = self.preprocessor.transform(input_data)

            probability = self.model.predict_proba(processed_data)[0][1]

            prediction = int(probability >= CHURN_THRESHOLD)

            if prediction == 1:
                risk_level = "High"
                message = "Customer is likely to churn."
            else:
                risk_level = "Low"
                message = "Customer is unlikely to churn."

            return {
                "prediction": prediction,
                "churn_probability": round(float(probability), 4),
                "risk_level": risk_level,
                "message": message
            }

        except Exception as exc:
            raise PredictionError("Prediction failed.") from exc