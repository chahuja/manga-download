
# coding: utf-8

# In[ ]:

# Make sure all these libraries are installed before proceeding
import urlparse as prs
import urllib2
import os
from collections import namedtuple
import pdb
from bs4 import BeautifulSoup


# In[ ]:

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


# ## User Specific Data

# In[ ]:

# Starting html path of the manga
site = "http://www.mangareader.net/death-note/1/1"
# Folder to store the generated images
folder = 'dn'
## Make the folder if it is not already made
try:
    os.makedirs(folder)
except:
    print("Folder already exists")
# Hardcoded number of chapters
MAX_CHAP = 109
chap = 1
ep = 1


# In[ ]:

"""
Starts with the given site and updates the number in the filename in the image.
Check each filename until you reach the limit of the number of images in the chapter.
"""

site_base = '/'.join(site.split('/'))[:-3]

for chap in range(1,MAX_CHAP+1):
    ep = 1
    while(1):
        # update numbers in the site
        site = os.path.join(site_base,str(chap),str(ep))
        # Read the html page with the image
        req = urllib2.Request(site, headers=hdr)
        try:
            page = urllib2.urlopen(req)
            content = page.read()
            soup = BeautifulSoup(content, 'html.parser')
            for link in soup.find_all('img'):
                url = link.get('src')

            # Read the image url to get the content of the image
            req = urllib2.Request(url, headers=hdr)
            page = urllib2.urlopen(req)
            content = page.read()
            try:
                os.makedirs(os.path.join(folder,'%s-%03d'%(folder,chap)))
            except:
                pass
            filename = os.path.join(folder,'%s-%03d'%(folder,chap),'%s-%03d-%03d.jpg'%(folder,chap,ep))
            ep+=1
            with open(filename,'w') as fid:
                fid.write(content)
        except:
            break
    print(chap)    

