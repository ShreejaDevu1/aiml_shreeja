#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Load and Explore the Data
#Load the sales_data.csv file using Pandas.
#Display the first 5 rows of the dataset.
#Print basic statistics (mean, median, min, max, etc.) of the numerical columns using .describe().
import pandas as pd
file_path = 'Day_7_sales_data.csv'  
sales_data = pd.read_csv(file_path)
print("First 5 rows of the dataset:")
print(sales_data.head())
print("\nBasic statistics of numerical columns:")
print(sales_data.describe())



# In[ ]:


#Data Analysis
#Calculate the total sales for each region.
#Find the most sold product (based on quantity).
#Compute the average profit margin for each product. (Profit margin = Profit / Sales * 100)


# In[5]:


import pandas as pd
file_path = 'Day_7_sales_data.csv'
sales_data = pd.read_csv(file_path)
total_sales_by_region = sales_data.groupby('Region')['Sales'].sum()
print("Total sales for each region:")
print(total_sales_by_region)
most_sold_product = sales_data.groupby('Product')['Quantity'].sum().idxmax()
print("\nMost sold product (based on quantity):")
print(most_sold_product)
sales_data['Profit Margin'] = (sales_data['Profit'] / sales_data['Sales']) * 100
average_profit_margin_by_product = sales_data.groupby('Product')['Profit Margin'].mean()
print("\nAverage profit margin for each product:")
print(average_profit_margin_by_product)


# In[ ]:




