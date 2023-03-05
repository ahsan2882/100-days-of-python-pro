#!/usr/bin/env python
# coding: utf-8

# # Introduction
#
# Do higher film budgets lead to more box office revenue? Let's find out if there's a relationship using the movie budgets and financial performance data that I've scraped from [the-numbers.com](https://www.the-numbers.com/movie/budgets) on **May 1st, 2018**.
#
# <img src=https://i.imgur.com/kq7hrEh.png>

# # Import Statements

# In[160]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from pandas.plotting import register_matplotlib_converters


# # Notebook Presentation

# In[161]:


pd.options.display.float_format = '{:,.2f}'.format

register_matplotlib_converters()


# # Read the Data

# In[162]:


data = pd.read_csv('cost_revenue_dirty.csv')


# # Explore and Clean the Data

# **Challenge**: Answer these questions about the dataset:
# 1. How many rows and columns does the dataset contain?
# 2. Are there any NaN values present?
# 3. Are there any duplicate rows?
# 4. What are the data types of the columns?

# In[163]:


data.shape


# In[164]:


data.isna().values.any()
data.duplicated().values.any()
data.info()


# ### Data Type Conversions

# **Challenge**: Convert the `USD_Production_Budget`, `USD_Worldwide_Gross`, and `USD_Domestic_Gross` columns to a numeric format by removing `$` signs and `,`.
# <br>
# <br>
# Note that *domestic* in this context refers to the United States.

# In[165]:


data.USD_Domestic_Gross = data.USD_Domestic_Gross.astype(
    str).str.replace(',', '')
data.USD_Domestic_Gross = data.USD_Domestic_Gross.astype(
    str).str.replace('$', '')
data.USD_Domestic_Gross = pd.to_numeric(data.USD_Domestic_Gross)
data.USD_Production_Budget = data.USD_Production_Budget.astype(
    str).str.replace('$', '')
data.USD_Production_Budget = data.USD_Production_Budget.astype(
    str).str.replace(',', '')
data.USD_Production_Budget = pd.to_numeric(data.USD_Production_Budget)
data.USD_Worldwide_Gross = data.USD_Worldwide_Gross.astype(
    str).str.replace('$', '')
data.USD_Worldwide_Gross = data.USD_Worldwide_Gross.astype(
    str).str.replace(',', '')
data.USD_Worldwide_Gross = pd.to_numeric(data.USD_Worldwide_Gross)


# **Challenge**: Convert the `Release_Date` column to a Pandas Datetime type.

# In[166]:


data.Release_Date = pd.to_datetime(data.Release_Date)
data


# ### Descriptive Statistics

# **Challenge**:
#
# 1. What is the average production budget of the films in the data set?
# 2. What is the average worldwide gross revenue of films?
# 3. What were the minimums for worldwide and domestic revenue?
# 4. Are the bottom 25% of films actually profitable or do they lose money?
# 5. What are the highest production budget and highest worldwide gross revenue of any film?
# 6. How much revenue did the lowest and highest budget films make?

# In[167]:


data.describe()


# # Investigating the Zero Revenue Films

# **Challenge** How many films grossed $0 domestically (i.e., in the United States)? What were the highest budget films that grossed nothing?

# In[168]:


zero_domestic = data[data.USD_Domestic_Gross == 0]
print(f'Number of films that grossed $0 domestically {len(zero_domestic)}')
zero_domestic.sort_values('USD_Production_Budget', ascending=False)


# **Challenge**: How many films grossed $0 worldwide? What are the highest budget films that had no revenue internationally?

# In[169]:


zero_worldwide = data[data.USD_Worldwide_Gross == 0]
print(f'Number of films that grossed $0 worldwide {len(zero_worldwide)}')
zero_worldwide.sort_values('USD_Production_Budget', ascending=False)


# ### Filtering on Multiple Conditions

# In[170]:


international_releases = data.loc[(data.USD_Domestic_Gross == 0) &
                                  (data.USD_Worldwide_Gross != 0)]
international_releases


# **Challenge**: Use the [`.query()` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html) to accomplish the same thing. Create a subset for international releases that had some worldwide gross revenue, but made zero revenue in the United States.
#
# Hint: This time you'll have to use the `and` keyword.

# In[171]:


international_releases = data.query(
    'USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')
print(f'Number of international releases: {len(international_releases)}')
international_releases.tail()


# ### Unreleased Films
#
# **Challenge**:
# * Identify which films were not released yet as of the time of data collection (May 1st, 2018).
# * How many films are included in the dataset that have not yet had a chance to be screened in the box office? 
# * Create another DataFrame called data_clean that does not include these films.

# In[172]:


# Date of Data Collection
scrape_date = pd.Timestamp('2018-5-1')


# In[173]:


future_releases = data[data.Release_Date >= scrape_date]
print(f"Number of unreleased movies:{len(future_releases)}")
future_releases


# In[174]:


data_clean = data.drop(future_releases.index)
data_clean


# ### Films that Lost Money
#
# **Challenge**:
# What is the percentage of films where the production costs exceeded the worldwide gross revenue? 

# In[175]:


money_losing = data_clean.loc[data_clean.USD_Production_Budget >
                              data_clean.USD_Worldwide_Gross]
len(money_losing)/len(data_clean)


# # Seaborn for Data Viz: Bubble Charts

# In[176]:


sns.scatterplot(data=data_clean,
                x='USD_Production_Budget',
                y='USD_Worldwide_Gross')
plt.figure(figsize=(8, 4), dpi=200)

ax = sns.scatterplot(data=data_clean,
                     x='USD_Production_Budget',
                     y='USD_Worldwide_Gross')

ax.set(ylim=(0, 3000000000),
       xlim=(0, 450000000),
       ylabel='Revenue in $ billions',
       xlabel='Budget in $100 millions')

plt.show()


# ### Plotting Movie Releases over Time
#
# **Challenge**: Try to create the following Bubble Chart:
#
# <img src=https://i.imgur.com/8fUn9T6.png>
#
#

# In[177]:


plt.figure(figsize=(8, 4), dpi=200)
ax = sns.scatterplot(data=data_clean,
                     x='USD_Production_Budget',
                     y='USD_Worldwide_Gross',
                     hue='USD_Worldwide_Gross',  # colour
                     size='USD_Worldwide_Gross',)  # dot size

ax.set(ylim=(0, 3000000000),
       xlim=(0, 450000000),
       ylabel='Revenue in $ billions',
       xlabel='Budget in $100 millions',)

plt.show()


# In[178]:


plt.figure(figsize=(8, 4), dpi=200)

# set styling on a single chart
with sns.axes_style('darkgrid'):
    ax = sns.scatterplot(data=data_clean,
                         x='Release_Date',
                         y='USD_Production_Budget',
                         hue='USD_Worldwide_Gross',
                         size='USD_Worldwide_Gross')

    ax.set(xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
           ylim=(0, 450000000),
           xlabel='Year',
           ylabel='Budget in $100 millions')


# # Converting Years to Decades Trick
#
# **Challenge**: Create a column in `data_clean` that has the decade of the release.
#
# <img src=https://i.imgur.com/0VEfagw.png width=650>
#
# Here's how:
# 1. Create a [`DatetimeIndex` object](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DatetimeIndex.html) from the Release_Date column.
# 2. Grab all the years from the `DatetimeIndex` object using the `.year` property.
# <img src=https://i.imgur.com/5m06Ach.png width=650>
# 3. Use floor division `//` to convert the year data to the decades of the films.
# 4. Add the decades as a `Decade` column to the `data_clean` DataFrame.

# In[179]:


dt_index = pd.DatetimeIndex(data_clean.Release_Date)
decades = (dt_index.year // 10)*10
data_clean['Decade'] = decades


# In[179]:


# ### Separate the "old" (before 1969) and "New" (1970s onwards) Films
#
# **Challenge**: Create two new DataFrames: `old_films` and `new_films`
# * `old_films` should include all the films before 1969 (up to and including 1969)
# * `new_films` should include all the films from 1970 onwards
# * How many films were released prior to 1970?
# * What was the most expensive film made prior to 1970?

# In[180]:


old_films = data_clean[data_clean.Decade <= 1960]
new_films = data_clean[data_clean.Decade > 1960]
old_films.describe()
idx = old_films.USD_Production_Budget.idxmax()
old_films.loc[idx]


# # Seaborn Regression Plots

# In[181]:


plt.figure(figsize=(8, 4), dpi=200)
with sns.axes_style("whitegrid"):
    sns.regplot(data=old_films,
                x='USD_Production_Budget',
                y='USD_Worldwide_Gross',
                scatter_kws={'alpha': 0.4},
                line_kws={'color': 'black'})


# **Challenge**: Use Seaborn's `.regplot()` to show the scatter plot and linear regression line against the `new_films`.
# <br>
# <br>
# Style the chart
#
# * Put the chart on a `'darkgrid'`.
# * Set limits on the axes so that they don't show negative values.
# * Label the axes on the plot "Revenue in \$ billions" and "Budget in \$ millions".
# * Provide HEX colour codes for the plot and the regression line. Make the dots dark blue (#2f4b7c) and the line orange (#ff7c43).
#
# Interpret the chart
#
# * Do our data points for the new films align better or worse with the linear regression than for our older films?
# * Roughly how much would a film with a budget of $150 million make according to the regression line?

# In[182]:


plt.figure(figsize=(8, 4), dpi=200)
with sns.axes_style('darkgrid'):
    ax = sns.regplot(data=new_films,
                     x='USD_Production_Budget',
                     y='USD_Worldwide_Gross',
                     color='#2f4b7c',
                     scatter_kws={'alpha': 0.3},
                     line_kws={'color': '#ff7c43'})

    ax.set(ylim=(0, 3000000000),
           xlim=(0, 450000000),
           ylabel='Revenue in $ billions',
           xlabel='Budget in $100 millions')


# # Run Your Own Regression with scikit-learn
#
# $$ REV \hat ENUE = \theta _0 + \theta _1 BUDGET$$

# In[187]:


regression = LinearRegression()
X = pd.DataFrame(new_films, columns=['USD_Production_Budget'])
y = pd.DataFrame(new_films, columns=['USD_Worldwide_Gross'])
regression.fit(X, y)
regression.intercept_
regression.coef_
regression.score(X, y)


# **Challenge**: Run a linear regression for the `old_films`. Calculate the intercept, slope and r-squared. How much of the variance in movie revenue does the linear model explain in this case?

# In[190]:


X = pd.DataFrame(old_films, columns=['USD_Production_Budget'])
y = pd.DataFrame(old_films, columns=['USD_Worldwide_Gross'])
regression.fit(X, y)

regression.coef_


# In[192]:


regression.intercept_
regression.score(X, y)


# # Use Your Model to Make a Prediction
#
# We just estimated the slope and intercept! Remember that our Linear Model has the following form:
#
# $$ REV \hat ENUE = \theta _0 + \theta _1 BUDGET$$
#
# **Challenge**:  How much global revenue does our model estimate for a film with a budget of $350 million?

# In[193]:


budget = 350000000
revenue_estimate = regression.intercept_[0] + regression.coef_[0, 0]*budget
revenue_estimate = round(revenue_estimate, -6)
print(
    f'The estimated revenue for a $350 film is around ${revenue_estimate:.10}.')


# In[183]:
