#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[18]:


df = pd.read_csv('spelling words.csv')
df.head()


# In[26]:


print(df['Words'].sample(n=4, axis=0))


# In[ ]:





# In[ ]:




