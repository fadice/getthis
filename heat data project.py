#!/usr/bin/env python
# coding: utf-8

# In[130]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import researchpy as rp


# In[131]:


heat_trainner = pd.read_csv("c:/users/fadic/anaconda3/Library/lib/Untitled Folder/heat_trainner.csv")
# printing the first 5 rows of dataset
heat_trainner.head()


# In[132]:


# getting the columns of the dataset
columns = list(heat_trainner.columns)
columns


# In[159]:


# check datatype in each column
print("Column datatypes: ")
print(heat_trainner.dtypes)


# In[ ]:





# In[160]:


# Loading the dataset

numeric_col = ['heat_group', 'heat_stroke', 'heat_syn_cramps', 'heat_exh', 'heat_other', 'RHABDO', 'HYPONATREMIA', 'AGE_GROUP',
               'LOS', 'RACE_CODE']
 
#Using Correlation analysis to depict the relationship between the numeric/continuous data variables
corr = heat_trainner.loc[:,numeric_col].corr()
print(corr)


# In[134]:


# names of the columns
columns = ['DX1', 'DX2', 'DX3', 'DX4', 'Diagnosis__Admitting']

# looping through the columns to fill the entries with NaN values with ""
for column in columns:
    heat_trainner[column] = heat_trainner[column].fillna("")


# In[135]:


# printing the first 5 rows of dataset
heat_trainner.head()


# In[136]:


# names of the columns
columns = ['heat_stroke', 'heat_syn_cramps', 'heat_exh', 'heat_other', 'RHABDO','HYPONATREMIA','Death_Indicator']

# looping through the columns to fill the entries with NaN values with ""
for column in columns:
   heat_trainner[column] = heat_trainner[column].fillna(0)


# In[59]:


# names of the columns
columns = ['heat_stroke', 'heat_syn_cramps', 'heat_exh', 'heat_other', 'RHABDO','HYPONATREMIA','Death_Indicator']

# looping through the columns to fill the entries with NaN values with ""
for column in columns:
    heat_trainner[column] = heat_trainner[column].format(1)


# In[72]:


formatted_number = round(number, 0)
print(formatted_number)


# In[137]:


# printing the first 5 rows of dataset
heat_trainner.head()


# In[138]:


pd.crosstab(index=heat_trainner['LOS'], columns=heat_trainner['AGE_GROUP'])


# In[143]:


contigency = pd.crosstab(heat_trainner['LOS'], heat_trainner['AGE_GROUP'] )
contigency


# In[144]:


# Chi-square test of independence.
c, p, dof, expected = chi2_contingency(contigency)
p


# In[85]:


pd.crosstab(index=heat_trainner['AGE_GROUP'], columns=heat_trainner['RACE_CODE'])


# In[86]:


pd.crosstab(index=heat_trainner['AGE_GROUP'], columns=heat_trainner['WORK_POSITION'])


# In[109]:


from scipy.stats import chi2_contingency
 
# defining the table
stat, p, dof, expected = chi2_contingency(heat_trainner)
 
# interpret p-value
alpha = 0.05
print("p value is " + str(p))
if p <= alpha:
    print('Dependent (reject H0)')
else:
    print('Independent (H0 holds true)')


# In[161]:


stats.ttest_ind(heat_trainner['heat_stroke'][heat_trainner['SEX'] == 1 ],
                heat_trainner['heat_stroke'][heat_trainner['SEX'] == 2 ])


# In[162]:


rp.ttest(group1= heat_trainner['heat_stroke'][heat_trainner['SEX'] == 1], group1_name= "Male",
         group2= heat_trainner['heat_stroke'][heat_trainner['SEX'] == 2], group2_name= "Female")


# In[164]:


summary, results = rp.ttest(group1= heat_trainner['heat_stroke'][heat_trainner['SEX'] == 1], group1_name= "Male",
                            group2= heat_trainner['heat_stroke'][heat_trainner['SEX'] == 2], group2_name= "Female")
print(summary)


# In[165]:


print(results)


# In[184]:


random={1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5}


# In[185]:


random.head()


# In[177]:


x=2
y=3

#print('x =', x)

#b. print('Value of', x, '+', x, 'is', (x + x))

#c. print('x =')

#d. print((x + y), 'x =', (y + x))


# In[178]:


random.head()


# In[ ]:




