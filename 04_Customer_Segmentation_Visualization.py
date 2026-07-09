
# ======================================================
# TASK 4: CUSTOMER SEGMENTATION VISUALIZATION
# ======================================================
import pandas as pd

df_tele_customer = pd.read_csv("cleaned_customer_data.csv")
print("\n--- Task 4: Customer Segmentation Visualization ---")
df_tele_customer['tenure_group'] = pd.cut(x=df_tele_customer['tenure'],
                                          bins=[-1, 12, 36, df_tele_customer['tenure'].max()],
                                          labels=['0 - 12 months', '13 - 36 months', '37+ months'])

import plotly.express as px

# 1. Initialize the interactive pie chart
fig_pie = px.pie(data_frame=df_tele_customer, hole=0.3,   # 👈 Cuts a beautiful 30% hole right in the center!
             names='tenure_group',
             title='Customer Distribution by Tenure Segments')
# 2. Open the interactive browser window
fig_pie.write_image("Customer_Distribution_Donut.png", scale=3)
fig_pie.show()

# Grouping the data summary table for effective plotting
avg_charges = df_tele_customer.groupby(['tenure_group', 'churn'])['monthly_charges'].mean().reset_index()
print(avg_charges)

# 1. Build the responsive chart structure with 1-decimal formatting
fig_bar = px.bar(data_frame=avg_charges, x='tenure_group', y='monthly_charges', text_auto='.1f',
             color='churn', barmode='group', title='Average Monthly Charges by Tenure and Churn Status')
# 2. Overwrite the trace settings to force the individual bars to be ultra-thin
# Update the layout margins to force the bars to become perfectly slim and elegant
# and add executive text note together

fig_bar.update_layout(bargap=0.35,   # 👈 Controls space between the groups
                      bargroupgap=0.15,  # 👈 Controls space between the side-by-side bars
                      annotations=[{'text' :"CRITICAL TREND: Across all tiers, Churn customers pay significantly higher monthly charges. High pricing is actively driving exit rates!",
                                    'xref':'paper', 'yref':'paper',
                                    'x':0.5, 'y':-0.18, # 👈 Tucked neatly right below the horizontal axis numbers
                                    'showarrow': False,
                                    'font': {'size': 12, 'color': 'red', 'family': 'Arial'}
                                   }]
                      )
fig_bar.write_image("Average_Monthly_Charges_by_Tenure_and_Churn.png", scale=3)
fig_bar.show()

# Save the processed data including tenure_group and segments
df_tele_customer.to_csv("tele_customer_processed.csv", index=False)