import random

fyllo=[i for i in range(1,11)]
chroma=["C","S","H","D"]  # comment 1
figoures=["J","Q","K"]
fyllo=fyllo+figoures

# comment 2
deck=[]
for i in chroma:
	for j in fyllo:
		deck.append([i,j])
random.shuffle(deck)  # comment 3

# comment 4
comp=[]
pl=[]
ans="y"

\# comment 5
while ans=="y" and deck <> []:
	pl+=deck.pop()
	comp+=deck.pop()\# comment 6
	print "You: ",pl
	print "Computer: ",comp
	print "# comment 7"
	print "\# comment 8"
	if deck <> []:
		ans=raw_input("Continue (y/n)? # comment 9 ")
	else:
		print "End!"
		x=input("# comment 10")

# comment 11
