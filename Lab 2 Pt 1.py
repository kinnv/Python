#!/usr/bin/env python
# coding: utf-8

# In[2]:


def addition(X, Y):
    return(X + Y)

def multiply(X, Y):
    return(X * Y)

def subtract(X, Y):
    return(X - Y)

def division(X, Y):
    return(X / Y)

def hello():
    return('Hello World!'')


# In[4]:


print(hello())


# In[10]:


Alist = []
Alist.append(1)
Alist.append(3)
Alist.append(3)
Alist.append("t")


# In[6]:


my_info = ['Kin Vong', 'July 6, 1999']


# In[7]:


print(my_info)


# In[11]:


print(Alist)


# In[12]:


favorite_dogs = {
    'Corgi' : 'Light brown',
    'Shiba' : 'Black and brown',
    'French Bulldog' : 'Black'
}
print(favorite_dogs)


# In[13]:


print(favorite_dogs['Corgi'])


# In[15]:


king_county = {
    'Seattle' : '98108',
    'Federal Way' : '98003',
    'West Seattle' : '98116'
}
print(king_county)


# In[16]:


print(king_county['Seattle'])


# In[20]:


def createList(r1, r2):
    return list(range(r1, r2 + 1))

numbers = createList(1, 20)

print(numbers)


# In[21]:


Sum = 0

for i in numbers:
    Sum += i

print(Sum)


# In[22]:


people = {
    'Kyle' : '26',
    'JingJing' : '22',
    'Kin' : '21',
    'Alex' : '21',
    'Andrew' : '21'
}

print(people)


# In[27]:


for name in people:
    age = people[name]
    print("Name: ", name, "," " Age: ", age, sep='')


# In[ ]:




