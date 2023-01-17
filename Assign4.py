#!/usr/bin/env python
# coding: utf-8

# In[1]:


games={"basketball","Vollyball","football","cricket"}


# In[2]:


type(games)


# In[3]:


len(games)


# In[4]:


games.remove("football")


# In[5]:


games


# In[6]:


games.add('hockey')


# In[7]:


games


# In[8]:


games.update(["ice-skating","Swimming"])


# In[9]:


games


# In[10]:


for i in games:
    print(i)


# In[11]:


games.clear()


# In[12]:


games


# In[13]:


s1={1,2,3,4}


# In[14]:


s2={2,3,4,5}


# In[15]:


s1.union(s2)


# In[16]:


s1.intersection(s2)


# In[17]:


s1.difference(s2)


# In[ ]:




