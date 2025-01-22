#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np


# In[9]:


df= pd.read_csv("universities.csv")
df


# In[11]:


np.std(df["GradRate"])


# In[15]:


df.describe


# In[17]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[19]:


plt.figure(figsize=(6,3))
plt.title("Acceptance Ratio")
plt.hist(df["Accept"])


# In[21]:


np.var(df["SFRatio"])


# In[23]:


np.mean(df["SAT"])


# In[25]:


np.median(df["SAT"])


# In[27]:


df.describe()


# In[29]:


sns.histplot(df["Accept"])


# In[35]:


sns.histplot(df["Accept"], kde =True)


# In[ ]:




