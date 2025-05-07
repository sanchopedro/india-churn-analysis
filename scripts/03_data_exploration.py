# %% Import necessary libraries
import pandas as pd

# Load the CSV file
df = pd.read_csv("../data/processed/prod_customer_data.csv")
df.head()

# %% Display the DataFrame shape
df.shape

# %% Display the DataFrame statistics
df.describe()

# %% Explore the data
# 1. Gender distribution
gender_stats = df["Gender"].value_counts(dropna=False).reset_index()
gender_stats.columns = ["Gender", "TotalCount"]
gender_stats["Percentage"] = gender_stats["TotalCount"] * 100.0 / len(df)

# 2. Contract type distribution
contract_stats = df["Contract"].value_counts(dropna=False).reset_index()
contract_stats.columns = ["Contract", "TotalCount"]
contract_stats["Percentage"] = contract_stats["TotalCount"] * 100.0 / len(df)

# 3. Total revenue by customer status
status_stats = (
    df.groupby("Customer_Status")
    .agg(TotalCount=("Customer_Status", "count"), TotalRev=("Total_Revenue", "sum"))
    .reset_index()
)
total_revenue = df["Total_Revenue"].sum()
status_stats["RevPercentage"] = status_stats["TotalRev"] * 100.0 / total_revenue

# 4. State distribution
state_stats = df["State"].value_counts(dropna=False).reset_index()
state_stats.columns = ["State", "TotalCount"]
state_stats["Percentage"] = state_stats["TotalCount"] * 100.0 / len(df)
state_stats = state_stats.sort_values(by="Percentage", ascending=False)

# Show the results
print("Gender Stats:\n", gender_stats, "\n" + "=" * 50 + "\n")
print("Contract Stats:\n", contract_stats, "\n" + "=" * 50 + "\n")
print("Customer Status Stats:\n", status_stats, "\n" + "=" * 50 + "\n")
print("State Stats:\n", state_stats, "\n" + "=" * 50 + "\n")

# %% Filter the DataFrame to include only churned and stayed customers
df_churn = df[
    (df["Customer_Status"] == "Churned") | (df["Customer_Status"] == "Stayed")
].reset_index(drop=True)
df_churn.head()

# %% Filter the DataFrame to include only new customers
df_new_customers = df[df["Customer_Status"] == "Joined"].reset_index(drop=True)
df_new_customers.head()

# %% Export the DataFrames to CSV files
df_churn.to_csv("../data/output/prod_customer_data_churn.csv", index=False)
df_new_customers.to_csv(
    "../data/output/prod_customer_data_new_customers.csv", index=False
)
