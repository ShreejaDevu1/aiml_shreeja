#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Assignment 1: Filtering Data Based on Conditions
#Tasks:
#Filter out all rows where the Transaction_Amount is greater than 2000.
#Find all rows where the Transaction_Type is "Loan Payment" and the Account_Balance is greater than 5000.
#Extract transactions made in the "Uptown" branch.
#Objective:
#Practice filtering data using conditions and boolean indexing.


# In[1]:


import pandas as pd

# Load the data from CSV
file_name = "Day_10_banking_data (1).csv"
df = pd.read_csv(file_name)

# 1. Filter rows where Transaction_Amount > 2000
high_transaction_amount = df[df["Transaction_Amount"] > 2000]

# 2. Find rows where Transaction_Type is "Loan Payment" and Account_Balance > 5000
loan_payment_high_balance = df[(df["Transaction_Type"] == "Loan Payment") & (df["Account_Balance"] > 5000)]

# 3. Extract transactions made in the "Uptown" branch
uptown_transactions = df[df["Branch"] == "Uptown"]

# Save results to new CSV files
high_transaction_amount.to_csv("Filtered_High_Transaction_Amount.csv", index=False)
loan_payment_high_balance.to_csv("Filtered_Loan_Payment_High_Balance.csv", index=False)
uptown_transactions.to_csv("Filtered_Uptown_Transactions.csv", index=False)

# Display results
print("1. Transactions with Transaction_Amount > 2000 saved to 'Filtered_High_Transaction_Amount.csv'")
print("2. Loan Payments with Account_Balance > 5000 saved to 'Filtered_Loan_Payment_High_Balance.csv'")
print("3. Transactions in the 'Uptown' branch saved to 'Filtered_Uptown_Transactions.csv'")


# In[ ]:


#Assignment 2: Data Transformation
#Tasks:
#Add a new column called Transaction_Fee, calculated as 2% of Transaction_Amount.
#Create a new column Balance_Status:
#If Account_Balance is greater than 5000, label it as "High Balance".
#Otherwise, label it as "Low Balance".
#Objective:
#Learn how to create new columns and apply transformations based on existing data.


# In[5]:


import pandas as pd
file_name = "Day_10_banking_data (1).csv"
df = pd.read_csv(file_name)
df["Transaction_Fee"] = df["Transaction_Amount"] * 0.02
df["Balance_Status"] = df["Account_Balance"].apply(lambda x: "High Balance" if x > 5000 else "Low Balance")
output_file_name = "Transformed_Banking_Data.csv"
df.to_csv(output_file_name, index=False)
print(f"Transformed data saved to '{output_file_name}'")
print(df.head())


# In[ ]:




