# %% import necessary libraries
import pandas as pd

# Load the CSV file
csv_file_path = "../data/raw/Customer_Data.csv"
df = pd.read_csv(csv_file_path)

# Display the first few rows of the DataFrame
df.head()

# %% Display the DataFrame information

df.info()

# %% Display the DataFrame statistics
df.describe()

# %% Check for missing values in the DataFrame
df.isna().sum()
# %% Check for duplicate rows in the DataFrame
for column in df.columns:
    print(f"Coluna: {column}")
    print(df[column].value_counts(dropna=False))  
    print("\n" + "="*50 + "\n")

# %% Create a dictionary to map the values to their corresponding

# Use o método .loc para cada coluna problemática
# df.loc[df['Value_Deal'].isna(), 'Value_Deal'] = "Not Available"
# df.loc[df['Internet_Type'].isna(), 'Internet_Type'] = "Not Available"

fill_values = {

    "Value_Deal": "Not Available",
    "Multiple_Lines": "No",
    "Internet_Type": "Not Available",
    "Online_Security": "No",
    "Online_Backup": "No",
    "Device_Protection_Plan": "No",
    "Premium_Support": "No",
    "Streaming_TV": "No",
    "Streaming_Movies": "No",
    "Streaming_Music": "No",
    "Unlimited_Data": "No",
    "Churn_Category": "Other",
    "Churn_Reason": "Others"
}

# Fill missing values in the DataFrame with the specified values
df.fillna(fill_values, inplace=True)

# %% Check for missing values in the DataFrame
df.isna().sum()

# %% Remove negative values from the Monthly_Charge column
df = df[df['Monthly_Charge'] >= 0]

# %% Export the DataFrame to a CSV file
df.to_csv("../data/output/prod_customer_data.csv", index=False)
