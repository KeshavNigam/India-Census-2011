#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv(r"E:\\Data\\India _Census_2011\\India_Census_2011.csv")


# In[4]:


data


# In[5]:


data.shape


# In[9]:


data.head()


# In[10]:


data.size


# In[11]:


data.columns


# In[12]:


data.dtypes


# In[13]:


data.info()


# In[14]:


data.describe()


# In[17]:


data.index


# In[18]:


data.count()


# In[19]:


# Q. 1) How will you hide the indexes of the dataframe.?


# In[20]:


data.head(2)


# In[29]:


data.style.hide_index()


# In[25]:


# Q. 2) How can we set the caption / heading on the dataframe.?


# In[26]:


data.head(2)


# In[30]:


data.style.set_caption('India_Census_2011')


# In[31]:


# Q. 3) Show the records related with the districts - New Delhi , Lucknow , Jaipur.?


# In[32]:


data.head(2)


# In[35]:


data['District_name'].isin(['New Delhi','Lucknow','Jaipur'])


# In[36]:


data[data['District_name'].isin(['New Delhi','Lucknow','Jaipur'])]


# In[37]:


# Q. 4) Calculate state-wise :
# A. Total number of population.


# In[38]:


data.head(2)


# In[39]:


data.groupby('State_name').Population.sum()


# In[40]:


# B. Total no. of the population with different religions.?


# In[41]:


data.head(2)


# In[45]:


data.groupby('State_name')['Hindus', 'Muslims', 'Christians', 'Sikhs', 'Buddhists', 'Jains'].sum()


# In[46]:


#Q. 5) How many Male Workers were there in Maharashtra state ?


# In[47]:


data.head(2)


# In[59]:


data[data.State_name =='MAHARASHTRA']['Male_Workers'].sum()


# In[60]:


# Q. 6) How to set a column as index of the dataframe ?


# In[61]:


data.head(2)


# In[62]:


data.set_index('District_code')


# In[63]:


# Q. 7a) Add a Suffix to the column names.?


# In[64]:


data.head(2)


# In[65]:


data.add_suffix('__rightone')


# In[66]:


#Q. 7b) Add a Prefix to the column names.?


# In[67]:


data.head(2)


# In[68]:


data.add_prefix('__leftone')


# In[ ]:




