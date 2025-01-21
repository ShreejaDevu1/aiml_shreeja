#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Data Filtering
#Extract all rows where sales are greater than 1000.
#Find all sales records for a specific region (e.g., "East").


# In[1]:


import pandas as pd
file_path = 'Day_8_sales_data.csv'  
sales_data = pd.read_csv(file_path)
sales_above_1000 = sales_data[sales_data['Sales'] > 1000]
print("Rows where sales are greater than 1000:")
print(sales_above_1000)
region = "East" 
sales_in_region = sales_data[sales_data['Region'] == region]
print(f"\nSales records for the '{region}' region:")
print(sales_in_region)


# In[ ]:


#Data Processing
#Add a new column, Profit_Per_Unit, calculated as Profit / Quantity.
#Create another column, High_Sales, which labels rows as Yes if Sales > 1000, else No.


# In[3]:


import pandas as pd
file_path = 'Day_8_sales_data.csv'  
sales_data = pd.read_csv(file_path)
sales_data['Profit_Per_Unit'] = sales_data['Profit'] / sales_data['Quantity']
print("Added column 'Profit_Per_Unit':")
print(sales_data.head())
sales_data['High_Sales'] = sales_data['Sales'].apply(lambda x: 'Yes' if x > 1000 else 'No')
print("\nAdded column 'High_Sales':")
print(sales_data.head())
output_file_path = 'Processed_Day_8_sales_data.csv'
sales_data.to_csv(output_file_path, index=False)
print(f"\nUpdated dataset saved to {output_file_path}")


# In[ ]:




