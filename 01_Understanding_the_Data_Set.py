# ==========================================
# TASK 1: LOADING & DISCOVERY
# ==========================================
import pandas as pd

df_tele_customer = pd.read_csv('Telco_Customer_Churn_Dataset.csv')
# Basic Inspections (Checking structural flaws)
print("\n---------UNDERSTANDING/EXPLORING DATA---------")
print(df_tele_customer.head(10))                # Step 2 Display the first 10 rows
print(df_tele_customer.shape)
print(df_tele_customer.info())
print(df_tele_customer.duplicated().sum())      # Step 3 Checking for duplicate
print(df_tele_customer.isnull().sum())          # Step 4 Checking for Missing Values