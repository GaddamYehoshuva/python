#!/usr/bin/env python
# coding: utf-8

# In[1]:


def reverse(s):
    str = ""
    for i in s:
        str =i + str
    return str
s=input("enter the string :")
print ("the original string is :",end="")
print(s)
print("the reversed string is : ",end="")
print(reverse(s))


# In[ ]:




