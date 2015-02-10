import urllib

def saveHtml(url):
	# Saving raw html data	
	opener = urllib.FancyURLopener({})
	f = opener.open(url)
	content = f.read()
	file = open("raw_data.txt","wb")
	file.writelines(content)
	file.close()
	return