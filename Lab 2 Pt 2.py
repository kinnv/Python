#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


InpatientData = pd.read_csv('./Downloads/estimated_inpatient_all_20201120_2144.csv')


# In[5]:


InpatientData


# In[6]:


InpatientData.loc[InpatientData['state'] == 'WA']


# In[27]:


import math
def factorial(X):
    return math.factorial(X)


# In[63]:


def factorial(X):
    number = X
    factorial = 1
    for i in range(1,number + 1):
        factorial *= i
    print(factorial)


# In[64]:


factorial(3)


# In[173]:


numbers = [2, 10, 4, 6, 7]

def list_sum(X):
    Sum = 0
    for i in X:
        Sum += i
    return print(Sum)


# In[174]:


list_sum(numbers)


# In[113]:


def my_list(numbers):
       sorted_list = sorted(numbers)
       return sorted_list
       


# In[114]:


my_list(numbers)


# In[175]:


dnumbers = [6, 7, 1, 5, 10, 23, 60, 100]

def greater_than_20(X):
    new_list = []
    for i in X:
        if i > 20:
            new_list.append(i)
    return new_list
        
    


# In[176]:


greater_than_20(dnumbers)


# In[177]:


def count_of_20(greater_than_20, X):
    greater_than_20(X)
    count = 0
    for i in new_list:
        i = 1
        count += i
    return count


# In[178]:


count_of_20(greater_than_20, dnumbers)


# In[165]:





# In[ ]:




