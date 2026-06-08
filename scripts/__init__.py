import pandas as pd
import numpy as np
import os

def clean_fraud_data(df):
    print("Missing values:\n", df.isnull().sum())

    # Drop only critical missing values
    df = df.dropna(subset=['signup_time', 'purchase_time', 'ip_address'])

    # Remove duplicates
    df = df.drop_duplicates()

    # Convert datetime
    df['signup_time'] = pd.to_datetime(df['signup_time'])
    df['purchase_time'] = pd.to_datetime(df['purchase_time'])

    # Safer numeric conversion
    df['ip_address'] = pd.to_numeric(df['ip_address'], errors='coerce')

    return df


def clean_credit_data(df):
    return df.drop_duplicates()


# -----------------------------
# LOAD DATA
# -----------------------------
fraud_df = pd.read_csv(r"C:\Users\PC\fraud-detection\data\raw\Fraud_Data.csv")

# -----------------------------
# CLEAN DATA
# -----------------------------
cleaned_fraud_df = clean_fraud_data(fraud_df)

# -----------------------------
# SAVE DATA
# -----------------------------
os.makedirs("../data/processed", exist_ok=True)

output_path = "data/processed/cleaned_fraud_data.csv"
cleaned_fraud_df.to_csv(output_path, index=False)

print("Data cleaned and saved successfully.")
print("Final shape:", cleaned_fraud_df.shape)



ip_df =  pd.read_csv(r"C:\Users\PC\fraud-detection\data\raw\IpAddress_to_Country.csv")
def ip_to_country(ip_df, fraud_df):

    fraud_df['ip_address'] = pd.to_numeric(fraud_df['ip_address'], errors='coerce')

    def get_country(ip):
        match = ip_df[
            (ip_df['lower_bound_ip_address'] <= ip) &
            (ip_df['upper_bound_ip_address'] >= ip)
        ]
        return match['country'].values[0] if not match.empty else 'Unknown'

    fraud_df['country'] = fraud_df['ip_address'].apply(get_country)

    return fraud_df
# Step 2: map IP → country
fraud_df = ip_to_country(ip_df, fraud_df)

# Step 3: NOW country exists
print(fraud_df['country'].value_counts().head())

# Step 4: fraud rate analysis
print(
    fraud_df.groupby('country')['class']
    .mean()
    .sort_values(ascending=False)
)

def engineer_features(df):
    # Temporal
    df['time_since_signup'] = (df['purchase_time'] - df['signup_time']).dt.total_seconds() / 3600  # hours
    df['hour_of_day'] = df['purchase_time'].dt.hour
    df['day_of_week'] = df['purchase_time'].dt.dayofweek
    
    # Velocity (per user)
    df = df.sort_values(['user_id', 'purchase_time'])
    df['tx_velocity_1h'] = df.groupby('user_id')['purchase_time'].diff().dt.total_seconds() / 3600
    # More: rolling counts, etc.
    
    return df