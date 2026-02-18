import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")

df.columns = df.columns.str.lower().str.replace(" ", "_")

df['totalcharges'] = pd.to_numeric(df['totalcharges'], errors='coerce')
df = df.dropna(subset=['totalcharges'])

df['churn_flag'] = df['churn'].map({'Yes': 1, 'No': 0})
df['monthly_revenue'] = df['monthlycharges']

df['tenure_bucket'] = pd.cut(
    df['tenure'],
    bins=[0, 6, 12, 24, 48, 72],
    labels=['0-6 months', '6-12 months', '1-2 years', '2-4 years', '4-6 years']
)

df['tenure_years'] = df['tenure'] / 12

# SAFE cohort creation
df['signup_date'] = pd.to_datetime('2016-01-01') + pd.to_timedelta(df['tenure'] * 30, unit='D')
df['cohort_month'] = df['signup_date'].dt.to_period('M').astype(str)

df.to_csv("cleaned_churn_data.csv", index=False)

print("✅ Data cleaning completed successfully")
