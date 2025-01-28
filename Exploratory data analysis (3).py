#!/usr/bin/env python
# coding: utf-8

# In[1]:


#load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv("data_clean.csv")
data


# In[3]:


data.info()


# In[4]:


print(type(data))
print(data.shape)


# In[5]:


data.dtypes


# In[6]:


data1 = data.drop(['Unnamed: 0',"Temp C"], axis =1)
data1


# In[7]:


#convert the Month column data to integer data type
data1['Month']=pd.to_numeric(data['Month'],errors='coerce')
data1.info


# In[8]:


#checking for duplicate rows in the table 
#print duplicated rows
data1[data1.duplicated()]


# In[9]:


#print all duplicated rows
data1[data1.duplicated(keep=False)]


# In[10]:


#change column names(Rename the columns)
data1.rename({'Solar.R':'Solar'},axis=1,inplace = True)
data1


# In[11]:


#change column names(Rename the columns)
data1.rename({'Solar.R':'Solar','Temp':'Temperature'},axis=1,inplace = True)
data1


# In[12]:


#display total missing values count in each columns using isnull().sum()
data1.isnull().sum()


# In[13]:


#visualize data1 missing values using graph
cols = data1.columns
colours=['black','yellow']
sns.heatmap(data1[cols].isnull(),cmap=sns.color_palette(colours),cbar=True)


# In[14]:


#find the mean and median values of each numeric column
#Imputation of missing value with median
median_ozone =  data1["Ozone"].median()
mean_ozone = data1["Ozone"].mean()
print("Medium of Ozone: ",median_ozone)
print("Mean of Ozone: ",mean_ozone)


# In[15]:


#Replace the ozone missing values with median value
data1['Ozone'] = data1['Ozone'].fillna(median_ozone)
data1.isnull().sum()


# In[22]:


#find the mode values of categorical column(weather)
print(data1["Weather"].value_counts())
mode_weather = data1["Weather"].mode()[0]
print(mode_weather)


# In[29]:


#Impute missing values(Replace NaN with mode etc.)of "Weather" using fillna()
data1["Weather"] = data1["Weather"].fillna(mode_weather)
data1.isnull().sum()


# In[34]:


data1.tail


# In[37]:


data1.reset_index(drop=True)


# In[39]:


#create a figure with two subplots, stacked vertically
fig, axes = plt.subplots(2,1, figsize=(8,6),gridspec_kw={'height_ratios':[1,3]})
#plot the boxplot  in the first(top)subplot
sns.boxplot(data=data1["Ozone"],ax=axes[0], color='skyblue', width=0.5,orient='h')
axes[0].set_title("Boxplot")
axes[0].set_xlabel("Ozone Levels")
#plot the histoogram with KDE curve in the second (bottom) subplot
sns.histplot(data1["Ozone"], kde=True, ax=axes[1],color='purple', bins=30)
axes[1].set_title("Histogram with KDE")
axes[1].set_xlabel("Ozone Levels")
axes[1].set_ylabel("Frequency")
#adjust layout for letter spacing
plt.tight_layout()
#show the plot
plt.show()


# In[41]:


#observations:
#1)The ozone column has extreme values beyond 81 as seen from box plot
#2)The same is confirmed from the below right-skewed histogram


# In[43]:


#for solar(subplots)
fig, axes = plt.subplots(2,1, figsize=(8,6),gridspec_kw={'height_ratios':[1,3]})
#plot the boxplot  in the first(top)subplot
sns.boxplot(data=data1["Solar"],ax=axes[0], color='skyblue', width=0.5,orient='h')
axes[0].set_title("Boxplot")
axes[0].set_xlabel("Solar Levels")
#plot the histoogram with KDE curve in the second (bottom) subplot
sns.histplot(data1["Solar"], kde=True, ax=axes[1],color='purple', bins=30)
axes[1].set_title("Histogram with KDE")
axes[1].set_xlabel("Ozone Levels")
axes[1].set_ylabel("Frequency")
#adjust layout for letter spacing
plt.tight_layout()
#show the plot
plt.show()


# In[49]:


#Create a figure for violin plot
sns.violinplot(data=data1["Ozone"],color='lavender')
plt.title("Violin Plot")
plt.show()


# In[47]:


plt.figure(figsize=(6,2))
boxplot_data=plt.boxplot(data1["Ozone"],vert=False)
[item.get_xdata() for item in boxplot_data['fliers']]


# In[51]:


data1["Ozone"].describe()


# In[59]:


mu = data1["Ozone"].describe()[1]
sigma = data1["Ozone"].describe()[2]
for x in data1["Ozone"]:
    if((x < (mu - 3*sigma)) or (x > (mu + 3*sigma))):
        print(x)


# In[61]:


import scipy.stats as stats
#create Q-Q plot
plt.figure(figsize=(8,6))
stats.probplot(data1["Ozone"],dist="norm", plot=plt)
plt.title("Q-Q Plot for Outlier Detection", fontsize=14)
plt.xlabel("Theoretical Quantiles",fontsize=12)


# In[ ]:




