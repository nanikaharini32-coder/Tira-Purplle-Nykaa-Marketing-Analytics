import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
RAW = BASE / "data/raw/Tira_Purplle_Nykaa_Marketing_Campaign_Analytics_166665_raw.csv"
OUT = BASE / "data/cleaned/Tira_Purplle_Nykaa_Marketing_Campaign_Analytics_166665_cleaned.csv"

df = pd.read_csv(RAW)
clean = df.copy()

# 1. Trim whitespace from text fields
for col in clean.select_dtypes(include=["object"]).columns:
    clean[col] = clean[col].astype("string").str.strip()

# 2. Convert numeric columns to numeric types
integer_cols = ["Duration", "Impressions", "Clicks", "Leads", "Conversions", "Revenue"]
decimal_cols = ["Acquisition_Cost", "ROI", "Engagement_Score"]

for col in integer_cols:
    clean[col] = pd.to_numeric(clean[col], errors="raise").astype("int64")

for col in decimal_cols:
    clean[col] = pd.to_numeric(clean[col], errors="raise").astype("float64")

# 3. Parse dates as dates
clean["Date"] = pd.to_datetime(clean["Date"], errors="raise")

# 4. Validate that all rows and columns remain
assert len(clean) == len(df), "Row count changed during cleaning!"
assert clean.shape[1] == df.shape[1], "Column count changed during cleaning!"

OUT.parent.mkdir(parents=True, exist_ok=True)
clean.to_csv(OUT, index=False, date_format="%Y-%m-%d")

print("Raw shape:", df.shape)
print("Cleaned shape:", clean.shape)
print("Rows removed:", len(df) - len(clean))
print("Missing values in raw:", int(df.isna().sum().sum()))
print("Duplicate rows in raw:", int(df.duplicated().sum()))
print("Saved cleaned file to:", OUT)
