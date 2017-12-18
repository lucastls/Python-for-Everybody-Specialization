import urllib
import json

url = raw_input('Enter location: ')

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

try: js = json.loads(str(data))
except: js = None

#print json.dumps(js, indent=4)

print "Count:",len(js["comments"])
sum=0
for num in range(len(js["comments"])):
    sum = sum + int(js["comments"][num]["count"])
print "Sum:",sum
