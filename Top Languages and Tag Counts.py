#!/usr/bin/env python
# coding: utf-8

#Import libraries and packages
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
import matplotlib.style as style
from matplotlib import pyplot as mp
from IPython.core.display import Image, display
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
get_ipython().run_line_magic('matplotlib', 'inline')

#Download webpage content from stackoverflow
response = requests.get('https://stackoverflow.com/tags')
#Check whether the get request is successful
#200 means successful
#404 means unsuccessful
response.status_code

#Parsing webpage content into BeautifulSoup
soup = bs(response.content, 'html.parser')
#body tags
body = soup.find('body')
print(body)
type(body)

#Extract all the language links and place in a list
lang_tags = body.findAll('a', class_ = 'post-tag')
lang_tags[: 5]

#Extract language names 
languages = [i.text for i in lang_tags]
languages[: 5]

#Extract all the tag counts and place in a list
tag_counts = body.findAll('span', class_ = 'item-multiplier-count')
tag_counts[: 5]

#Extract number of tags
number_of_tags = [int(i.text) for i in tag_counts]
number_of_tags[:5]

#Concatenate the two lists
#Done using Pandas.DataFrame
df = pd.DataFrame({'Languages': languages, 'Tag Count': number_of_tags})
df.head()

#Plot the data
plt.figure(figsize = (10, 3))
plt.bar(height=df['Tag Count'][:10], x = df['Languages'][:10])
plt.xlabel('Languages')
plt.ylabel('Tag Counts')
plt.show()
