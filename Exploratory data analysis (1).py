#!/usr/bin/env python
# coding: utf-8

# In[1]:


#load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv("data_clean.csv")
data


# In[3]:


data.info()


# In[4]:


print(type(data))
print(data.shape)


# In[5]:


data.dtypes


# In[6]:


data1 = data.drop(['Unnamed: 0',"Temp C"], axis =1)
data1


# In[7]:


#convert the Month column data to integer data type
data1['Month']=pd.to_numeric(data['Month'],errors='coerce')
data1.info


# In[8]:


#checking for duplicate rows in the table 
#print duplicated rows
data1[data1.duplicated()]


# In[9]:


#print all duplicated rows
data1[data1.duplicated(keep=False)]


# In[19]:


#change column names(Rename the columns)
data1.rename({'Solar.R':'Solar'},axis=1,inplace = True)
data1


# In[21]:


#change column names(Rename the columns)
data1.rename({'Solar.R':'Solar','Temp':'Temperature'},axis=1,inplace = True)
data1


# In[23]:


#display total missing values count in each columns using isnull().sum()
data1.isnull().sum()


# In[25]:


#visualize data1 missing values using graph
cols = data1.columns
colours=['black','yellow']
sns.heatmap(data1[cols].isnull(),cmap=sns.color_palette(colours),cbar=True)


# In[27]:


#find the mean and median values of each numeric column
#Imputation of missing value with median
median_ozone =  data1["Ozone"].median()
mean_ozone = data1["Ozone"].mean()
print("Medium of Ozone: ",median_ozone)
print("Mean of Ozone: ",mean_ozone)


# In[31]:


#Replace the ozone missing values with median value
data1['Ozone'] = data1['Ozone'].fillna(median_ozone)
data1.isnull().sum()


# In[ ]:




