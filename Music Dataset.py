#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


songs_data=pd.read_csv('C:/Users/Cyntexia/Downloads/archive (2)/songs.csv')
songs_data.head()


# In[3]:


songs_data.info()


# In[4]:


songs_data.describe()


# In[5]:


import matplotlib.pyplot as plt
songs_data.hist(bins=50, figsize=(20,15))
plt.show()


# In[6]:


songs_data.plot(kind="scatter", y="Artist", x="Popularity", alpha=0.1)


# In[7]:


songs_data.nlargest(799, 'Popularity', keep='last')


# In[19]:


songs_data = songs_data.loc[songs_data["Popularity"] >90 ]


# In[20]:


songs_data


# In[21]:


songs_data.describe()


# In[39]:


songs_data.plot(kind="scatter", y="Artist", x="Popularity", alpha=0.1)


# In[43]:


from matplotlib.ticker import PercentFormatter
color1 = 'blue'
color2 = 'purple'
line_size = 6

fig, ax = plt.subplots()
ax.bar(songs_data.index, songs_data['Artist'], color=color1)


ax2 = ax.twinx()
ax2.plot(songs_data.index, songs_data['Popularity'], color=color2, marker="D", ms=line_size)
ax2.yaxis.set_major_formatter(PercentFormatter())


ax.tick_params(axis='y', colors=color1)
ax2.tick_params(axis='y', colors=color2)


plt.show()


# In[ ]:




