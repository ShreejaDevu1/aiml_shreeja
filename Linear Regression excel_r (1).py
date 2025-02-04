#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf


# In[2]:


data1 = pd.read_csv("NewspaperData.csv")
data1


# In[3]:


data1.info()


# In[4]:


data1.describe()


# In[5]:


#Boxplot for daily column
plt.figure(figsize=(6,3))
plt.title("Box plot for Daily Sales")
plt.boxplot(data1["daily"], vert=False)
plt.show()


# In[6]:


sns.histplot(data1['daily'], kde=True, stat='density',)
plt.show()


# Scatter plot

# In[14]:


x=data1['daily']
y=data1['sunday']
plt.scatter(data1['daily'], data1['sunday'])
plt.xlim(0, max(x)+100)
plt.ylim(0, max(y)+100)
plt.show()


# In[16]:


data1['daily'].corr(data1['sunday'])


# In[18]:


data1[['daily','sunday']].corr()


# #Plot the scatter plot and overlay the fited straight line using matplotlib
# x=data1['daily'].values
# y=data1['sunday'].values
# plt.scatter(x, y, color='m', marker='o', s=30)
# b0=13.84
# b1=1.33
# 
# #plotting the regression line
# plt.plot(x, y, color='g')
# 
# #putting labels
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

# In[21]:


#Plot the scatter plot and overlay the fited straight line using matplotlib
x=data1['daily'].values
y=data1['sunday'].values
plt.scatter(x, y, color='m', marker='o', s=30)
b0=13.84
b1=1.33
#predicted response vector
y_hat=b0+b1*x

#plotting the regression line
plt.plot(x, y, color='g')

#putting labels
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# predict for new data points(test data)

# In[24]:


#predict sunday sales for 200 and 300 and 1500 daily circulation
newdata=pd.Series([200,300,1500])


# In[26]:


data_pred=pd.DataFrame(newdata,columns=['daily'])
data_pred


# In[28]:


import statsmodels.formula.api as smf
model1 = smf.ols("sunday~daily", data = data1).fit()


# In[30]:


model1.predict(data_pred)


# In[32]:


pred=model1.predict(data1['daily'])
pred


# In[34]:


#plot the linear regression line using seaborn regplot() method
sns.regplot(x='daily', y='sunday', data=data1)
plt.xlim([0,1250])
plt.show()


# In[38]:


data1["Y_hat"] = pred
data1


# In[40]:


data1["residuals"] =data1["sunday"]-data1["Y_hat"]
data1


# In[42]:


mse = np.mean((data1["daily"]-data1["Y_hat"])**2)
rmse = np.sqrt(mse)
print("MSE: ",mse)
print("RMSE: ",rmse)


# In[44]:


mae = np.mean(np.abs(data1["daily"]-data1["Y_hat"]))
mae


# In[46]:


plt.scatter(data1["Y_hat"],data1["residuals"])


# In[56]:


# plot the residuals versus y_hat(to check whether residuals are independent of each other)
plt.scatter(data1["Y_hat"],data1["residuals"])
plt.xlabel('Y_hat')
plt.ylabel('Residuals')


# In[50]:


#plot the Q.Q plot (to check the normality of residuals)
import statsmodels.api as sm
sm.qqplot(data1["residuals"],line='45',fit=True)
plt.show()


# In[58]:


sns.histplot(data1['residuals'], kde=True)


# In[ ]:




