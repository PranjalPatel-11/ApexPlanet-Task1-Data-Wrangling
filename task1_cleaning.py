import pandas as pd
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
df = pd.read_excel(BASE_DIR / "data" / "original dataset.xlsx")

print("Dataset loaded successfully!")

df["Age"] = df["Age"].fillna(df["Age"].median())
df["City"] = df["City"].fillna(df["City"].mode()[0])

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

df["Month"] = df["Order_Date"].dt.month
df["Year"] = df["Order_Date"].dt.year
df["Month_Name"] = df["Order_Date"].dt.month_name()

# Check duplicate Order_ID occurrences
duplicate_order_ids = df["Order_ID"].duplicated().sum()
print("Duplicate Order_ID occurrences:", duplicate_order_ids)

# Detect Total_Sales outliers using IQR
Q1 = df["Total_Sales"].quantile(0.25)
Q3 = df["Total_Sales"].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["Total_Sales"] < lower_limit) |
    (df["Total_Sales"] > upper_limit)
]

print("Total_Sales outliers:", len(outliers))

print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())
print("Final shape:", df.shape)

OUTPUT_FILE = BASE_DIR / "output" / "cleaned_dataset.xlsx"

df.to_excel(OUTPUT_FILE, index=False)

print("Cleaned dataset saved successfully!")