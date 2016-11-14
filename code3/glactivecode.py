#!/usr/bin/python
# _*_ encoding:utf-8 _*_
import sys, uuid, string, os, json

class GLActiveCode(object):
	"""Generate active code"""
	argv = {
		'total': 20,
		'output': None,#print or save to path
		'path' : None,
		'upper': True,
		'format': 'text', #support: text,json
	}

	OUTPUT_SUPPORT = ['print','file',None]
	FORMAT_SUPPORT = ['text','json']

	def __init__(self,argvDic ={}):
		self.argv.update(argvDic)
		self.__validate()

	def __validate(self):
		if self.argv['output'] not in self.OUTPUT_SUPPORT:
			raise Exception('only support output method is ' 
				+ string.join(self.OUTPUT_SUPPORT,',') )

		if self.argv['output'] == 'file' and self.argv['path'] == None :
			raise ValueError("the save path can not been empty!")

		if self.argv['format'] not in self.FORMAT_SUPPORT:
			raise Exception('not support save format!')

	def generate(self, type = 'uuid'):
		if self.argv['output'] == 'file':
			self.__saveToPath(self.__generate(self.argv['total']) , 
								self.argv['path'] )

		elif self.argv['output'] == 'print':
			if self.argv['format'] == 'text':
				for i in self.__generate(self.argv['total']):
					print i
			elif self.argv['format'] == 'json':
				print json.dumps( self.__generate(self.argv['total']) , 
					sort_keys=True, indent=4, separators=(',', ': '))
		else:
			return self.__generate(self.argv['total'])

	def __saveToPath(self, source , path , format = 'text'):
		f = open(path,'w+')
		last = len(source)
		i = 1

		if self.argv['format'] == 'text':
			for l in source:
				if i == last:
					f.write(l)
				else:
					f.write(l + "\n")

				i = i + 1
		elif self.argv['format'] == 'json':
			f.write( json.dumps( source, sort_keys = True, indent=4,
								 separators=(',',': ')) )

		f.close()

	def __generate(self, num = 10, upper = True):
		result = []

		for i in range(int(num)):
			if upper:
				result.append( str(uuid.uuid4()).upper() )
			else:
				result.append( str(uuid.uuid4()) )

		return result

if __name__ == '__main__':
	argDic = {}
	for a in sys.argv[1:]:
		if a.startswith('--'):
			if '=' not in a:
				raise Exception('argument value "' + a + '" can not been empty')
			(arg , v) = a.split('=')
			argDic[arg[2:]] = v

	GLActiveCode(argDic).generate()