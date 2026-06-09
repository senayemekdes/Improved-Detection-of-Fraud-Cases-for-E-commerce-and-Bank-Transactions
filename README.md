Fraud Detection System (E-Commerce & Credit Card)
 Overview

This project builds a machine learning system to detect fraudulent transactions using two datasets:

E-commerce transactions (Fraud_Data.csv)
Credit card transactions (creditcard.csv)

It includes preprocessing, modeling, evaluation, and explainable AI (SHAP).

📂 Project Structure
Fraud-Detection/
│
├── data/
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_modeling.ipynb
│   ├── 04_shap_explainability.ipynb
│   └── 05_creditcard_modeling.ipynb
│
├── src/
├── config/
├── reports/
└── requirements.txt
 Pipeline
Data preprocessing
Feature engineering (e-commerce only)
Model training (Logistic Regression, XGBoost)
Evaluation (AUC-PR, F1, Precision@K)
Explainability (SHAP)
 Models
Logistic Regression (baseline)
XGBoost (final model)
 Evaluation Metrics
AUC-PR (primary)
F1 Score
Confusion Matrix
Precision@K
 Explainability (SHAP)
Global feature importance (summary plot)
Local prediction explanation (force/waterfall plots)

Key fraud drivers:

time_since_signup
purchase_value
country
transaction velocity
 Key Insights
New accounts with high-value transactions are high risk
Rapid transactions indicate fraud behavior
Unusual location increases fraud probability
 How to Run
pip install -r requirements.txt
python src/train.py
python src/evaluate.py
python src/explain.py
Notes
Two datasets are modeled separately
SHAP used for model interpretability
Focus on imbalanced classification handling