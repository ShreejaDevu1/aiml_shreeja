#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Assignment 1: Data Visualization
#Tasks:
#Plot the total sum of Transaction_Amount per Account_Type using a bar plot.
#Create a pie chart to show the percentage of transactions per Branch.
#Objective:
#Understand how to visualize data using Pandas' built-in plotting capabilities (Matplotlib integration).



# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
file_name = "Day_12_banking_data.csv"
df = pd.read_csv(file_name)
account_type_totals = df.groupby("Account_Type")["Transaction_Amount"].sum()
plt.figure(figsize=(8, 5))
account_type_totals.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Total Transaction Amount by Account Type")
plt.xlabel("Account Type")
plt.ylabel("Total Transaction Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Barplot_Transaction_Amount_Account_Type.png")  
plt.show()
branch_transaction_counts = df["Branch"].value_counts()
plt.figure(figsize=(6, 6))
branch_transaction_counts.plot(kind="pie", autopct="%1.1f%%", startangle=90, colormap="Pastel1")
plt.title("Percentage of Transactions per Branch")
plt.ylabel("")  
plt.tight_layout()
plt.savefig("Piechart_Transactions_Branch.png")  
plt.show()

