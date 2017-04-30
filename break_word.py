import sys

int2type={}
wordbnd=open(sys.argv[1],"r+")
for line in wordbnd:
	words = line.split(' ')
	words = [word.strip() for word in words]
	int2type[words[0]] = words[1]
wordbnd.close()

ali=open(sys.argv[2],"r+")
beginTime=0
for line in ali:
	words = line.split(' ')
	words = [word.strip() for word in words]
	category=int2type[words[2]]
	if category == "singleton":
		print words[0], words[1]
	elif category== "begin":
		beginTime=float(words[0])
	elif category =="end":
		endTime=float(words[0])
		duration=float(words[1])
		endTime = endTime+duration
		duration=endTime-beginTime
		print beginTime, duration
ali.close()