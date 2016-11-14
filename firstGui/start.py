#!/usr/bin/python
# _*_ encoding:utf-8 _*_
from Tkinter import *

class Application(Frame):

	def __init__(self, master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.helloLabel = Label(self,text="hello,world!")
		self.helloLabel.pack()
		self.quitButton = Button(self,text='quit',command=self.quit)
		self.quitButton.pack()

if __name__ == '__main__':
	app = Application()
	app.master.geometry('475x280')
	app.master.title("first gui")
	app.mainloop()