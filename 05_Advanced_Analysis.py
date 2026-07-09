
# ======================================================
# TASK 5: ADVANCE ANALYSIS
# ======================================================
import pandas as pd

df_tele_customer = pd.read_csv("tele_customer_processed.csv")
pd.set_option('display.max_columns', None) #THIS FORCES PANDAS TO DISPLAY ALL SECTIONS
print("\n--- Task 5: Advanced Analysis ---")
# Mapping the churn to numbers
df_tele_customer['churn_numeric'] = df_tele_customer['churn'].map({'Yes':1, 'No':0})
print(df_tele_customer[['churn', 'churn_numeric']].head())

# grouping customers by tenure to compute statistics for charges and churn.
print("\n------Advanced Statistics Computation------")
advanced_stats = df_tele_customer.groupby('tenure_group').agg({
    'monthly_charges': ['mean', 'median', 'sum'],
    'total_charges': ['mean', 'median', 'sum'],
    'churn_numeric': ['mean']
}).reset_index()
print(advanced_stats)

# Create a list of the exact demographic and operational columns
features = ['gender', 'senior_citizen', 'payment_method', 'contract']
print("\n--- ITEM 2: DEMOGRAPHIC & OPERATIONAL CHURN RATES ---")
# Run a simple loop to cycle through them one by one
for columns in features:
    print(f"\n📈 Churn Rates by {columns.upper()}: ")
# Group by the current feature, isolate churn_numeric, and calculate the mean percentage!
    churn_analysis = df_tele_customer.groupby(columns)['churn_numeric'].mean().reset_index()
    print(churn_analysis)

# --- ADVANCED BUSINESS INSIGHT REPORT ---
print("\n=================================================================")
print("            SAIKET SYSTEMS: ADVANCED CHURN DIAGNOSTICS          ")
print("=================================================================")
print("1. OPERATIONAL DANGER: Electronic Check payment methods represent the")
print("   single largest operational risk with a massive 45.3% churn rate.")
print("   Frictionless automatic payments cut this risk by nearly two-thirds.")
print("\n2. AGE DISPARITY: Senior Citizens are highly volatile, showing a 41.7%")
print("   churn rate compared to only 23.6% for younger account holders.")
print("\n3. CONTRACT POWER: Volatile Month-to-month contracts leak 42.7% of")
print("   their customer base annually, whereas long-term 2-Year contract")
print("   lock-ins permanently crush churn risk down to an elite 2.8%.")
print("=================================================================\n")

# PLOTTING THE LINE CHART USING YOUR ORIGINAL DATA STRUCTURE
import plotly.express as px
# 1. Take a clean, flat copy of just the two columns we need for this specific line graph
plot_data = pd.DataFrame({
    'lifecycle_stage': advanced_stats[('tenure_group', '')],
    'churn_rate': advanced_stats[('churn_numeric', 'mean')]
# 2. Feed this perfectly flat, single-storey table straight into Plotly Express!
})
fig_lifecycle = px.line(data_frame=plot_data,
                        x='lifecycle_stage',    # 👈 Pure single strings with zero tuple confusion!
                        y='churn_rate',         # 👈 Pure single strings with zero tuple confusion!
                        markers=True,
                        # 1. Tells Plotly to extract text numbers from our exact churn rate column!
                        text='churn_rate',      # 👈 Maps perfectly with a length of 3!
                        labels={'lifecycle_stage': 'Customer Lifecycle Stage',
                                'churn_rate': 'Churn Rate Percentage'},
                        title= 'Customer Churn Rate Lifecycle Journey Trend')
# 3. Overwrites the display skin to format the numbers to 1-decimal percentages!
fig_lifecycle.update_traces(
    texttemplate='%{text:.1%}',     # 👈 Beautifully prints 42.7%, 11.3%, 2.8% on top of dots!
    textposition='top center'      # 👈 Safely floats the number right above the geometric dot!
)
fig_lifecycle.write_image("Customer_Lifecycle_Journey_Trend.png", scale=3)
fig_lifecycle.show()