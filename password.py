import tkinter as tk
from tkinter import *
from tkinter import ttk


def run(window, font):
	ask = tk.Label(window, text = "請選擇輸入Google或Facebook帳戶及密碼")
	ask["font"] = font
	ask.grid(row = 0, column = 1, pady = (80, 10)) 
	combo = ttk.Combobox(window, values=['', 'Google', 'Facebook'], state="readonly")
	combo.grid(row = 1, column = 1, pady = 5) 
	combo.current(0)
	result = ""
	acc = tk.StringVar()
	passw = tk.StringVar()
	def setup():
		account = tk.Entry(window, textvariable = acc)
		account["font"] = font
		account.insert(0, '帳號')
		account.grid(row = 4, column = 1, pady = 10, padx = 160) 

		password = tk.Entry(window, textvariable = passw)
		password["font"] = font
		password.insert(0, '密碼')
		password.grid(row = 5, column = 1, pady = 10, padx = 160) 

		btn = tk.Button(window, text='儲存', width=5, height=1, bd=0, bg = "#D35400", fg = "white")
		btn["font"] = font
		btn.grid(row = 6, column = 1, pady = 10, padx = 160)

		

	label = tk.Label(window, text = "")
	label["font"] = font
	def getResult():
		if combo.get() == combo['values'][1]:
			label['text'] = "請輸入您的Google帳戶及密碼"
			label.grid(row = 3, column = 1, pady = 5) 
			setup()
			acc = acc.get()
			passw = passw.get()
			window.update() 
			window.update_idletasks()
			
		elif combo.get() == combo['values'][2]:
			label['text'] = "請輸入您的Facebook帳戶及密碼"
			label.grid(row = 3, column = 1, pady = 5) 
			setup()
			acc = acc.get()
			passw = passw.get()
			window.update() 
			window.update_idletasks()

		def importData():
			f = open("data.ahk", "w")
			f.write(""+acc+"\t"+passw)
			f.close()

		importData()

	confirm = tk.Button(window, text='確定', width=5, height=1, bd=0, bg = "#D35400", fg = "white", command = lambda: getResult())
	confirm["font"] = font
	confirm.grid(row = 2, column = 1, pady = 5, padx = 10)



	