'''
Assignment 6.5

You can write any code you like in the window below. There are three files loaded and ready for you to open if you want to do file processing: "mbox-short.txt", "romeo.txt", and "words.txt".
'''
text = "X-DSPAM-Confidence: 0.8475"
pos=text.find('0')
number=float(text[pos:])
print number
