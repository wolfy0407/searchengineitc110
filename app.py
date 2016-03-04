from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
#oking the word "how" in the index (We can search for any keyword, just for demonstration I am using how). The Look_up function helps us in our later task returning a list of urls that contain our keyword.
def Look_up(index,keyword):#This function is for given an index, it finds the keyword in the index and returns the list of links
 f=[]
 for i in index:
  if i[0]==keyword:
   for j in i[1]:
    f.append(j)
 return f
#The format of element in the index is <keyword>,[<List of urls that contain the keyword>]
def add_to_index(index,url,keyword):
 for i in index:
  if keyword==i[0]:
   i[1].append(url)
   return
 index.append([keyword,[url]])
def add_page_to_index(index,url,content):#Adding the content of the webpage to the index
 for i in content.split():
  add_to_index(index,url,i)
 
def Crawl_web(seed):#The website to act as seed page is given as input
 tocrawl=[seed]
 crawled=[]
 index=[]
 while tocrawl:
  p=tocrawl.pop()
  if p not in crawled:#To remove the looping, if a page is already crawled and it is backlinked again by someother link we are crawling, we need not crawl it again
   c=get_page(p)
   add_page_to_index(index,p,c)
   union(tocrawl,get_all_links(c))
   crawled.append(p)#As soon as a link is crawled it is appended to crawled. In the end when all the links are over, we will return the crawled since it contains all the links we have so far
 return crawled,index #Returns the list of links
crawled,index=Crawl_web('http://xkcd.com/353')#printing all the links
#print index 
print Look_up(index,"how")#We are looking for the keyword "how" in the index
 


if __name__ == '__main__':
    # gets Heroku's suggested port out of the environment dictionary if exists:
    port = int(os.environ.get('PORT', 5000))
    # this is the wsgi hook:
    app.run(host='0.0.0.0', port=port)
