'''
Assignment 9.4

9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

auxlst=[]
dict={}

for line in handle:

  if line.startswith("From:"):
   continue

  if line.startswith("From"):
   auxlst=line.split()
   email=auxlst[1]

  if email in dict:
   dict[email]=dict[email]+1
  else:
   dict[email]=1

#print (dict)

m=max(dict.values())

for k,v in dict.items():
  if dict[k]==m:
   print(k,v)
