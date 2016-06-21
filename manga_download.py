
# coding: utf-8

# In[1]:

# Make sure all these libraries are installed before proceeding
import urlparse as prs
import urllib2
import os
from collections import namedtuple
import pdb


# In[2]:

def updateSite(site):
    site_parse = prs.urlparse(site)
    ext_parse = site_parse.path.split('.')
    num_parse = ext_parse[0].split('-')
    # update number
    num_parse[-1] = str(int(num_parse[-1]) + 1)
    ext_parse[0] = "-".join(num_parse)
    site_parse_asdict = site_parse._asdict()
    site_parse_asdict['path']= ".".join(ext_parse)
    updated_site = namedtuple('ParseResult', site_parse_asdict.keys())(**site_parse_asdict)
    updated_site = prs.urlunparse(updated_site)
    return updated_site


# In[3]:

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


# ## User Specific Data

# In[4]:

# Starting Image path on the server
site = "http://i8.mangareader.net/liar-game/1/liar-game-1846821.jpg"
# Folder to store the generated images
folder = 'ch1'
## Make the folder if it is not already made
try:
    os.makedirs(folder)
except:
    print("Folder already exists")
# Hardcoded number of images in each chapter
MAX_FILES = 224
count = 0


# In[ ]:

"""
Starts with the given site and updates the number in the filename in the image.
Check each filename until you reach the limit of the number of images in the chapter.
"""

while(count < MAX_FILES):
    req = urllib2.Request(site, headers=hdr)
    try:
        page = urllib2.urlopen(req)
        content = page.read()
        count+=1
        print(count)
        filename = os.path.join(folder,'%s-%03d.jpg'%(folder,count))
        with open(filename,'w') as fid:
            fid.write(content)
    except:
        pass
        
    # update the number in the site
    site = updateSite(site)

