#!/usr/bin/env python
# coding: utf-8

# In[66]:


import pandas as pd
import numpy as np


# In[68]:


df= pd.read_csv("universities.csv")
df


# In[70]:


np.std(df["GradRate"])


# In[72]:


df.describe


# In[74]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[76]:


plt.figure(figsize=(6,3))
plt.title("Acceptance Ratio")
plt.hist(df["Accept"])


# In[78]:


np.var(df["SFRatio"])


# In[80]:


np.mean(df["SAT"])


# In[82]:


np.median(df["SAT"])


# In[84]:


df.describe()


# In[86]:


sns.histplot(df["Accept"])


# In[88]:


sns.histplot(df["Accept"], kde =True)


# In[90]:


s1=[20,15,10,25,30,35,28,40,45,60]
scores1= pd.Series(s1)
scores1


# In[94]:


plt.boxplot(scores1, vert=False)


# In[96]:


df = pd.read_csv("universities.csv")
print(df)
plt.boxplot(df["SAT"])


# In[ ]:




