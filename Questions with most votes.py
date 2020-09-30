# Import libraries and packages
from bs4 import BeautifulSoup as bs
from matplotlib import pyplot as mp
from IPython.core.display import Image, display
from IPython.core.interactiveshell import InteractiveShell
import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
import matplotlib.style as style

InteractiveShell.ast_node_interactivity = "all"

get_ipython().run_line_magic('matplotlib', 'inline')

# Download webpage content from stackoverflow
# Top 50 questions
response = requests.get('https://stackoverflow.com/questions?sort=votes&pagesize=50')

# Check whether the get request is successful
# 200 means successful
# 404 means unsuccessful
response.status_code

# Parsing webpage content into BeautifulSoup
soup = bs(response.content, 
          'html.parser')
# body tags
body = soup.select_one('body')
print(body)
type(body)

# Extract all the question links
question_links = body.select("h3 a.question-hyperlink")

# Confirm there are 50 questions
print(len(question_links))
question_links[:5]

# Extract questions into a list
questions = [i.text for i in question_links]
questions[:5]

# Extract summaries links
summary_divs = body.select("div.excerpt")
print(len(summary_divs))
print(summary_divs[0])

# Extract all the questions
summaries = [i.text.strip() for i in summary_divs]
summaries[0]

# Extract tags per question
tags_divs = body.select("div.summary > div:nth-of-type(2)")
print(len(tags_divs))
tags_divs[0]

# Extract a tags in a list, grouped per question.
a_tags_list = [i.select('a') for i in tags_divs]

# Printing first question's a tags
a_tags_list[0]

#Extract tags names
tags = []

for a_group in a_tags_list:
    tags.append([a.text for a in a_group])

print(len(tags))
tags[:3]

# Number of votes
vote_spans = body.select("span.vote-count-post strong")
print(len(vote_spans))
print(vote_spans[:5])

# Extract vote counts
no_of_votes = [int(i.text) for i in vote_spans]
no_of_votes[:5]

# Number of answers
answer_divs = body.select("div.status strong")
print(len(answer_divs))
print(answer_divs[:5])

# Extract answer counts
no_of_answers = [int(i.text) for i in answer_divs]
no_of_answers[:5]

# Number of views
div_views = body.select("div.supernova")
print(len(div_views))
print(div_views[0])

# Extract views counts
no_of_views = [int(i) for i in no_of_views]
no_of_views[:5]

# Combining everything into a dataframe
df = pd.DataFrame({'Question': questions, 
                   'Summary': summaries, 
                   'Tags': tags,
                   'Number of votes': no_of_votes,
                   'Number of answers': no_of_answers,
                   'Number of views': no_of_views})

# Plot data
f, ax = plt.subplots(3, 1, figsize=(12, 8))

ax[0].bar(df.index, df.no_of_votes)
ax[0].set_ylabel('No of Votes')

ax[1].bar(df.index, df.no_of_views)
ax[1].set_ylabel('No of Views')

ax[2].bar(df.index, df.no_of_answers)
ax[2].set_ylabel('No of Answers')

plt.show()
