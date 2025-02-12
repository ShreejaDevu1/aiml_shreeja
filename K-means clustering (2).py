#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from sklearn.cluster import KMeans


# In[2]:


Univ = pd.read_csv("Universities.csv")
Univ


# In[3]:


Univ.info()


# In[4]:


Univ.describe()


# In[5]:


pd.read_csv("Universities.csv")


# ### Standardization of the data

# In[7]:


#Read all numeric columns in to univ1
Univ1 =  Univ.iloc[:,1:]


# In[8]:


Univ1


# In[16]:


cols = Univ1.columns


# In[18]:


#standardization funtion
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_Univ_df = pd.DataFrame(scaler.fit_transform(Univ1),columns = cols)
scaled_Univ_df


# In[20]:


from sklearn.cluster import KMeans
clusters_new=KMeans(3, random_state=0)
clusters_new.fit(scaled_Univ_df)


# In[22]:


clusters_new.labels_


# In[24]:


set(clusters_new.labels_)


# In[26]:


Univ['clusterid_new']=clusters_new.labels_
Univ


# In[28]:


Univ.sort_values(by = "clusterid_new")


# In[30]:


#use groypby() to find aggregated (mean) values in each cluster
Univ.iloc[:,1:].groupby("clusterid_new").mean()


# ## Observations
# - Cluster 2 appears to be the top rated universities cluster as the cut off score,Top 10,SF ratio paramenter mean values are highest
# - Cluster 1 appears to occupy the iddle level rated universities
# - Cluster 0 comes as the lower level rated universities

# In[33]:


Univ[Univ['clusterid_new']==0]


# In[35]:


from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


wcss = []


for i in range(1, 20):
    kmeans = KMeans(n_clusters=i, random_state=0)  # Corrected the class reference
    kmeans.fit(scaled_Univ_df)
    wcss.append(kmeans.inertia_)  # Inertia represents WCSS (Within-Cluster Sum of Squares)

# Print the WCSS values for each k
print(wcss)

# Plot the WCSS against the number of clusters
plt.plot(range(1, 20), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')  # Corrected the typo here
plt.show()


# ## Quality of Clustering

# In[42]:


#quality of clusters is expressed in terms of silhoutte score
from sklearn.metrics import silhouette_score
score = silhouette_score(scaled_Univ_df,\
                         clusters_new.labels_ ,metric='euclidean')
score


# In[ ]:




