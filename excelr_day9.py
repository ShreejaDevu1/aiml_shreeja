#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Assignment 1: Data Exploration
#Tasks:
#Load the banking_data.csv file using Pandas.
#Display the first 5 rows of the dataset.
#Use .describe() to generate basic statistics of the numerical columns (e.g., Transaction_Amount, Account_Balance).
#Check for missing values in the dataset.
#Objective:
#Understand how to load and inspect the dataset.
#Use basic descriptive statistics and data integrity checks.


# In[4]:


import pandas as pd
file_path = 'banking_data.csv' 
banking_data = pd.read_csv(file_path)
print("First 5 rows of the dataset:")
print(banking_data.head())
print("\nBasic statistics of numerical columns:")
print(banking_data.describe())
print("\nMissing values in the dataset:")
print(banking_data.isnull().sum())


# In[ ]:


#Assignment 2: Data Aggregation and Grouping
#Tasks:
#Group the data by Account_Type and calculate:
#The total sum of Transaction_Amount.
#The average Account_Balance for each account type.
#Group the data by Branch and calculate:
#The total number of transactions per branch.
#The average transaction amount per branch.
#Objective:
#Learn to use groupby() for aggregating data by categories.
#Gain skills in calculating grouped statistics.



# In[6]:


import pandas as pd
file_path = 'banking_data.csv' 
banking_data = pd.read_csv(file_path)
total_transaction_by_account_type = banking_data.groupby('Account_Type')['Transaction_Amount'].sum()
print("Total Transaction Amount by Account Type:")
print(total_transaction_by_account_type)
average_balance_by_account_type = banking_data.groupby('Account_Type')['Account_Balance'].mean()
print("\nAverage Account Balance by Account Type:")
print(average_balance_by_account_type)
total_transactions_by_branch = banking_data.groupby('Branch')['Transaction_Amount'].count()
print("\nTotal Number of Transactions by Branch:")
print(total_transactions_by_branch)
average_transaction_by_branch = banking_data.groupby('Branch')['Transaction_Amount'].mean()
print("\nAverage Transaction Amount by Branch:")
print(average_transaction_by_branch)


# In[ ]:




