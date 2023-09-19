#!/usr/bin/env python
# coding: utf-8

# In[153]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[154]:


from urllib.request import urlopen
from bs4 import BeautifulSoup


# In[155]:


url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)


# In[156]:


soup = BeautifulSoup(html, 'lxml')
type(soup)


# In[157]:


# Get the title
title = soup.title
print(title)


# In[135]:


#company_name=[]
#for company in bsobj.findAll('div',{'class':'w_iUH7'}):
 # company_name.append(company.a.text.strip())


# In[131]:


#company_name 


# In[158]:


all_links = soup.find_all("a")
for link in all_links:
    print(link.get("href"))


# In[ ]:




