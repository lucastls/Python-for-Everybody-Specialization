import urllib
from BeautifulSoup import *

url = "http://python-data.dr-chuck.net/known_by_Koden.html"#raw_input('Enter - ')
count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: '))-1

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
# Retrieve all of the anchor tags
tags = soup('a')

Names=[]
aux=0
link=tags[position].get('href', None)

title = soup.title.contents
title=title[0].split()
name=title[2]
Names.append(name)

print "Retrieving:",url

while aux<count:
	print "Retrieving:",link
	url = link
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	link=tags[position].get('href', None)
	title = soup.title.contents
	title=title[0].split()
	name=title[2]
	Names.append(name)
	aux+=1

print Names[-1]
