# Features and target
import pandas as pd


fraud_data = pd.read_csv(r"C:\Users\PC\fraud-detection\data\processed/cleaned_fraud_data.csv")
X = fraud_data.drop('class', axis=1)
y = fraud_data['class']

print(X.shape)
print(y.value_counts())