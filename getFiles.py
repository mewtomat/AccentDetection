from HTMLParser import HTMLParser
import requests
from htmlentitydefs import name2codepoint
import urllib
import wget
# wget.download('url')


printLiItem = False

class MyHTMLParser(HTMLParser):
	# def __init__ (self):
	# 	HTMLParser.__init__(self)
	# 	self.printli = False
	# 	self.printul = False
	# 	self.counter = 1078
	# 	self.aok = True
	# 	self.emok = True
	# 	self.

	def handle_starttag(self, tag, attrs):
		if tag == "source":
			# print self.counter, attrs[1][1]
			print attrs[1][1]
			# urllib.urlretrieve(attrs[1][1],str(self.counter)+".mp3")
			wget.download(attrs[1][1])
			# self.counter = self.counter+1
		# if tag == 'ul':
		# 	if attrs[0][1] =='bio':
		# 		self.printul = True

	# def handle_endtag(self, tag):
	# 	if tag == 'ul':
	# 		self.printul = False

	# def handle_data(self, data):
	# 	if (self.printul is True):
	# 		file = open(str(self.counter)+".meta","aw")
	# 		file.write(data)
	# 		file.close()


parser = MyHTMLParser()
for i in range(0,2368):
	parser.feed(requests.get("http://accent.gmu.edu/searchsaa.php?function=detail&speakerid=" + str(i)).text)