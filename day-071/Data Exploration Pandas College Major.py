#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
from pathlib import Path

CSV_PATH = Path(
    'salaries_by_college_major.csv'
).resolve()

df = pd.read_csv(CSV_PATH)


# In[33]:


clean_df = df.dropna()
clean_df


# In[34]:


idx = clean_df['Starting Median Salary'].idxmax()
print(clean_df.loc[idx])


# In[35]:


print(clean_df['Mid-Career Median Salary'].max())
idx = clean_df['Mid-Career Median Salary'].idxmax()
print(clean_df['Undergraduate Major'][idx])


# In[36]:


print(clean_df['Starting Median Salary'].min())
idx = clean_df['Starting Median Salary'].idxmin()
print(clean_df['Undergraduate Major'][idx])


# In[37]:


print(clean_df['Mid-Career Median Salary'].min())
idx = clean_df['Mid-Career Median Salary'].idxmin()
print(clean_df['Undergraduate Major'][idx])


# In[38]:


spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
clean_df


# In[43]:


low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']]


# In[44]:


highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']]


# In[48]:


pd.options.display.float_format = '{:,.2f}'.format 
highest_spread = clean_df.sort_values('Spread', ascending=False)
highest_spread[['Undergraduate Major', 'Spread']]


# In[49]:


clean_df.groupby('Group').count()


# In[50]:


clean_df.groupby('Group').mean()

