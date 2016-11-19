
# coding: utf-8

# In[ ]:

import pywikibot
import pywikibot.pagegenerators


# In[ ]:

pywikibot.__version__


# In[ ]:

pywikibot.__release__


# In[ ]:

site = pywikibot.Site('id', 'wikipedia')


# In[22]:

board = site.load_board("Wikipedia:Warung Kopi (Bantuan)")


# In[47]:

topic_list = site.load_topiclist("Wikipedia:Warung Kopi (Bantuan)",
                                 format='wikitext',
                                 limit=100,
                                 sortby='newest',
                                 toconly=False,
                                 offset=None,
                                 offset_id="t6wi2jcry4hrbsny",
                                 reverse=False,
                                 include_offset=False)

# In[49]:

import json
with open("topic_list3.json", "w") as f:
    f.write(json.dumps(topic_list))

