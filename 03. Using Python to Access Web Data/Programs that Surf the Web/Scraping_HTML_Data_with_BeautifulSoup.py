import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags "<span>-------<\span>"
tags = soup('span')

Numbers=[]
sum=0

for tag in tags:
  # Look at the parts of a tag
	"""
  print 'TAG:',tag
  print 'URL:',tag.get('href', None)
  print 'Contents:',tag.contents[0]
  print 'Attrs:',tag.attrs
	"""
	Numbers.append(tag.contents[0])
	sum=sum+int(tag.contents[0])

print "Count",len(Numbers)
print "Sum",sum
