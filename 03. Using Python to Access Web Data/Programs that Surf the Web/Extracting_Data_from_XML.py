import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)

counts = tree.findall('.//count')
#print counts
print "Count:",len(counts)
sum=0
for i in range(len(counts)):
    sum = sum + int(counts[i].text)
print "Sum:",sum
