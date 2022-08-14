#!/usr/bin/env python
# coding: utf-8

# In[4]:


string = input("enter a string: ")
lst = []
for data in string:
    if data not in lst:
        lst.append(data)
for char in lst:
    print(char," ",string.count(char),"times")


# In[ ]:




