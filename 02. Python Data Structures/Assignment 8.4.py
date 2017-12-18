'''
Assignment 8.4

8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.pythonlearn.com/code/romeo.txt
'''

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
auxlst=[]
i=0

for line in fh:
  line.rstrip()
  auxlst=line.split()

  for i in range(0,len(auxlst)):
  aux=auxlst[i]
  if aux not in lst:
  lst.append(aux)
  else:
  continue

lst.sort()
print lst
