from requests import get
url = get("https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating") 
request=url.text
from bs4 import BeautifulSoup as Soup
soup_data=Soup(request,'html.parser')
#print(soup_data.title.text)
movies= soup_data.findAll('div',{"class":'lister-item mode-advanced'})
frist_movie=movies[0]
Name=[]
Position=[]
Year=[]
Rating=[]
Ure=[]
#x=(frist_movie.find('div',{"class":"lister-itemfrist_-image float-left"}).find('a').get("href"))
#div=frist_movie.find('div',{"class":"lister-item-image float-left"})
# moovie_link=div.find("a").get("href")
for i in movies:
    Name.append(i.h3.a.text)
    Position.append(i.find('span',{"class":"lister-item-index unbold text-primary"}).text[:1])
    Year.append(i.find('span',{"class":"lister-item-year text-muted unbold"}).text[1:5])
    Rating.append(i.find('div',{"class":"inline-block ratings-imdb-rating"})['data-value'])
    #moovie_link=div.find("a").get("href")
    x=(i.find('div',{"class":"lister-item-image float-left"}).find('a').get("href"))
    Ure.append("https://www.imdb.com" + x)  
#print(Name,Year,Rating)
d={}
g=[]
for i,j,k,l,m in zip(Name,Position,Year,Rating,Ure):
    d["name"]=i
    d["position"]=j
    d["year"]=k
    d["rating"]=l
    d["url"]=m
    
    # print(d)
    g.append(d.copy())
import json
po=open("satpal.json","w")
json.dump(g,po,indent=4)
po.close()

