#!/usr/bin/env python
# coding: utf-8

# In[1]:


t1=("Adarsh",10,10.2,False,"a","A","a")


# In[2]:


type(t1)


# In[3]:


t2=tuple(("Adarsh",10,10.2,False,"a","A","a",["Kite",10]))


# In[4]:


type(t2)


# In[6]:


len(t1)


# In[7]:


len(t2)


# In[9]:


t1.count("a")


# In[10]:


t2.count("a")


# In[11]:


t1+t2


# In[13]:


t1*4


# In[15]:


t1.insert(1,"hello")


# In[19]:


del t1


# In[20]:


t1


# In[22]:


t2[1]


# In[23]:


t2[0:3]


# In[24]:


t2[-1]


# In[ ]:




