Machine Learning Models
Baseline Model
Logistic Regression
Handles imbalance using class_weight="balanced"
Advanced Model
XGBoost Classifier
Tuned hyperparameters
Handles nonlinear fraud patterns
 Evaluation Metrics

The following metrics are used:

AUC-PR (Primary metric for fraud detection)
F1 Score
Confusion Matrix
Precision@K (business-driven metric)
 Explainability (SHAP)

SHAP is used to interpret model predictions:

Global Interpretability
Feature importance ranking
Summary plots showing fraud drivers
Local Interpretability
Force plots for individual transactions
Waterfall plots for detailed explanations
Key Fraud Drivers (E-Commerce)
time_since_signup
purchase_value
country
hour_of_day
transaction velocity
 Model Comparison
Dataset	Model	AUC-PR	F1 Score
Fraud_Data	Logistic Regression	0.xx	0.xx
Fraud_Data	XGBoost	0.xx	0.xx
Credit Card	Logistic Regression	0.xx	0.xx
Credit Card	XGBoost	0.xx	0.xx
 Business Insights

The model identifies key fraud patterns:

New accounts with high-value transactions are high risk
Rapid transaction velocity indicates suspicious behavior
Unusual geographic location increases fraud probability
Early account activity (< 2 hours) is strongly correlated with fraud
Recommended Actions:
Require 2FA for high-risk transactions
Delay processing for suspicious activity
Manual review for high-risk scores
Device verification enforcement