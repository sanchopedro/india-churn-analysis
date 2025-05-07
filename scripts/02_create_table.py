# Import necessary libraries
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float, text
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, declarative_base
import pyodbc
from dotenv import load_dotenv
import os

# load the environment variables from the .env file
load_dotenv()

# Database connection parameters
server = "localhost"
database = "db_Churn"
username = "sa"
password = os.getenv("SA_PASSWORD")
driver = "ODBC Driver 17 for SQL Server"

# Create the connection URL
connection_url = URL.create(
    "mssql+pyodbc",
    username=username,
    password=password,
    host=server,
    database=database,
    query={"driver": driver, "TrustServerCertificate": "yes"},
)
db = create_engine(connection_url)
Session = sessionmaker(bind=db)
session = Session()

# Test the connection to the database
try:
    with db.connect() as conn:
        print("Database connection established successfully.")
except Exception as e:
    print(f"Error connecting to the database: {e}")
    exit()

# Check if the database exists, and create it if it doesn't
try:
    with db.connect() as conn:
        conn.execute(text(f"IF DB_ID('{database}') IS NULL CREATE DATABASE {database}"))
        print(f"Database '{database}' verified/created successfully.")
except Exception as e:
    print(f"Error creating/verifying the database: {e}")
    exit()

# Define the base class for declarative models
Base = declarative_base()


# Define the Customer model
class Customer(Base):
    __tablename__ = "Customer"
    Customer_ID = Column("Customer_ID", String(50), primary_key=True)
    Gender = Column("Gender", String(10), nullable=True)
    Age = Column("Age", Integer, nullable=True)
    Married = Column("Married", String(10), nullable=True)
    State = Column("State", String(50), nullable=True)
    Number_of_Referrals = Column("Number_of_Referrals", Integer, nullable=True)
    Tenure_in_Months = Column("Tenure_in_Months", Integer, nullable=True)
    Value_Deal = Column("Value_Deal", String(50), nullable=True)
    Phone_Service = Column("Phone_Service", String(10), nullable=True)
    Multiple_Lines = Column("Multiple_Lines", String(50), nullable=True)
    Internet_Service = Column("Internet_Service", String(50), nullable=True)
    Internet_Type = Column("Internet_Type", String(50), nullable=True)
    Online_Security = Column("Online_Security", String(50), nullable=True)
    Online_Backup = Column("Online_Backup", String(50), nullable=True)
    Device_Protection_Plan = Column("Device_Protection_Plan", String(50), nullable=True)
    Premium_Support = Column("Premium_Support", String(50), nullable=True)
    Streaming_TV = Column("Streaming_TV", String(50), nullable=True)
    Streaming_Movies = Column("Streaming_Movies", String(50), nullable=True)
    Streaming_Music = Column("Streaming_Music", String(50), nullable=True)
    Unlimited_Data = Column("Unlimited_Data", String(50), nullable=True)
    Contract = Column("Contract", String(50), nullable=True)
    Paperless_Billing = Column("Paperless_Billing", String(10), nullable=True)
    Payment_Method = Column("Payment_Method", String(50), nullable=True)
    Monthly_Charge = Column("Monthly_Charge", Float, nullable=True)
    Total_Charges = Column("Total_Charges", Float, nullable=True)
    Total_Refunds = Column("Total_Refunds", Float, nullable=True)
    Total_Extra_Data_Charges = Column(
        "Total_Extra_Data_Charges", Integer, nullable=True
    )
    Total_Long_Distance_Charges = Column(
        "Total_Long_Distance_Charges", Float, nullable=True
    )
    Total_Revenue = Column("Total_Revenue", Float, nullable=True)
    Customer_Status = Column("Customer_Status", String(20), nullable=True)
    Churn_Category = Column("Churn_Category", String(50), nullable=True)
    Churn_Reason = Column("Churn_Reason", String(100), nullable=True)

    def __init__(self, Customer):
        self.Customer_ID = Customer["Customer_ID"]
        self.Gender = Customer["Gender"]
        self.Age = Customer["Age"]
        self.Married = Customer["Married"]
        self.State = Customer["State"]
        self.Number_of_Referrals = Customer["Number_of_Referrals"]
        self.Tenure_in_Months = Customer["Tenure_in_Months"]
        self.Value_Deal = Customer["Value_Deal"]
        self.Phone_Service = Customer["Phone_Service"]
        self.Multiple_Lines = Customer["Multiple_Lines"]
        self.Internet_Service = Customer["Internet_Service"]
        self.Internet_Type = Customer["Internet_Type"]
        self.Online_Security = Customer["Online_Security"]
        self.Online_Backup = Customer["Online_Backup"]
        self.Device_Protection_Plan = Customer["Device_Protection_Plan"]
        self.Premium_Support = Customer["Premium_Support"]
        self.Streaming_TV = Customer["Streaming_TV"]
        self.Streaming_Movies = Customer["Streaming_Movies"]
        self.Streaming_Music = Customer["Streaming_Music"]
        self.Unlimited_Data = Customer["Unlimited_Data"]
        self.Contract = Customer["Contract"]
        self.Paperless_Billing = Customer["Paperless_Billing"]
        self.Payment_Method = Customer["Payment_Method"]
        self.Monthly_Charge = Customer["Monthly_Charge"]
        self.Total_Charges = Customer["Total_Charges"]
        self.Total_Refunds = Customer["Total_Refunds"]
        self.Total_Extra_Data_Charges = Customer["Total_Extra_Data_Charges"]
        self.Total_Long_Distance_Charges = Customer["Total_Long_Distance_Charges"]
        self.Total_Revenue = Customer["Total_Revenue"]
        self.Customer_Status = Customer["Customer_Status"]
        self.Churn_Category = Customer["Churn_Category"]
        self.Churn_Reason = Customer["Churn_Reason"]


# Create the table in the database
Base.metadata.create_all(db)

# Load the CSV file
csv_file_path = "../data/output/prod_customer_data.csv"
data = pd.read_csv(csv_file_path)

# Check if the table already exists and if it has data
existing_data_count = session.query(Customer).count()

if existing_data_count > 0:
    print(f"Data already inserted. Total existing records: {existing_data_count}")
else:
    # Insert data into the database
    print("Inserting data into the database...")
    for _, row in data.iterrows():
        customer = Customer(row)
        session.add(customer)

    # Confirmar a transação
    session.commit()
    print("Data successfully inserted into the database.")

