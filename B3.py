#!/usr/bin/env python
# coding: utf-8

# In[4]:


x=2
lr=0.01
precision=0.000001
previous_step_size=1
max_iter=10000
iters=0
gf=lambda x:(x+3)**2


# In[5]:


import matplotlib.pyplot as plt


# In[6]:


gd = []


# In[7]:


while precision<previous_step_size and iters < max_iter:
    prev = x
    x = x - lr * gf(prev)
    previous_step_size = abs(x - prev)
    iters += 1
    print('Iteration:',iters,'Value:',x)
    gd.append(x)


# In[8]:


print('Local Minima:',x)


# In[12]:


plt.plot(range(9975),gd)


# In[ ]:




