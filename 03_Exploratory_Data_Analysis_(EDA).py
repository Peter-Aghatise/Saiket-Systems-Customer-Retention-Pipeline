# ==========================================
# TASK 3: EXPLORATORY DATA ANALYSIS(EDA)
# ==========================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_tele_customer = pd.read_csv("cleaned_customer_data.csv")
print("\n--- Task 3: Exploratory Data Analysis (EDA) ---")

# ----------------------------------------
# SUMMARY STATISTICS
# ----------------------------------------
# --- ITEM 2: GENERATE SUMMARY STATISTICS FOR ALL NUMERICAL COLUMNS ---(mean,median, mode).
num_mean = df_tele_customer[['tenure', 'monthly_charges', 'total_charges']].mean()
num_median = df_tele_customer[['tenure', 'monthly_charges', 'total_charges']].median()
num_mode = df_tele_customer[['tenure', 'monthly_charges', 'total_charges']].mode().iloc[0]

# Combine them into your clean executive summary grid matrix
summary_table = pd.DataFrame({'mean': num_mean,
                              'median': num_median,
                              'mode': num_mode})

print("\n--- ITEM 2: EXECUTIVE SUMMARY STATISTICS GRID --- ")
print(summary_table)

# --- ITEM 1: TRENDS AND DISTRIBUTIONS SUMMARY (Printed Insights) ---
print("\n=================================================================")
print("             BUSINESS INSIGHTS & DATA TREND REPORT              ")
print("=================================================================")
print("1. TENURE: The most common customer length is 1 month (Mode: 1.00),")
print("   showing high initial sign-ups but an early retention issue.")
print("\n2. MONTHLY CHARGES: The most popular price point is $20.05, but")
print("   the median ($70.35) reveals a strong shift to premium tiers.")
print("\n3. TOTAL CHARGES: The distribution is heavily skewed right, proving")
print("   that a small group of high-value loyal accounts pull up the average.")
print("=================================================================\n")

# --- ITEM 3: CREATE VISUALIZATIONS FOR NUMERICAL COLUMNS (MASTER SUBPLOT GRID) ---
# 3 Rows (Tenure, Monthly, Total) and 2 Columns (Histogram, Boxplot)
# ------------------------------------------
# ROW 0: TENURE COLUMN ANALYSIS
# ------------------------------------------

# Create Subplots visualizations for numerical columns so comparison is easily visualized
# Creation Grid layouts
fig, axes = plt.subplots(3, 2, figsize=(14, 18), constrained_layout=True)

# Plotting the visuals
sns.histplot(data=df_tele_customer, x='tenure', bins='fd', color='deeppink', kde=True, ax=axes[0, 0])
axes[0, 0].set_title('Tenure Range Distribution', fontsize=12, fontweight='bold')

# FOR BOXPLOT
sns.boxplot(data=df_tele_customer, y='tenure', color='deeppink', ax=axes[0, 1])
# 1. The Numbers must stay strictly sorted lowest-to-highest for Python's math engine!
axes[0, 1].set_yticks([1, 29, 32.4])
# 2. You pass a matching list of text names to perfectly describe those exact positions!
axes[0, 1].set_yticklabels(['1 (mode)', '29 (median)', '32.4 (mean)' ])
axes[0, 1].set_title('Tenure Range Summary for Box plot', fontsize=12, fontweight='bold')

# ------------------------------------------
# ROW 1: MONTHLY_CHARGES COLUMN ANALYSIS
# ------------------------------------------
sns.histplot(data=df_tele_customer, x='monthly_charges', bins='fd', color='blue', kde=True, ax=axes[1, 0])
axes[1, 0].set_title('Monthly Charges Distribution', fontsize=12, fontweight='bold')

# FOR BOXPLOT
sns.boxplot(data=df_tele_customer, y='monthly_charges', color='blue', ax=axes[1, 1])
axes[1, 1].set_yticks([20.1, 64.8, 70.4])
axes[1, 1].set_yticklabels(['20.1 (mode)', '64.8 (mean)', '70.4 (median)'])
axes[1, 1].set_title('Monthly Charges Distribution', fontsize=12, fontweight='bold')

# ------------------------------------------
# ROW 2: TOTAL_CHARGES COLUMN ANALYSIS
# ------------------------------------------
sns.histplot(data=df_tele_customer, x='total_charges', bins='fd', color='navy', kde=True, ax=axes[2, 0])
axes[2, 0].set_title('Total Charges Distribution', fontsize=12, fontweight='bold')

# FOR THE BOXPLOT
sns.boxplot(data=df_tele_customer, y='total_charges', color='navy', ax=axes[2, 1])
axes[2, 1].set_yticks([0, 1394.6, 2279.7])
axes[2, 1].set_yticklabels(['0 (mode)', '1394.6 (median)', '2279.7 (mean)'])
axes[2, 1].set_title('Total Charges Distribution', fontsize=12, fontweight='bold')

# SAVE AND DISPLAY MASTER GRID DASHBOARD (Called once after all rows are drawn!)
plt.savefig('Numerical_Analysis_Dashboard.png', dpi=300)
plt.show(block=True)

# --- ITEM 4: ANALYZE CHURN RATES (CHURN VS NON-CHURN PROPORTIONS) ---
# 1. Calculate the split of Churn vs Non-Churn
churn_value = df_tele_customer['churn'].value_counts()

# 2. Build the Pie Chart visualization
plt.figure(figsize=(5, 5))
plt.pie(churn_value.values,          # 1. Give it the numeric slices first
        labels= churn_value.index,   # 2. Give it the category names for labels
        autopct='%1.1f%%',          # 3. This just tells it to calculate percentages automatically
        startangle=90,              # 4. Rotates the pie so it looks neat
        colors=['green', 'red']     # 5. Assigns colors to your slices
        )
plt.legend(churn_value.index, loc='upper left', frameon=False)
plt.title('Churn Proportion Rate: Churn vs Non-Churn', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('Churn_Proportion_Rate.png', dpi=300)
plt.show(block=True)

print("\n--------- Task 3 Completed Successfully ----------")