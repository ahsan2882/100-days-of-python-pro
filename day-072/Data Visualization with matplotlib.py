#!/usr/bin/env python
# coding: utf-8

# ## Get the Data
# 
# Either use the provided .csv file or (optionally) get fresh (the freshest?) data from running an SQL query on StackExchange: 
# 
# Follow this link to run the query from [StackExchange](https://data.stackexchange.com/stackoverflow/query/675441/popular-programming-languages-per-over-time-eversql-com) to get your own .csv file
# 
# <code>
# select dateadd(month, datediff(month, 0, q.CreationDate), 0) m, TagName, count(*)
# from PostTags pt
# join Posts q on q.Id=pt.PostId
# join Tags t on t.Id=pt.TagId
# where TagName in ('java','c','c++','python','c#','javascript','assembly','php','perl','ruby','visual basic','swift','r','object-c','scratch','go','swift','delphi')
# and q.CreationDate < dateadd(month, datediff(month, 0, getdate()), 0)
# group by dateadd(month, datediff(month, 0, q.CreationDate), 0), TagName
# order by dateadd(month, datediff(month, 0, q.CreationDate), 0)
# </code>

# ## Import Statements

# In[40]:


import pandas as pd
from matplotlib import pyplot as plt


# ## Data Exploration

# **Challenge**: Read the .csv file and store it in a Pandas dataframe

# In[41]:


df = pd.read_csv('QueryResults.csv',names=['DATE','TAG','POSTS'],header=0)

clean_df = df.dropna()

print(clean_df)


# **Challenge**: Examine the first 5 rows and the last 5 rows of the of the dataframe

# In[42]:


print('HEAD:')
print(clean_df.head())
print('TAIL:')
print(clean_df.tail())


# **Challenge:** Check how many rows and how many columns there are. 
# What are the dimensions of the dataframe?

# In[43]:


print(clean_df.shape)


# **Challenge**: Count the number of entries in each column of the dataframe

# In[44]:


print(clean_df.count())


# **Challenge**: Calculate the total number of post per language.
# Which Programming language has had the highest total number of posts of all time?

# In[45]:


posts_df = clean_df.groupby('TAG').sum()
print(posts_df)


# Some languages are older (e.g., C) and other languages are newer (e.g., Swift). The dataset starts in September 2008.
# 
# **Challenge**: How many months of data exist per language? Which language had the fewest months with an entry? 
# 

# In[46]:


count_df = clean_df.groupby('TAG').count()
print(count_df)


# ## Data Cleaning
# 
# Let's fix the date format to make it more readable. We need to use Pandas to change format from a string of "2008-07-01 00:00:00" to a datetime object with the format of "2008-07-01"

# In[47]:


clean_df['DATE'] = pd.to_datetime(clean_df['DATE'])


# In[47]:





# In[47]:





# ## Data Manipulation
# 
# 

# In[48]:


reshaped_df = clean_df.pivot(columns='TAG',index='DATE',values='POSTS')
print(reshaped_df)


# In[48]:





# **Challenge**: What are the dimensions of our new dataframe? How many rows and columns does it have? Print out the column names and print out the first 5 rows of the dataframe.

# In[49]:


print(reshaped_df.shape)


# In[50]:


print(reshaped_df.columns)


# In[50]:





# **Challenge**: Count the number of entries per programming language. Why might the number of entries be different? 

# In[51]:


print(reshaped_df.count())


# In[52]:


reshaped_df.fillna(0,inplace=True)


# In[73]:


print(reshaped_df.head())
print(reshaped_df.count())


# ## Data Visualisaton with with Matplotlib
# 

# **Challenge**: Use the [matplotlib documentation](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot) to plot a single programming language (e.g., java) on a chart.

# In[73]:





# In[73]:





# In[74]:


plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Posts', fontsize= 16)
plt.ylim(bottom=0,top=35000)
plt.plot(reshaped_df.index,reshaped_df.python)
plt.plot(reshaped_df.index,reshaped_df.java)


# **Challenge**: Show two line (e.g. for Java and Python) on the same chart.

# In[75]:


plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column],label=reshaped_df[column].name,linewidth=3)
plt.legend()


# # Smoothing out Time Series Data
# 
# Time series data can be quite noisy, with a lot of up and down spikes. To better see a trend we can plot an average of, say 6 or 12 observations. This is called the rolling mean. We calculate the average in a window of time and move it forward by one overservation. Pandas has two handy methods already built in to work this out: [rolling()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html) and [mean()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.window.rolling.Rolling.mean.html). 

# In[93]:


roll_df = reshaped_df.rolling(window=2).mean()


# In[94]:


plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=3, label=roll_df[column].name)
plt.legend(fontsize=16)


# In[ ]:





# In[ ]:




