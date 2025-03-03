#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder


# In[7]:


iris=pd.read_csv("iris.csv")
iris


# In[11]:


#plot a barchart to visualize the category of class on the "VARIETY"
counts = iris["variety"].value_counts()
plt.bar(counts.index, counts.values)


# In[13]:


iris.info()


# In[15]:


iris[iris.duplicated(keep=False)]


# ## Observations
# 
# There are 150 rows and 5 columns
# There are no Null values
# There is one duplicated row
# The x-columns are sepal.length,sepal.width,petal.length and petal.width
# All the x-columns are continuous
# The y-column is "variety" which is categorical
# There are three flower categories(classes)

# In[21]:


#drop the duplicates
iris = iris.drop_duplicates(keep='first')


# In[23]:


#Ensures further that no duplicated rows are present
iris[iris.duplicated]


# In[25]:


#Reset the index
iris = iris.reset_index(drop=True)
iris


# ## Perform label encoding of target column

# In[28]:


#Encode the three flower classes as 0,1,2
labelencoder = LabelEncoder()
iris.iloc[:, -1] = labelencoder.fit_transform(iris.iloc[:,-1])
iris.head()


# In[30]:


#cgeck datatypes after label encoding
iris.info()


# # Observation
# -The target column"variety" is still object type.It needs to be converted to numeric(int)

# In[33]:


#convert the target column data type to integer
iris['variety']=pd.to_numeric(labelencoder.fit_transform(iris['variety']))
print(iris.info())


# In[35]:


#divide the dataset in to x-columns and y-columns
X=iris.iloc[:,0:4]
Y=iris['variety']


# In[37]:


#further splitting of data into training and testing data sets
x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.3,random_state = 1)
x_train


# ## Building Decision Tree Classifier Using Entropy Criteria

# In[46]:


model = DecisionTreeClassifier(criterion = 'entropy',max_depth = None)
model.fit(x_train,y_train)


# In[48]:


#Plot the decision tree
plt.figure(dpi=1200)
tree.plot_tree(model);


# In[ ]:




