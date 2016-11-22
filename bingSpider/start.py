# _*_ encoding:utf-8 _*_
import urllib
import os
import re
import sys
import time



if os.path.exists('./photo') == False:
	os.mkdir('./photo')

url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=1&n=1&nc={0}&pid=hp&video=0'.format(time.time())

if os.path.exists('./photo/version'):
		try:
			fp = open('./photo/version','r')
			version = fp.readline(13)
			if version < time.time() - 1800:
				print 'after 30 mins update'
				sys.exit(-1)
			fp.close()
		except Exception as e:
			print e

html = urllib.urlopen(url).read()

if html == 'null':
	print 'read bing image error!'
	sys.exit(-1)
else:
	

	reg = re.compile(r'"url":"(.*)","urlbase"', re.S)
	path = re.search(reg,html).group(1)

	right = path.rindex('/')
	name =  path.replace( path[:right+1],'')
	savePath = './photo/' + name

	try:
		fp = urllib.URLopener().open(path)
		data = fp.read()

		f = open(savePath , 'w+b')
		f.write(data)
		f.close()

		#write lock file
		f = open('./photo/version','w+')
		f.write( str(time.time()) )
		f.close()

		print 'save photo success!'
	except Exception as e:
		print e
