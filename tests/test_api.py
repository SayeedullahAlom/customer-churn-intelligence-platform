from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


high_risk_customer = {
    "Country": "United States",
    "State": "California",
    "Latitude": 33.0,
    "Longitude": -117.0,
    "Gender": "Male",
    "Senior_Citizen": "No",
    "Partner": "No",
    "Dependents": "No",
    "Tenure_Months": 2,
    "Phone_Service": "Yes",
    "Multiple_Lines": "No",
    "Internet_Service": "Fiber optic",
    "Online_Security": "No",
    "Online_Backup": "No",
    "Device_Protection": "No",
    "Tech_Support": "No",
    "Streaming_TV": "Yes",
    "Streaming_Movies": "Yes",
    "Contract": "Month-to-month",
    "Paperless_Billing": "Yes",
    "Payment_Method": "Electronic check",
    "Monthly_Charges": 85.0,
    "Total_Charges": 170.0
}


low_risk_customer = {
    "Country": "United States",
    "State": "California",
    "Latitude": 34.05,
    "Longitude": -118.24,
    "Gender": "Female",
    "Senior_Citizen": "No",
    "Partner": "Yes",
    "Dependents": "Yes",
    "Tenure_Months": 60,
    "Phone_Service": "Yes",
    "Multiple_Lines": "No",
    "Internet_Service": "DSL",
    "Online_Security": "Yes",
    "Online_Backup": "Yes",
    "Device_Protection": "Yes",
    "Tech_Support": "Yes",
    "Streaming_TV": "No",
    "Streaming_Movies": "No",
    "Contract": "Two year",
    "Paperless_Billing": "No",
    "Payment_Method": "Bank transfer (automatic)",
    "Monthly_Charges": 55.0,
    "Total_Charges": 3300.0
}


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Customer Churn API is running"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"
    assert data["model_loaded"] is True
    assert data["preprocessor_loaded"] is True
    assert data["churn_threshold"] == 0.35


def test_high_risk_prediction():
    response = client.post("/predict", json=high_risk_customer)

    assert response.status_code == 200

    data = response.json()

    assert data["prediction"] == 1
    assert data["risk_level"] == "High"
    assert data["message"] == "Customer is likely to churn."
    assert 0 <= data["churn_probability"] <= 1


def test_low_risk_prediction():
    response = client.post("/predict", json=low_risk_customer)

    assert response.status_code == 200

    data = response.json()

    assert data["prediction"] == 0
    assert data["risk_level"] == "Low"
    assert data["message"] == "Customer is unlikely to churn."
    assert 0 <= data["churn_probability"] <= 1


def test_invalid_gender():
    invalid_customer = high_risk_customer.copy()
    invalid_customer["Gender"] = "Femalee"

    response = client.post("/predict", json=invalid_customer)

    assert response.status_code == 422