#!/usr/bin/python
# _*_ encoding:utf-8 _*_
from glactivecode import GLActiveCode
import MySQLdb,datetime

db = MySQLdb.connect(host='127.0.0.1',user='root',passwd='69886Gl',db='ll',
						port=3307)

cur = db.cursor()

r = GLActiveCode({'total':200})

for code in r.generate():
	currentDateTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	try:
		cur.execute('''
					INSERT INTO 
						active_codes(code,created_at,updated_at) 
					VALUES(
						"%s" , "%s" , "%s"
					)
			''' %(code , currentDateTime, currentDateTime) )
		db.commit()
	except:
		db.rollback()

db.close()