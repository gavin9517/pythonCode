#!/usr/bin/python
# _*_ encoding:utf-8 _*_
import os
from PIL import Image

IPHONE5_WIDTH = 640
IPHONE5_HEIGHT = 1136
PATH = './image/'

def convertToIphone5(source,savePath):
	im = Image.open(source)
	(width, height) = im.size
	
	if width > IPHONE5_WIDTH:
		im.thumbnail((IPHONE5_WIDTH,IPHONE5_HEIGHT), Image.BILINEAR)
		im.save(savePath+ os.path.basename(source))

if not os.path.exists('./iphone5'):
	os.mkdir('./iphone5')

if os.path.exists(PATH):
	imageList = [ f for f in os.listdir('./image') if f[-3:] in ['jpg','png']]
	
	for f in imageList:
		convertToIphone5(os.path.abspath(PATH + f), './iphone5/')
else:
	print 'no "{0}" directory'.format(PATH)