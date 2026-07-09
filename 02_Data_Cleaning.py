# ==========================================
# TASK 2: DATA CLEANING
# ==========================================
import pandas as pd
df_tele_customer = pd.read_csv('Telco_Customer_Churn_Dataset.csv')

# --- STEP A: STANDARDIZE THE HEADERS FIRST ---
# (We fix the columns here so the rest of our cleaning code can use the clean names!)
print("\n---Tasks 2: Data Cleaning ( Ensure the dataset is clean for analysis.)---")

# 1. Add underscores before capitals and chain lowercase
df_tele_customer.columns = df_tele_customer.columns.str.replace(r'(?<!^)(?=[A-Z])', '_', regex=True).str.lower()

# 2. Fix the double-underscore abbreviations
df_tele_customer.columns = df_tele_customer.columns.str.replace('i_d', 'id', regex=False).str.replace('t_v', 'tv', regex=False)
print(f"Cleaned Columns: {list(df_tele_customer.columns)}")     # Confirm job done

# --- STEP B: CLEAN THE ROWS & CELLS ---

# 3. Convert TotalCharges from string to float now using the new lowercase name
# total_charges dtype convert to numeric
df_tele_customer['total_charges'] = pd.to_numeric(df_tele_customer['total_charges'], errors='coerce')
# Confirm conversion
print(f"TotalCharges Column is now converted to: {df_tele_customer['total_charges'].dtype}")

# 4. Fill those 11 exposed missing values with 0
print(f"Number of hidden missing values exposed: {df_tele_customer['total_charges'].isna().sum()}")

# handling missing values
# Fill the new customer blanks with 0
df_tele_customer['total_charges'] = df_tele_customer['total_charges'].fillna(0)
df_tele_customer.to_csv("cleaned_customer_data.csv", index=False)
print("\n---------Task 2 Completed----------")
