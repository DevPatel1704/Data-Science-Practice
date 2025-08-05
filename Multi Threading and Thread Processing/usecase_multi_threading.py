'''
Real world example : multithreading for uo bound tasks 
Scenario : Web Sacaping
Web Scraping often involves making numerous network requests to 
fetch web pages.
These tasks are I/O bound because they spend lot of ime waiting
for responases from servers.
multithreading can significantly 
imporve the performance by allowing multiple web pages to be 
fetched concerrently.

'''

# https://python.langchain.com/v0.2/docs/introduction/


# https://python.langchain.com/v0.2/docs/concepts/


# https://python.langchain.com/v0.2/docs/tutorials/




import threading
import requests
from bs4 import BeautifulSoup

urls=[
    
    
'https://python.langchain.com/v0.2/docs/introduction/',

'https://python.langchain.com/v0.2/docs/concepts/' ,

'https://python.langchain.com/v0.2/docs/tutorials/'
]


def fetch_content(url):
    responce=requests.get(url)
    soup=BeautifulSoup(responce.content,'html.parser')
    print(f'Fecthed {len(soup.text)} characters from {url}')
    
    
threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
    
print("All Web pages fetched")