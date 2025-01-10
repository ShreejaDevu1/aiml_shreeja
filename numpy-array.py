#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
a=np.array([10,20,30,40])
print(a)


# In[9]:


c = np.arange(1,5)
print(a)
type(a)


# In[11]:


a=np.array([1,2,3,4])
np.sqrt(a)


# In[13]:


a1=np.array([[3,4,5,6],[37,8,9,np.NAN]])
a1_copy1=a1.astype(float)
a1_copy1.dtype


# In[15]:


a1=np.array([[3,4,5,6],[37,8,9,np.NAN]])
print(a1)
a1.dtype


# In[17]:


a1_copy1=a1.astype(str)
print(a1_copy1)
a1_copy1.dtype


# In[19]:


b=np.array([[3,4,6],[7,9,10],[4,6,12]])
b


# In[22]:


a3=np.array([[3,4,5],[5,6,7],[8,9,0]])
print(a3)
np.fill_diagonal(a3,0)
print(a3)


# In[24]:


A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
C = np.matmul(A,B)
print(C)


# In[30]:


#
print(A.T)
print(B.T)


# In[44]:


#accessing array elements
A4= np.array([[3,4,5],[7,2,8],[9,1,6],[10,9,18]])
A4


# In[ ]:




