#!/usr/bin/python
# _*_ encoding: utf-8 _*_
from PIL import Image , ImageDraw , ImageFont

im = Image.open('./avator.png')

picWidth, picHeight = im.size

font = ImageFont.load_default()

draw = ImageDraw.Draw(im)
draw.text((picWidth - 30,10),"89", font= font)

# del draw

im.save('./avator.text.png')
