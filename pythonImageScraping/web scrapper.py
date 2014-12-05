#TO DOWNLOAD DATA , downloaded lxml from http://www.lfd.uci.edu/~gohlke/pythonlibs/
#from lxml import html
#import requests
#
#url = 'http://econpy.pythonanywhere.com/ex/001.html'
#
#r = requests.get(url)
#
#tree = html.fromstring(r.text)
#
#buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#
#
#print('buyers :',buyers)


#TO DOWNLOAD DATA
#import requests
#from bs4 import BeautifulSoup
#
#url = 'http://espn.go.com/nba/teams'
#
#r = requests.get(url)
#
#soup = BeautifulSoup(r.text)
#
#tables = soup.find_all('ul',class_='medium-logos')
#
##print('tables :',tables)
#
#teams = []
#
#for table in tables:
	#lis = table.find_all('li')
	##print('bye')
	#for li in lis:
		#info = li.h5.a
		##print('hi :',info)
		#teams.append(info.text)
		#
#print(teams)


#TO DOWNLOAD IMAGES
#import requests
#from bs4 import BeautifulSoup
#
#url = 'http://imgur.com/'
#r = requests.get(url)
#soup = BeautifulSoup(r.text)
#images = soup.find_all('img')
##print(images)
#for image in images[0:10]:
	#urlt = image['src']
	#urlt = 'http:' + urlt
	#t = requests.get(urlt)
	#inputDir = 'download_images'
	#directory = inputDir + urlt.split('/')[-1]
	#print(urlt)
	#f = open(directory, 'w+b')
	#f.write(t.content)
	#f.close()



#TO DOWNLOAD IMAGES
#from lxml import html
#import requests
#import sys
##import urlparse : it is in python 2
#import urllib.parse
#
#def convert(count):
	#val = ''
	##print('%d\n' %count)
	#while count != 0:
		#val = chr(int(count%10)+48) + val
		#count = int(count/10)
	#return val
#
#url = 'http://imgur.com/'
#
#r = requests.get(url)
#
#tree = html.fromstring(r.text)
#
#images = tree.xpath('//img/@src')
##print(images)
#if not images:
	#sys.exit('No images found.')
#
#images = [urllib.parse.urljoin(r.url, url) for url in images] # changes relative addresses to absolute
#print('Found %s images' % len(images))
#
#count = int(1)
#for url in images[0:10]:
	#t = requests.get(url)
	#print(url)
	##print('%s' % url.split('/')[-1])
	##f = open('download_images/%s' % url.split('/')[-1], 'w+b')
	#val = ''
	#val = convert(count)
	#name = val + '.jpeg'
	#print(name)
	#f = open('download_images/%s' %name, 'w+b')
	#f.write((t.content))#.decode("utf-16"))
	#f.close()
	#count = count+1

import os
import requests
from bs4 import BeautifulSoup

url = 'http://www.kelvi.net/books/comics/index.php?album=Walt+Disney+Comics'
r = requests.get(url)
soup = BeautifulSoup(r.text)
images = soup.find_all('img')
inputDir = 'download_images'
os.system('mkdir ' + inputDir)
print(images)
for image in images:
	urlt = image['src']
	urlt = 'http://www.kelvi.net' + urlt
	t = requests.get(urlt)
	directory = inputDir + '\\' + urlt.split('/')[-1]
	print(urlt)
	f = open(directory, 'w+b')
	f.write(t.content)
	f.close()