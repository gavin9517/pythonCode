# _*_ encoding:utf-8 _*_
'''
你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
'''
import re

countDic = {}

with open('./1.txt','r') as f:

	for l in f:
		p = re.compile(r'[\s]*')
		for w in p.split(l):
			if len(w) == 0:
				continue

			if w not in countDic:
				countDic[w] = 1
			else:
				countDic[w] += 1
f.close()

for (k,v) in sorted(countDic.items(), key=lambda e: e[1], reverse=True)[:10]:
	print k,'出现',v,'次'