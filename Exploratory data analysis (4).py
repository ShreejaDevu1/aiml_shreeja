#!/usr/bin/env python
# coding: utf-8

# In[73]:


#load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[75]:


data = pd.read_csv("data_clean.csv")
data


# In[77]:


data.info()


# In[79]:


print(type(data))
print(data.shape)


# In[81]:


data.dtypes


# In[83]:


data1 = data.drop(['Unnamed: 0',"Temp C"], axis =1)
data1


# In[85]:


#convert the Month column data to integer data type
data1['Month']=pd.to_numeric(data['Month'],errors='coerce')
data1.info


# In[87]:


#checking for duplicate rows in the table 
#print duplicated rows
data1[data1.duplicated()]


# In[89]:


#print all duplicated rows
data1[data1.duplicated(keep=False)]


# In[91]:


#change column names(Rename the columns)
data1.rename({'Solar.R':'Solar'},axis=1,inplace = True)
data1


# In[93]:


#change column names(Rename the columns)
data1.rename({'Solar.R':'Solar','Temp':'Temperature'},axis=1,inplace = True)
data1


# In[95]:


#display total missing values count in each columns using isnull().sum()
data1.isnull().sum()


# In[97]:


#visualize data1 missing values using graph
cols = data1.columns
colours=['black','yellow']
sns.heatmap(data1[cols].isnull(),cmap=sns.color_palette(colours),cbar=True)


# In[98]:


#find the mean and median values of each numeric column
#Imputation of missing value with median
median_ozone =  data1["Ozone"].median()
mean_ozone = data1["Ozone"].mean()
print("Medium of Ozone: ",median_ozone)
print("Mean of Ozone: ",mean_ozone)


# In[101]:


#Replace the ozone missing values with median value
data1['Ozone'] = data1['Ozone'].fillna(median_ozone)
data1.isnull().sum()


# In[103]:


#find the mode values of categorical column(weather)
print(data1["Weather"].value_counts())
mode_weather = data1["Weather"].mode()[0]
print(mode_weather)


# In[105]:


#Impute missing values(Replace NaN with mode etc.)of "Weather" using fillna()
data1["Weather"] = data1["Weather"].fillna(mode_weather)
data1.isnull().sum()


# In[107]:


data1.tail


# In[109]:


data1.reset_index(drop=True)


# In[111]:


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


# In[112]:


#observations:
#1)The ozone column has extreme values beyond 81 as seen from box plot
#2)The same is confirmed from the below right-skewed histogram


# In[115]:


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


# In[116]:


#Create a figure for violin plot
sns.violinplot(data=data1["Ozone"],color='lavender')
plt.title("Violin Plot")
plt.show()


# In[119]:


plt.figure(figsize=(6,2))
boxplot_data=plt.boxplot(data1["Ozone"],vert=False)
[item.get_xdata() for item in boxplot_data['fliers']]


# In[121]:


data1["Ozone"].describe()


# In[123]:


mu = data1["Ozone"].describe()[1]
sigma = data1["Ozone"].describe()[2]
for x in data1["Ozone"]:
    if((x < (mu - 3*sigma)) or (x > (mu + 3*sigma))):
        print(x)


# In[125]:


import scipy.stats as stats
#create Q-Q plot
plt.figure(figsize=(8,6))
stats.probplot(data1["Ozone"],dist="norm", plot=plt)
plt.title("Q-Q Plot for Outlier Detection", fontsize=14)
plt.xlabel("Theoretical Quantiles",fontsize=12)


# In[127]:


sns.swarmplot(data=data1, x="Weather", y="Ozone", color="orange", size=6)


# In[128]:


sns.stripplot(data=data1, x="Weather", y="Ozone", color="orange", size=6, jitter=True)


# In[131]:


#category wise boxplot for ozone
sns.boxplot(data=data1, x="Weather", y="Ozone")


# In[135]:


plt.scatter(data1["Wind"], data1["Temperature"])


# In[139]:


#it is observed that there is a mild negative correlation
#compute pearson correlation coefficient
#between Wind speed and Temperature
data1["Wind"].corr(data1["Temperature"])


# In[ ]:




