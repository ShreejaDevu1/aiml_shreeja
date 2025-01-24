#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


data = pd.read_csv("data_clean.csv")
data


# In[7]:


data.info()


# In[9]:


print(type(data))
print(data.shape)


# In[11]:


data.dtypes


# In[15]:


data1 = data.drop(['Unnamed: 0',"Temp C"], axis =1)
data1


# In[19]:


#convert the Month column data to integer data type
data1['Month']=pd.to_numeric(data['Month'],errors='coerce')
data1.info


# In[21]:


#checking for duplicate rows in the table 
#print duplicated rows
data1[data1.duplicated()]


# In[23]:


#print all duplicated rows
data1[data1.duplicated(keep=False)]


# In[ ]:




