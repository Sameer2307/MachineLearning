
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



routes = pd.read_sql_query("""
                           select cast(sa.longitude as float) as source_lon, 
                           cast(sa.latitude as float) as source_lat,
                           cast(da.longitude as float) as dest_lon,
                           cast(da.latitude as float) as dest_lat
                           from routes 
                           inner join airports sa on
                           sa.id = routes.source_id
                           inner join airports da on
                           da.id = routes.dest_id;
                           """, 
                           conn)
m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')
m.drawcoastlines()
for name, row in routes[:3000].iterrows():
    if abs(row["source_lon"] - row["dest_lon"]) < 90:
        # Draw a great circle between source and dest airports.
        m.drawgreatcircle(
            row["source_lon"], 
            row["source_lat"], 
            row["dest_lon"],
            row["dest_lat"],
            linewidth=1,
            color='b'
        )