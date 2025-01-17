#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
data = [10,20,"A",40,9.81]
Series =  pd.Series(data)
print(Series)


# In[9]:


data = {'a' : 10,'b' : 20,'c' : 30}
Series =  pd.Series(data)
print(Series)


# In[11]:


series.replace(20,100)


# In[13]:


import numpy as np
data= np.array([100,200,300])
series = pd.Series(data,index=['a','b','c'])
print(series)


# In[15]:


import pandas as pd
data = {'Name': ['Alice','Bob','Mary'],'Age': [25,30,34],'Country':["USA","UK","AUS"]}
df = pd.DataFrame(data)
print(df)


# In[20]:


iris_df=pd.read_csv("iris.csv")
print(iris_df)


# In[22]:


iris_df.info()


# In[24]:


iris_df.head()


# In[26]:


iris_df.describe()


# In[28]:


print(iris_df.shape)
print(iris_df.ndim)
print(iris_df.size)


# In[30]:


#convert data frame to numpy array
iris_array = np.array(iris_df)
iris_array


# In[32]:


iris_df[["sepal.length","petal.width"]]


# In[34]:


iris_df.info()


# In[36]:


iris_df.head()


# In[40]:


iris_df.iloc[10:21,:]


# In[42]:


iris_df.loc[10:20,"sepal.length":"petal.length"]


# In[44]:


iris_df.loc[10:15:20,"sepal.length":"petal.width"]


# In[46]:


data={"weight":[66,75,84,96,48,71], \
      "height":[156,165,186,165,174,167]}
bmi=pd.DataFrame(data)
bmi


# In[53]:


bmi["BMI"]=bmi["weight"]/(bmi["height"]/100)**2
bmi


# In[56]:


#insert new record
bmi.loc[3]=[78,np.nan,np.nan]
bmi


# In[72]:


#check column-wise sum of NaN values(missing values)
bmi.isnull().sum()


# In[74]:


#Replace missing value 65kg value of that 
bmi["height"]=bmi["height"].fillna(165)
bmi


# In[76]:


bmi.drop("BMI",axis=1,inplace=True)
bmi


# In[83]:


import matplotlib.pyplot as plt
plt.hist(iris_df["sepal.length"],color="green")


# In[ ]:




