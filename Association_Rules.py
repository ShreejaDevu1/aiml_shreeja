#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Install mlxtend library
get_ipython().system('pip install mlxtend')


# In[3]:


#Import necessary libraries
import pandas as pd
import mlxtend
from mlxtend.frequent_patterns import apriori,association_rules
import matplotlib.pyplot as plt


# In[9]:


#from google.colab import files
#uploaded = files.upload()


# In[11]:


#print the dataframe
titanic = pd.read_csv("Titanic.csv")
titanic


# In[7]:


titanic.info()


# ## Observations
# - All columns are object data type and categorical in value
# - there are no null values
# - As the columns are categorical, we can adopt one-hot-encoding

# In[14]:


#plot a bar chart to visualize the category of class on the ship
counts = titanic['Class'].value_counts()
plt.bar(counts.index, counts.values)


# In[16]:


#perform one-hot encoding on categorical columns
df = pd.get_dummies(titanic,dtype=int)
df.head()


# In[18]:


df.info()


# ## Apriori Algorithm

# In[23]:


#Apply Apriori Algorithm to get itemset combinations
frequent_itemsets = apriori(df, min_support = 0.05, use_colnames=True, max_len=None)
frequent_itemsets


# In[25]:


frequent_itemsets.info()


# In[27]:


#generate association rules with metrics
rules = association_rules(frequent_itemsets, metric="lift",min_threshold=1.0)
rules


# In[29]:


rules.sort_values(by='lift',ascending = False)


# ## Conclusion
# - Adult females travelling in 1st class survived most

# In[32]:


import matplotlib.pyplot as plt
rules[['support','confidence','lift']].hist(figsize=(15,7))
plt.show()


# In[ ]:




