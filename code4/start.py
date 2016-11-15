#!/usr/bin/python
# _*_ encoding:utf-8 _*_
import re

class test(object):

	def __enter__(self):
		print 'enter'
		return 1

	def __exit__(self, *arg):
		print 'exit'
		return True

def countWorld(filePath):
	with open(filePath) as f:
		t = f.read().lower()
		words = re.findall(r'[a-z]+', t)

	return len(words)

# print countWorld('./1.txt')
with test() as t:
	print("t is not the result of test(), it is __enter__ returned")  
	print("t is 1, yes, it is {0}".format(t))  