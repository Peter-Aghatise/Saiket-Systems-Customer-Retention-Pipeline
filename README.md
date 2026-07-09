# Saiket Systems: Customer Churn & Retention Analytics Pipeline

A production-grade, end-to-end data engineering and business intelligence pipeline built using the structural framework from Saiket Systems to analyze, visualize, and mitigate customer churn.

## 📁 Repository Architecture
The pipeline is engineered into 5 chronological, independent execution scripts to enforce strict separation of concerns and data layer integrity:
* **01_Understanding_the_Data_Set.py**: Initiates structural baseline schema and missing value mapping.
* **02_Data_Cleaning.py**: Resolves whitespace string data traps and outputs a normalized CSV data layer.
* **03_Exploratory_Data_Analysis_EDA.py**: Builds a high-resolution 6-chart Matplotlib distribution matrix.
* **04_Customer_Segmentation_Visualization.py**: Configures interactive Plotly Express donut and clustered bar metrics.
* **05_Advanced_Analysis.py**: Executes demographic loops and computes the customer lifecycle maturity trend curve.

## 📁 Project Structure
* **data/**: Houses the finalized, pristine `cleaned_customer_data.csv` asset.
* **outputs/**: Contains all 5 high-resolution exported presentation plots (`.png` assets).

## 💡 Strategic Business Insights
1. **Operational Billing Friction**: Customers paying via **Electronic Check** experience a staggering **45.3% churn rate**, proving that manual monthly transactional friction actively drives customer drop-off.
2. **The Retention Maturity Curve**: Onboarding rookie accounts under 12 months sit in a critical **47.4% risk zone**. Churn risk drops exponentially to an elite **11.9%** once an account crosses the 3-year threshold.
3. **Contract Lock-in Power**: Volatile Month-to-month contracts leak **42.7%** of their customer base annually, whereas long-term 2-Year contract agreements permanently crush churn risk down to **2.8%**.

## 📊 Core Recommendations
* Shift financial budgets away from cold marketing and deploy targeted **New Customer Success Teams** to proactively support and nurture rookie accounts in their first 12 months.
* Incentivize Electronic Check accounts to transition onto **frictionless automated card pathways** via small bill discounts to cut operational churn risk by nearly two-thirds.
