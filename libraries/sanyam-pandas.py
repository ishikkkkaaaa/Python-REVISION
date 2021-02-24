#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[8]:


GDP=[25,35,45,55,65]
years=[2000,2001,2002,2003,2004]
plt.plot(years,GDP)
plt.xlabel("years")
plt.ylabel("GDP")
plt.scatter(years,GDP)
plt.text(2000,45,"low latency")
plt.grid(True)
plt.show()


# In[12]:


year=[2019,2020,2021]
cgpa=[8.05,8.81,9.08]
plt.plot(year,cgpa)
plt.xlabel("Years of College")
plt.ylabel("CGPA scored")
plt.scatter(year,cgpa,alpha=1)
plt.grid(True)
plt.show()


# In[17]:


teams=['groupA', 'groupB', 'groupC']
values=[10,20,50]
plt.figure(figsize=(10,3))
plt.subplot(131)
plt.bar(teams,values)
plt.subplot(132)
plt.plot(teams,values,linewidth=5)
plt.subplot(133)
plt.scatter(teams,values)
plt.suptitle('Categorical plotting')
plt.show()


# In[1]:


import pandas as pd


# In[2]:


my_dict={
    'countries':['Russia','China','India','Japan'],'capitals':['Moscow','Delhi','Delhi','Bejing']
}

my_dict
# In[4]:


dataframe1 = pd.DataFrame(my_dict)


# In[5]:


dataframe1


# In[6]:


dataframe1.index=('R','C','I','J')


# In[7]:


dataframe1


# In[15]:


csv=pd.read_csv("D:\company_sales_data.csv")


# In[16]:


index_col=0


# In[21]:


csv.facecream


# In[25]:


type(csv[['facecream']])


# In[26]:


type(csv['facecream'])


# In[27]:


type(csv[['facecream','total_units']])


# In[28]:


csv[['facecream','total_units']]


# In[29]:


csv


# In[30]:


csv[1:5]


# In[34]:


csv.loc[5]


# In[36]:


csv.index= ['a','c','d','e','r','t','u','i','o','p','b','h']


# In[37]:


csv


# In[47]:


csv.loc[:,['facecream','bathingsoap','moisturizer']]


# In[44]:


csv.loc['p']


# In[46]:


csv.loc[['p','a','b']] //by names


# In[53]:


csv.iloc[[1,2,3],[0,1,2]]   //using indexes


# In[49]:


csv


# In[54]:


import matplotlib.pyplot as plt


# In[63]:


file=pd.read_csv("D:\company_sales_data.csv")


# In[67]:


plt.plot(csv.iloc[8],csv.iloc[9])
plt.xlabel()
plt.show()


# In[ ]:


ye bhi github par ?

