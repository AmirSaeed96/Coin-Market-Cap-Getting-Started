#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import coinmarketcapapi
import pandas as pd


# In[3]:


type(pd)


# In[4]:


cmc = coinmarketcapapi.CoinMarketCapAPI('Your API Key')


# In[5]:


## Bitcoin Info
data = cmc.cryptocurrency_info(symbol='BTC')
data


# In[6]:


## List of Cyrptocurrencies and their symbols
data_id_map = cmc.cryptocurrency_map()
data_id_map


# In[7]:


data_id_df = pd.DataFrame(data_id_map.data, columns =['name','symbol'])
data_id_df.set_index('symbol',inplace=True)
print(data_id_df)


# In[8]:


## Quote for individual cryptocurrency
data_quote = cmc.cryptocurrency_quotes_latest(symbol='ETH', convert='USD')


# In[9]:


data_quote


# In[10]:


data_listing = cmc.cryptocurrency_listings_latest()
data_listing


# In[11]:


data_listing.data


# In[12]:


for x in data_listing.data:
    print(x)
    print(x.get('name'))
    print(x.get('symbol'))
    print(x.get('quote', {}).get('USD', {}).get('price'))
    print(x.get('quote', {}).get('USD', {}).get('last_updated'))


# In[13]:


data_listing_df = pd.DataFrame(columns = ['Name', 'Symbol', 'Price_USD', 'Date'])
data_listing_df


# In[14]:


pd.DataFrame([[data_listing.data[0].get('name'), data_listing.data[0].get('symbol'), data_listing.data[0].get('quote', {}).get('USD', {}).get('price'), data_listing.data[0].get('quote', {}).get('USD', {}).get('last_updated')]])


# In[15]:


for x in data_listing.data:
    #print([[x.get('name'), x.get('symbol'), x.get('quote', {}).get('USD', {}).get('price'), x.get('quote', {}).get('USD', {}).get('last_updated')]])
    df2 = pd.DataFrame([[x.get('name'), x.get('symbol'), x.get('quote', {}).get('USD', {}).get('price'), x.get('quote', {}).get('USD', {}).get('last_updated')]], columns = ['Name', 'Symbol', 'Price_USD', 'Date'])
    data_listing_df = data_listing_df.append(df2)

data_listing_df = data_listing_df.reset_index()


# In[17]:


pd.DataFrame.to_csv(data_listing_df, 'name_symbol_price.csv')


# In[ ]:





# In[ ]:




