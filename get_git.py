'''
Name: Syed Sumair Zafar
Id  : 7099347
'''

# Modules Requirements
# module: BeautifulSoup
# module: gitpython
# module: urllib

from BeautifulSoup import BeautifulSoup
from functions import saveHtml
from git import Repo
import shutil
import stat
import urllib
import sys
import os
import re

	
count = len(sys.argv)

if (count > 1):
	configFile = sys.argv[1]
			
	# reading config file variables
	vars = [];
	with open(configFile) as fp:
		for line in fp:
			config_data = line.split(' = ')
			vars.append(config_data[1])
			
	url = vars[0]	
	rootDirectory = vars[1]
	links = []
		
	if "github.com" in url:
		if(len(url.split("/")) < 6 and len(url.split("/")) > 4):
			saveHtml(url) 			
			# parsing Html data to find github links		
			file = open('raw_data.txt', 'r')
			soup = BeautifulSoup(file)
			link=soup.find('a', {'class': 'js-current-repository'}).contents[0]
			git_link = soup.find('input', {'class': 'input-mini input-monospace js-url-field js-zeroclipboard-target'}).get('value')
			links.append(git_link)			
	else:	
		saveHtml(url) 			
		# parsing Html data to find github links		
		file = open('raw_data.txt', 'r')
		soup = BeautifulSoup(file)
		
		for link in soup.findAll('a', attrs={'href': re.compile("github.com")}):
			if(len(link.get('href').split("/")) < 6 and len(link.get('href').split("/")) > 4):
				links.append(link.get('href'))
								
	for git_url in links:
		part = git_url.split("/")
		repo_name = part[4]
		
		os.system('clear')
		os.system('CLS')
		
		print "\nCreating folder --> " + repo_name + "..."
		os.makedirs(rootDirectory+repo_name)
			
		try:
			print "\nCloning repository --> " + repo_name
			Repo.clone_from(git_url, rootDirectory+repo_name)			
			print "\nRepository cloned successfully"
		except Exception,e: 
			print str(e)
else:
	os.system('clear')
	os.system('CLS')
	print "Please input a configuration file"