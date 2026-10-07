# Customer Churn Intelligence Platform

A machine learning-powered customer churn prediction system that predicts the probability of customer churn and classifies customers into risk levels.

The project combines a trained Logistic Regression model with a preprocessing pipeline and exposes the model through a FastAPI REST API. The API is validated using automated tests and can be deployed using Docker.

## Features

- Customer churn prediction using Machine Learning
- Probability-based churn prediction
- Custom decision threshold of 0.35 to prioritise churn recall
- High/Low customer risk classification
- Input validation using Pydantic
- FastAPI REST API
- Interactive Swagger API documentation
- Health check endpoint
- Centralised prediction error handling
- Automated API tests using Pytest
- Dockerised deployment


## Machine Learning

The project uses the Telco Customer Churn dataset to predict whether a customer is likely to churn.

### Data Preprocessing

The preprocessing pipeline includes:

- Numerical feature imputation using the median
- Numerical feature standardisation using `StandardScaler`
- Categorical feature imputation using the most frequent value
- Categorical feature encoding using `OneHotEncoder`
- Stratified train-test split

The preprocessing pipeline is saved as `preprocessor.pkl` and reused during API inference to ensure the same transformations are applied to new customer data.

### Model Selection

Several classification models were evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

Stratified 5-fold cross-validation was used for model comparison based on ROC-AUC.

**Logistic Regression** achieved the best cross-validation ROC-AUC and was selected as the final model.

### Model Performance

| Model | Cross-Validation ROC-AUC |
|---|---:|
| Logistic Regression | 0.8583 |
| XGBoost | 0.8544 |
| Random Forest | 0.8449 |
| Decision Tree | 0.6664 |

The final Logistic Regression model achieved approximately **0.8478 ROC-AUC** on the holdout test set.

### Decision Threshold

The default classification threshold of 0.50 was changed to **0.35** after evaluating out-of-fold predictions.

The lower threshold improves the model's ability to identify customers who are likely to churn, which is useful when the business objective is to prioritise customer retention.

At a threshold of 0.35:

- Accuracy: **77.79%**
- Precision: **56.39%**
- Recall: **71.93%**
- F1-score: **63.22%**
- ROC-AUC: **84.78%**

## API

The application is built using FastAPI and provides three main endpoints.

### Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Confirms that the API is running |
| GET | `/health` | Checks API and ML model health |
| POST | `/predict` | Predicts customer churn probability and risk |

### Prediction Response

A successful prediction returns:

```json
{
  "prediction": 1,
  "churn_probability": 0.7989,
  "risk_level": "High",
  "message": "Customer is likely to churn."
}
