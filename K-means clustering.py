#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from sklearn.cluster import KMeans


# In[5]:


Univ = pd.read_csv("Universities.csv")
Univ


# In[7]:


Univ.info()


# In[9]:


Univ.describe()


# In[17]:


pd.read_csv("Universities.csv")


# ### Standardization of the data

# In[20]:


#Read all numeric columns in to univ1
Univ1 =  Univ.iloc[:,1:]


# In[22]:


Univ1


# In[24]:


cols = Univ1.columns


# In[26]:


#standardization funtion
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_Univ_df = pd.DataFrame(scaler.fit_transform(Univ1),columns = cols)
scaled_Univ_df


# In[ ]:




