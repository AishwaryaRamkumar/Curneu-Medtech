
# coding: utf-8

# In[9]:


import pandas as pd
data=pd.read_csv("C:/Users/Aishwarya/Desktop/curneu/User1data.csv")


# In[10]:


df=pd.DataFrame(data)
#df[df.columns[4:6]]


# In[17]:


data.dropna(inplace=True)
new=data["Recommended"].str.split("(",n=1,expand=True)
data["x"]=new[0]
data["y"]=new[1]
data.drop(columns=["x"],inplace=True)
#data.drop(columns=["Recommended"],inplace=True)
data


# In[14]:


#data.drop(columns=["x"],inplace=True)
data


# In[11]:




