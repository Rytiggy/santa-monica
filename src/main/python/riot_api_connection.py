
# coding: utf-8

# In[34]:


import requests

my_api_key = "RGAPI-9c2b1602-ebbe-4c9e-8068-8698ca534623"
summoner_miss = 'Miss'
summoner_slayre = 'Slayre'
summoner_by_name = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key=".format(summoner_slayre)


# In[35]:


full_endpoint = summoner_by_name + my_api_key
full_endpoint


# In[36]:


response = requests.get(full_endpoint)


# In[27]:


type(response)


# In[37]:


my_summoner_info = response.json()
my_summoner_info['id']


# In[31]:


my_summoner_info['id']

