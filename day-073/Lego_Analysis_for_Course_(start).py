#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# Today we'll dive deep into a dataset all about LEGO. From the dataset we can ask whole bunch of interesting questions about the history of the LEGO company, their product offering, and which LEGO set ultimately rules them all:
# 
# <ul type="square">
# <li>What is the most enormous LEGO set ever created and how many parts did it have?</li>
# 
# <li>How did the LEGO company start out? In which year were the first LEGO sets released and how many sets did the company sell when it first launched?</li>
# 
# <li>Which LEGO theme has the most sets? Is it one of LEGO's own themes like Ninjago or a theme they licensed liked Harry Potter or Marvel Superheroes?</li>
# 
# <li>When did the LEGO company really expand its product offering? Can we spot a change in the company strategy based on how many themes and sets did it released year-on-year?</li>
# 
# <li>Did LEGO sets grow in size and complexity over time? Do older LEGO 
# sets tend to have more or fewer parts than newer sets?</li>
# </ul>
# 
# **Data Source**
# 
# [Rebrickable](https://rebrickable.com/downloads/) has compiled data on all the LEGO pieces in existence. I recommend you use download the .csv files provided in this lesson.

# <img src="assets/bricks.jpg">

# # Import Statements

# In[80]:


import pandas as pd
from matplotlib import pyplot as plt


# # Data Exploration

# **Challenge**: How many different colours does the LEGO company produce? Read the colors.csv file in the data folder and find the total number of unique colours. Try using the [.nunique() method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.nunique.html?highlight=nunique#pandas.DataFrame.nunique) to accomplish this.

# In[81]:


df = pd.read_csv('data/colors.csv')
df = df.dropna()
df['name'].nunique()


# **Challenge**: Find the number of transparent colours where <code>is_trans == 't'</code> versus the number of opaque colours where <code>is_trans == 'f'</code>. See if you can accomplish this in two different ways.

# In[82]:


df.groupby('is_trans').count()


# In[83]:


df.is_trans.value_counts()


# ### Understanding LEGO Themes vs. LEGO Sets

# Walk into a LEGO store and you will see their products organised by theme. Their themes include Star Wars, Batman, Harry Potter and many more.
# 
# <img src='https://i.imgur.com/aKcwkSx.png'>

# A lego set is a particular box of LEGO or product. Therefore, a single theme typically has many different sets.
# 
# <img src="https://i.imgur.com/whB1olq.png ">

# The <code>sets.csv</code> data contains a list of sets over the years and the number of parts that each of these sets contained.
# 
# **Challenge**: Read the sets.csv data and take a look at the first and last couple of rows.

# In[84]:


sets = pd.read_csv('data/sets.csv')


# In[85]:


sets.head()


# In[86]:


sets.tail()


# **Challenge**: In which year were the first LEGO sets released and what were these sets called?

# In[87]:


idx=sets.sort_values('year')['year'].idxmin()
sets['name'][idx]


# **Challenge**: How many different sets did LEGO sell in their first year? How many types of LEGO products were on offer in the year the company started?

# In[88]:


sets[sets['year']==1949].count()


# **Challenge**: Find the top 5 LEGO sets with the most number of parts. 

# In[89]:


sets.sort_values('num_parts',ascending=False).head()


# **Challenge**: Use <code>.groupby()</code> and <code>.count()</code> to show the number of LEGO sets released year-on-year. How do the number of sets released in 1955 compare to the number of sets released in 2019? 

# In[90]:


sets_by_year = sets.groupby('year').count()
sets_by_year['set_num']


# In[91]:


s1955=sets[sets['year']==1955].count()
s2019=sets[sets['year']==2019].count()
s2019['year']-s1955['year']


# **Challenge**: Show the number of LEGO releases on a line chart using Matplotlib. <br>
# <br>
# Note that the .csv file is from late 2020, so to plot the full calendar years, you will have to exclude some data from your chart. Can you use the slicing techniques covered in Day 21 to avoid plotting the last two years? The same syntax will work on Pandas DataFrames. 

# In[98]:


plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=16)
plt.ylabel('LEGO Sets', fontsize= 16)
plt.ylim(bottom=0,top=1000)

# reshaped = sets.pivot(columns='',index='year',values=sets.groupby('year').count())

plt.plot(sets_by_year.index,sets_by_year.set_num)


# ### Aggregate Data with the Python .agg() Function
# 
# Let's work out the number of different themes shipped by year. This means we have to count the number of unique theme_ids per calendar year.

# In[100]:


theme_by_year = sets.groupby('year').agg({'theme_id':pd.Series.nunique})
theme_by_year


# **Challenge**: Plot the number of themes released by year on a line chart. Only include the full calendar years (i.e., exclude 2020 and 2021). 

# In[102]:


plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=16)
plt.ylabel('LEGO Sets', fontsize= 16)
plt.ylim(bottom=0,top=100)
plt.plot(theme_by_year.index, theme_by_year.theme_id)


# ### Line Charts with Two Seperate Axes

# In[114]:


ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.plot(sets_by_year.index,sets_by_year.set_num,color='green')
ax2.plot(theme_by_year.index, theme_by_year.theme_id)
ax1.set_xlabel('Year')
ax1.set_ylabel('Sets',color='green')
ax2.set_ylabel('Themes')
ax1.set_ylim(0,1000)
ax2.set_ylim(0,100)


# **Challenge**: Use the <code>.groupby()</code> and <code>.agg()</code> function together to figure out the average number of parts per set. How many parts did the average LEGO set released in 1954 compared to say, 2017?

# In[123]:


parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean})
p1954 = sets[sets['year']==1954]['num_parts'].mean()
p2017 = sets[sets['year']==2017]['num_parts'].mean()
p2017-p1954


# ### Scatter Plots in Matplotlib

# **Challenge**: Has the size and complexity of LEGO sets increased over time based on the number of parts? Plot the average number of parts over time using a Matplotlib scatter plot. See if you can use the [scatter plot documentation](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.scatter.html) before I show you the solution. Do you spot a trend in the chart? 

# In[124]:


plt.scatter(parts_per_set.index,parts_per_set.num_parts)


# ### Number of Sets per LEGO Theme

# LEGO has licensed many hit franchises from Harry Potter to Marvel Super Heros to many others. But which theme has the largest number of individual sets? 

# In[133]:


set_theme_count = sets['theme_id'].value_counts()
set_theme_count = pd.DataFrame({'id':set_theme_count.index,'set_count':set_theme_count.values})
set_theme_count


# <img src="https://i.imgur.com/Sg4lcjx.png" width=1600>

# 

# ### Database Schemas, Foreign Keys and Merging DataFrames
# 
# The themes.csv file has the actual theme names. The sets .csv has <code>theme_ids</code> which link to the <code>id</code> column in the themes.csv. 

# **Challenge**: Explore the themes.csv. How is it structured? Search for the name 'Star Wars'. How many <code>id</code>s correspond to this name in the themes.csv? Now use these <code>id</code>s and find the corresponding the sets in the sets.csv (Hint: you'll need to look for matches in the <code>theme_id</code> column)

# In[127]:


themes = pd.read_csv('data/themes.csv')
themes[themes['name']=='Star Wars']


# In[132]:


# sets[sets.theme_id==18]
sets[sets.theme_id==209]


# ### Merging (i.e., Combining) DataFrames based on a Key
# 

# In[ ]:


merged = pd.merge(set_theme_count,themes,on='id')
merged


# In[ ]:


plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
plt.bar(merged.name[:15],merged.set_count[:15])

