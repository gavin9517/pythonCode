#!/usr/bin/python
# _*_ encoding:utf-8 _*_
import glactivecode,time
import redis

# connect to redis server
r = redis.StrictRedis(host='localhost', port=6379, db=0)

if r.exists('activeCode'):
	r.delete('activeCode')

#write active code
for c in glactivecode.GLActiveCode({'total':200}).generate():
	r.lpush('activeCode', c)

#print all active code
for i in r.lrange('activeCode',0,200):
	print i