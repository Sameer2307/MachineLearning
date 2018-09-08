
# coding: utf-8

# In[1]:

import sqlite3


# In[2]:

conn = sqlite3.connect("D:\\hackveda\\flights.db")


# In[3]:

# now we will create a cursor so that we can perform sql queries
cur = conn.cursor()


# In[4]:

cur.execute("select * from airlines limit 5;")
results = cur.fetchall()
print (results)


# In[5]:

#mapp our dataset- airports 
#generate a graph


# In[6]:

coordinates = cur.execute("select cast(longitude as float), cast(latitude as float) from airports;").fetchall()
print(coordinates)

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
%matplotlib inline

# In[7]:

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat =80, llcrnrlon =-180, urcrnrlon =180, lat_ts=20, resolution ='c')

m.drawcoastlines()
m.drawmapboundary()


x,y = m([l[0] for l in coordinates], [l[1] for l in coordinates])

m.scatter(x,y, marker='o', color ='red')


# In[8]:

import pandas as pd


# In[9]:

df = pd.read_sql_query("select * from airlines limit 5;",conn)


# In[10]:

print(df)


# In[11]:

df['country']


# In[12]:

df.head(3)


# In[13]:

df.tail(3)


# In[14]:

df.columns


# In[16]:

# inserting rows using pandas

#cur = conn.cursor()
cur.execute("insert into airlines values (6048, 19846, 'Testflight', '','','',null,null,'y');" )
#commit the transactions
conn.commit()
pd.read_sql_query("select * from airlines where id = 19846;",conn)


# In[ ]:



