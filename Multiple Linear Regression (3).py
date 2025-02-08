#!/usr/bin/env python
# coding: utf-8

# ASSUMPTIONS: 
# 1.Linearity: The relationship between the predictors(X) and the response(Y) is linear.
# 2.Independence: Observations are independent of each other. 
# 3.Homoscedasticity: The residuals(Y-Y_hat) exhibit constant variance at all levels of the predictor.
# 4.Normal Distribution Of Errors: The residuals of the model are normally distributed.

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
from statsmodels.graphics.regressionplots import influence_plot
import numpy as np


# In[3]:


#Read the data from csv file
cars = pd.read_csv("Cars.csv")
cars.head()


# In[4]:


#Rearrange columns
cars = pd.DataFrame(cars,columns=["HP","VOL","SP","WT","MPG"])
cars.head


# #Description of columns:
# - MPG:Milege of car(Mile per Gallon)(This is Y-Column to be predicted)
# - HP:Horse Power  of the car(X1 Column)
# - VOL: Volume of the car (size) (X2 column)
# - SP: Top speed of the car(Miles per Hour)(X3 column)
# - WT: Weight of the car(pounds)(X4 column)

# #Observations
# - There are no missing values
# - There are 81 observations(81 different cars data)
# - The datatypes of the columns are relevant and valid

# In[7]:


fig, (ax_box, ax_hist)=plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})
sns.boxplot(data=cars, x='HP', ax=ax_box, orient='h')
ax_box.set(xlabel='')
sns.histplot(data=cars, x='HP', ax=ax_hist, bins=30, kde=True, stat="density")
ax_hist.set(ylabel='Density')
plt.tight_layout()
plt.show()


# Observations:
# 
# There are some extreme values (outliers) observed in towards the right tail of SP and HP distributions.
# In VOL and WT columns,a few outliers are observed in both tails of their distributions.
# The extreme values of cars data may have come from the specially designed nature of cars.
# As this is multi-dimensional data,the outliers with respect to spatial dimensions may have to be considered while building the regression model.

# Chceking for duplicated rows

# In[10]:


cars[cars.duplicated()]


# Pair plot and correlation coefficients

# In[12]:


sns.set_style(style='darkgrid')
sns.pairplot(cars)


# Observations form correlation plots coefficient
# - Between x and y,all the variables are showing moderate to high correlation strengths,highest between MPG and HP
# - Therefore the dataset qualifies tfor building a multiple linear regression model to predict MPG
# - Among x columns (x1,x2,x3 and x4),some very high correlation strengths are observed between SP vs HP,VOL vs WT
# - THe high correlation among x columns is not desirable as it might lead to multicollinearity problem

# Preparing the preliminary model considering all X columns

# In[18]:


#Build model
#import statsmodel.formula.api as smf
model = smf.ols('MPG~WT+VOL+SP+HP',data=cars).fit()


# In[20]:


model.summary()


# Performance Metrics for model1

# In[23]:


#Find the performance metrics
#create a data frame with actual y and predicted y columns

df1= pd.DataFrame()
df1["actual_y1"]=cars["MPG"]
df1.head()


# In[24]:


#Predict for the given x data columns
pred_y1 = model.predict(cars.iloc[:,0:4])
df1["pred_y1"]=pred_y1
df1.head()


# In[25]:


#Rearrange the columns
cars = pd.DataFrame(cars, columns=["HP","VOL","SP","WT","MPG"])
cars.head()


# In[26]:


df1.head()


# In[27]:


#compute the MSE,RMSE,MAE for model
from sklearn.metrics import mean_squared_error,mean_absolute_error
print("MSE:",mean_squared_error(df1["actual_y1"],df1["pred_y1"]))


# In[28]:


#predict for the given data columns
pred_y1 = model.predict(cars.iloc[:,0:4])
df1["pred_y1"] = pred_y1
df1.head


# In[29]:


#compute the Mean squared error(MSE0, RMSE for model
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(df1["actual_y1"], df1["pred_y1"])
print("MSE :", mse)
print("RMSE :",np.sqrt(mse))


# Checking for multicollinearity among x-columns using VIF method

# In[31]:


# Compute VIF values
rsq_hp = smf.ols('HP~WT+VOL+SP',data=cars).fit().rsquared
vif_hp = 1/(1-rsq_hp)

rsq_wt = smf.ols('WT~HP+VOL+SP',data=cars).fit().rsquared  
vif_wt = 1/(1-rsq_wt) 

rsq_vol = smf.ols('VOL~WT+SP+HP',data=cars).fit().rsquared  
vif_vol = 1/(1-rsq_vol) 0

rsq_sp = smf.ols('SP~WT+VOL+HP',data=cars).fit().rsquared  
vif_sp = 1/(1-rsq_sp) 

# Storing vif values in a data frame
d1 = {'Variables':['Hp','WT','VOL','SP'],'VIF':[vif_hp,vif_wt,vif_vol,vif_sp]}
Vif_frame = pd.DataFrame(d1)  
Vif_frame


# Observations:
# - The ideal range of VIF values shall be between 0 and 10. However slightly higher values can be tolerated
# - As seen from very high VIF values for VOL and WT,it is clear that they are prone to multicollinearity problem
# - Hence it is decided to drop one of the columns(either VOL and WT) to overcome the multicollinearity
# - it is decided to drop WT and retain VOL column in further models

# In[ ]:


cars1 = cars.drop("WT", axis=1)
cars1.head()


# In[ ]:


#build model
import statsmodels.formula.api as smf
model2 = smf.ols('MPG~VOL+SP+HP',data=cars1).fit()


# In[ ]:


#create a data frame with actual y and predicted y columns
df2 = pd.DataFrame()
df2["actual_y2"] = cars["MPG"]
df2.head()


# In[ ]:


pred_y2 = model.predict(cars.iloc[:,0:4])
df2["pred_y2"]=pred_y2
df2.head()


# In[ ]:


#compute the Mean squared error(MSE0, RMSE for model
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(df2["actual_y2"], df2["pred_y2"])
print("MSE :", mse)
print("RMSE :",np.sqrt(mse))


# #### Obsevation from model2 summary()
# - The adjusted R-Squared value improved slightly to 0.76
# - All the p-values for model parameters less than 5% hence they are significant
# - Therefore the HP,VOL,SP columns are finalized as the significant predictor for MPG response variable
# - There is no improvement in MSE value

# ## Identification of High influence points(spatial outliers)

# In[37]:


cars.shape


# ## Leverage Values

# Leverage values diagnose if a data point has an extreme value in terms of the independent variables. A point with high leverage has a great ability to influence the regression line. The threshold for considering a point as having high leverage is typically set at 3(k+1)/n, where k is the number of predictors and n is the sample size.

# In[41]:


#Define variables and assign values
k=3
n=81
leverage_cutoff=3*((k+1)/n)
leverage_cutoff


# In[43]:


from statsmodels.graphics.regressionplots import influence_plot
influence_plot(model,alpha=.05)
y=[i for i in range(-2,8)]
x=[leverage_cutoff for i in range(10)]
plt.plot(x,y,'r+')
plt.show()


# In[59]:


cars1 =  cars.drop("WT", axis=1)
cars1.head()


# In[61]:


cars1[cars1.index.isin([65,70,76,78,79,80])]


# In[63]:


cars2=cars1.drop(cars1.index[[65,70,76,78,79,80]],axis=0).reset_index(drop=True)
cars2


# ## Build Model 3 on cars2 dataset

# In[68]:


#rebuild the model model
model3 = smf.ols('MPG~VOL+SP+HP',data = cars2).fit()


# In[70]:


model3.summary()


# # Performance Metrics for Model3

# In[73]:


df3=pd.DataFrame()
df3['actual_y3']=cars2['MPG']
df3.head()


# In[85]:


#predict on all x data columns
pred_y3 = model3.predict(cars2.iloc[0:3])
df3["pred3_y3"] = pred_y3
df3.head()


# In[89]:


import numpy as np
from sklearn.metrics import mean_squared_error
df_clean = df3.dropna(subset=["actual_y3", "pred3_y3"])
mse = mean_squared_error(df_clean["actual_y3"], df_clean["pred3_y3"])
print("MSE:", mse)
print("RMSE:", np.sqrt(mse))


# #### Comparison of models
#                      
# 
# | Metric         | Model 1 | Model 2 | Model 3 |
# |----------------|---------|---------|---------|
# | R-squared      | 0.771   | 0.770   | 0.885   |
# | Adj. R-squared | 0.758   | 0.761   | 0.880   |
# | MSE            | 18.89   | 18.91   | 8.68    |
# | RMSE           | 4.34    | 4.34    | 2.94    |
# 
# 
# - **From the above comparison table it is observed that model3 is the best among all with superior performance metrics**

# In[ ]:




