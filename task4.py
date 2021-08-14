import os,json,requests,task1
from bs4 import BeautifulSoup
from pprint import pprint

def movie_details(link):

	# if os.path.exists("/home/navgurukul/Desktop/rAju/data/aanand.json"):
	# 	with open("/home/navgurukul/Desktop/rAju/data/aanand.json") as file:
	data=requests.get(link).text

	# data0=file.read()
	genre_lst=[]
	director_lst=[]

	data=BeautifulSoup(data,"html.parser")
	name=data.find(class_="title_wrapper").h1.text
	timeClass=data.find(class_="title_wrapper")
	time=(timeClass.find(class_="subtext").time.text).strip()
	genre_class=timeClass.find(class_="subtext")
	genre_a=genre_class.find_all("a")
	for i in range(len(genre_a)-1):
		genre_lst.append(genre_a[i].text)

	bio=data.find(class_="summary_text").text
	director_class=data.find(class_="credit_summary_item")
	director_a=director_class.find_all("a")
	for i in range(len(director_a)):
		director_lst.append(director_a[i].text)
	link=data.find(class_="poster").img["src"]
	exta_details=data.find("div",attrs={"class":"article","id":"titleDetails"})
	txt_div=exta_details.find_all("div",class_="txt-block")
	count=0
	for div in txt_div:
		if count==2:
			break

		elif div.h4.text== "Country:":
			country_all= div.find_all("a")
			country=[a.text for a in country_all]
			count+=1
		elif div.h4.text=="Language:":
			language_all=div.find_all("a")
			language=[a.text for a in language_all]
			count+=1
		

	

		
	s={}
	s["name"]=name[:-8]
	s["country"]="india"
	s["genre"]=genre_lst
	s["running_time"]=int(time[0])*60+int(time[3])
	s["minfo"]=bio.strip()
	s["director"]=director_lst
	s["poster_link"]=link
	s["language"]=language
	s["country"]=country

	return s

	# else:
	# 	data0=requests.get(link).text
	# 	with open("/home/navgurukul/Desktop/rAju/data/aanand.json","w") as file:
	# 		file.write(data0)


movies_list=task1.top_250movies()
x=int(input("movie_serial_no:_"))
mDic=movies_list[x-1]
pprint(movie_details(mDic["link"]))