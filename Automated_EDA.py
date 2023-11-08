#!/usr/bin/env python
# coding: utf-8

# # Automated EDA tools 

# In[3]:


import pandas as pd


# In[4]:


df=pd.read_csv("Travel.csv")


# In[5]:


df


# # pandas profiling

# In[7]:


pip install pandas-profiling==3.6.1 --user


# In[9]:


from pandas_profiling import ProfileReport


# In[11]:


profile=ProfileReport(df)


# In[12]:


profile.to_file('travel_analysis.html')


# # sweetviz

# In[13]:


pip install sweetviz


# In[1]:


import sweetviz


# In[7]:


import sweetviz as sv

my_report = sv.analyze(df)
my_report.show_html() # Default arguments will generate to "SWEETVIZ_REPORT.html"


# # autoviz

# In[8]:


pip install autoviz


# In[9]:


from autoviz.AutoViz_Class import AutoViz_Class
AV = AutoViz_Class()
df = AV.AutoViz('Travel.csv')


# # dtale

# In[10]:


pip install dtale


# In[11]:


import dtale
d = dtale.show(df)
d.open_browser()


# In[ ]:




