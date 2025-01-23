#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Assignment 1: Sorting and Ranking Data
#Sort the dataset by Account_Balance in descending order and display the first 10 rows.
#Create a ranking column for Transaction_Amount within each Branch:
#Use rank() to give ranks for transactions based on their amounts within each branch.
#Objective:
#Learn how to sort data and apply ranking based on certain columns.


# In[1]:


import pandas as pd
file_name = "Day_11_banking_data.csv"
df = pd.read_csv(file_name)
sorted_by_balance = df.sort_values(by="Account_Balance", ascending=False).head(10)
df["Transaction_Rank"] = df.groupby("Branch")["Transaction_Amount"].rank(method="dense", ascending=False)
output_file_name = "Sorted_Ranked_Banking_Data.csv"
df.to_csv(output_file_name, index=False)
print("1. Top 10 rows sorted by Account_Balance (descending):")
print(sorted_by_balance)
print("\n2. Added Transaction_Rank column to the dataset.")
print(df.head())


# In[ ]:




