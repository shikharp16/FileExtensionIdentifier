#Program to fetch info about different file extensions from web
# Author : Shikhar Pahadia 

#for sending HTTP requests
import requests as req 

#for scraping the file descriptions from the web resources
from bs4 import BeautifulSoup 

#input the extension
t = raw_input("Type your extension : ")
#t='cpp'
"""
RESOURCE 1:
URL: https://www.file-extensions.org/'raw_input(file_extension)'/-file-extension

"""
print("Description from Source 1")
print("Description from Source 1")
print("")
try:
	#sending HTTP requests after generating url as per the above mentioned scheme
	r1 = req.get("https://www.file-extensions.org/"+t+"-file-extension")
	c1 = r1.content

	#Scraping required description of the input extension 
	#from the generated url and printing them
	soup1 = BeautifulSoup(c1,"html.parser")
	res = soup1.find_all("div",{"id":"extdesc"})[0].text if soup1.find("div",{"id":"extdesc"}) else 'Invalid Extension'
	print(res)
except req.exceptions.RequestException as e: 
    print(e)
print("")


"""
RESOURCE 2
URL:https://file.org/extension/input(file_extension)

"""
print("Description from Source 2")
print("")

try:
	#sending HTTP requests after generating url as per the above mentioned scheme
	r2 = req.get("https://file.org/extension/"+t)
	c2 = r2.content

	#Scraping required description of the input extension 
	#from the generated url and printing them
	soup2 = BeautifulSoup(c2,"html.parser")
	F2 = soup2.find_all("div",{"class":"purpose"})
	for i in F2[0].find_all("p"):
		print((i.text))
except req.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
print("")



"""
RESOURCE 2
URL:https://fileinfo.com/extension/input(file_extension)

"""
print("Description from Source 3")
print("")
#For accessing a restricted URL
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

try:
	#sending HTTP requests after generating url as per the above mentioned scheme
	r3 = req.get("https://fileinfo.com/extension/"+t,headers=agent)
	c3 = r3.content

	#Scraping required description of the input extension 
	#from the generated url and printing them
	soup3 = BeautifulSoup(c3,"html.parser")
	F31 = soup3.find_all("td",{"class":"platform"})
	F32 = soup3.find_all("table",{"class":"apps"})
	F33 = soup3.find_all("span",{"class":"fileType"})
	F34 = soup3.find_all("table",{"class","headerInfo"})
	if F34 is not None and len(F34) > 0:
		info = F34[0].find_all("tr") 
		for x in info:
			if x != info[1]:
				print((x.text))
		print("")
		print(("Programs that open "+t+" files"))
		print("")
		for i,j in zip(F31,F32):
				print(i.text,j.text)
	else:
		print("Invalid Extension")
except req.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
print("")


