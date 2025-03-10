#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import necessary libraries
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold, StratifiedKFold


# In[3]:


dataframe = pd.read_csv("diabetes.csv")
dataframe


# In[5]:


#Random Forest Classification


# In[11]:


from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

X = dataframe.iloc[:,0:8]
Y = dataframe.iloc[:,8]
Kfold = StratifiedKFold(n_splits=10,random_state = 3,shuffle=True)
model = RandomForestClassifier(n_estimators= 200,random_state= 20,max_depth=None)
results = cross_val_score(model, X, Y, cv=Kfold)
print(results)
print(results.mean())


# In[ ]:


#use Grid search CV to find best parameters (Hyper parameter tuning)
from sklearn.model_selection import GridSearchCV
rf = RandomForestClassifier(random_state=42, n_jobs=-1)
params = {
    'max_depth':[2,3,5,None],
    'min_samples_leaf':[5,10,20],
    'n_estimators':[50,100,200,500],
    'max_features':["sqrt","log2",None]
}
#Instantiate the grid search model
grid_search =  GridSearchCV(estimate=rf,
                            paramgrid=params,
                            cv = 5,
                            n_jobs=-1, verbose=10, scoring="accuracy")
grid_search.fit(X,Y)

