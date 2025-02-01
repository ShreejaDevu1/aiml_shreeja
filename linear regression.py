#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf


# In[7]:


data1 = pd.read_csv("NewspaperData.csv")
data1


# In[9]:


data1.info()


# In[11]:


data1.describe()


# In[13]:


#Boxplot for daily column
plt.figure(figsize=(6,3))
plt.title("Box plot for Daily Sales")
plt.boxplot(data1["daily"], vert=False)
plt.show()


# In[15]:


data1["daily"].corr(data1["sunday"])


# In[21]:


data1[["daily","sunday"]].corr()


# Observations:
# The relationship between x(Daily) and y(sunday) is seen to be linear as seen from scatter plot
# The correlation is strong positive with pearson's correlation coefficient of 0.958154

# In[ ]:




