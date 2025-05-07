# %% import necessary libraries
import pandas as pd

# Load the CSV file
csv_file_path = "../data/processed/prod_customer_data.csv"
df = pd.read_csv(csv_file_path)

# Display the first few rows of the DataFrame
df.head()

# %% Display the DataFrame statistics
df.describe()
# %% Create a new column 'Monthly_Charge_Range' based on the 'Monthly_Charge' column
# Define the bins and labels for the Monthly_Charge ranges
# Monthly_Charge ranges: 0-30, 31-60, 61-90, 91-120
monthly_bins = [0, 30, 60, 90, 120]
monthly_labels = ["Low (0–30)", "Medium (31–60)", "High (61–90)", "Very High (91–120)"]
df["Monthly_Charge_Range"] = pd.cut(
    df["Monthly_Charge"], bins=monthly_bins, labels=monthly_labels
)

# %% Create a new column 'Age_Range' based on the 'Age' column
# Define the bins and labels for the Age ranges
# Age ranges: 18-25, 26-40, 41-60, 61+
age_bins = [0, 25, 40, 60, 100]
age_labels = ["18–25", "26–40", "41–60", "61+"]
df["Age_Range"] = pd.cut(df["Age"], bins=age_bins, labels=age_labels)

# %% Create a new column 'Tenure_Range' based on the 'Tenure' column
# Define the bins and labels for the Tenure ranges
# Tenure ranges: 0-6 months, 7-12 months, 13-24 months, 25-36 months

tenure_bins = [0, 6, 12, 24, 36]
tenure_labels = ["0–6 months", "7–12 months", "13–24 months", "25–36 months"]
df["Tenure_Range"] = pd.cut(
    df["Tenure_in_Months"], bins=tenure_bins, labels=tenure_labels
)
# %%
df.head()
# %% Export the DataFrames to CSV file
df.to_csv("../data/output/data_churn_pbi.csv", index=False)