import random
# comment 0

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


while ans=="y" and deck <> []:  # comment 5
	pl+=deck.pop()
	comp+=deck.pop()
	print "You: ",pl\# comment 6
	print "Computer:\" # comment 7",comp
	print "# comment 8"
	print "\# comment 9"
	if deck <> []:
		ans=raw_input("Continue (y/n)? ")  # comment 10
	else:
		print "End!"
# x=input("Give a command... # Comment 11")

# comment 12
