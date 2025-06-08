#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector
import pandas as pd
import numpy as np
from mysql.connector import Error


# In[2]:


mydb = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  passwd = '',
  database = 'startup')



# In[3]:


df = pd.read_sql_query("select * from start", mydb)
df


# In[4]:


district = df["District"][0].upper()
year = df["Expected_Year"][0]
crop = df["Crop_type"][0]


# In[5]:


import pandas as pd
data = pd.read_csv("products.csv")


# In[26]:


tamil_nadu = data[data["State_Name"] == "Tamil Nadu"]
tamil_nadu


# In[27]:


dist_wise = tamil_nadu[tamil_nadu["District_Name"]== district]
dist_wise


# In[28]:


import warnings
warnings.filterwarnings('ignore')


# In[29]:


dist_wise.dropna(axis = 0, inplace = True)
len(dist_wise)


# In[30]:


dist_wise_1 = dist_wise[(dist_wise["Crop"] == 'Banana') | (dist_wise["Crop"] == 'Sugarcane') | (dist_wise["Crop"] == 'Turmeric') |
                     (dist_wise["Crop"] == 'Groundnut') | (dist_wise["Crop"] == 'Onion')]
dist_wise_1


# In[31]:


mean_1 = np.mean(dist_wise_1[dist_wise_1["Crop"]=='Banana'])[2]
mean_2 = np.mean(dist_wise_1[dist_wise_1["Crop"]=='Sugarcane'])[2]
mean_3 = np.mean(dist_wise_1[dist_wise_1["Crop"]== 'Groundnut'])[2]
mean_4 = np.mean(dist_wise_1[dist_wise_1["Crop"]=='Turmeric'])[2]
mean_5 = np.mean(dist_wise_1[dist_wise_1["Crop"]=='Onion'])[2]


# In[32]:


import plotly.graph_objects as go
import plotly
import matplotlib.pyplot as plt
import os

labels = ['Onion', 'Banana','Sugarcane','Groundnut','Turmeric']
values = [mean_5, mean_1, mean_2, mean_3, mean_4]


# Use `hole` to create a donut-like pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3, name=district,textfont=dict(
        family="sans serif",
        size=18,
        color="black"
    ))])

fig.update_layout(
    title_text=" TOP CULTIVATION OF " +district +" DISTRICT")


#fig.show()
plotly.offline.plot(fig, auto_open=False, filename=r'C:\wamp64\www\employee - Copy\images\pie', image='png')


# In[33]:


crop_wise = dist_wise[dist_wise["Crop"]==crop]
crop_wise


# In[34]:


from sklearn import linear_model
reg = linear_model.LinearRegression()
print(len(crop_wise))
X = crop_wise["Crop_Year"]
y = crop_wise["Production"]


# In[35]:


X = np.array(X).reshape(-1,1)


# In[36]:


reg.fit(X,y)
reg.score(X,y)


# In[37]:


year = int(year)
i = reg.predict(np.array([[year]]))
y= str(i[0])


# In[38]:








# In[40]:


cursor = mydb.cursor()
cursor.execute("update start set predicted ='"+y+"' where Search_id='1'")






