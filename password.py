#from data.ahk import autohotkey
import tkinter as tk
from tkinter import *
from tkinter import ttk

#autohotkey(

def run(window, font):
	ask = tk.Label(window, text = "請選擇輸入Google或Facebook帳戶及密碼")
	ask["font"] = font
	ask.grid(row = 0, column = 1, pady = (80, 10)) 
	combo = ttk.Combobox(window, values=['', 'Google', 'Facebook'], state="readonly")
	combo.grid(row = 1, column = 1, pady = 5) 
	combo.current(0)
	result = ""
	def setup():
		acc = tk.StringVar()
		account = tk.Entry(window, textvariable = acc)
		account["font"] = font
		account.insert(0, '帳號')
		account.grid(row = 4, column = 1, pady = (10), padx = 160) 
		acc = acc.get()

		passw = tk.StringVar()
		password = tk.Entry(window, textvariable = passw)
		password["font"] = font
		password.insert(0, '密碼')
		password.grid(row = 5, column = 1, pady = (10), padx = 160) 
		passw = passw.get()

		btn = tk.Button(window, text='儲存', width=5, height=1, bd=0, bg = "#D35400", fg = "white")
		btn["font"] = font
		btn.grid(row = 6, column = 1, pady = 10, padx = 160)
	def getResult():
		if combo.get() == 'Google':
			label = tk.Label(window, text = "請輸入您的Google帳戶及密碼")
			label["font"] = font
			label.grid(row = 3, column = 1, pady = 5) 
			setup()
			window.update() 
			window.update_idletasks()
		elif combo.get() == combo['values'][2]:
			label = tk.Label(window, text = "請輸入您的Facebook帳戶及密碼")
			label["font"] = font
			label.grid(row = 3, column = 1, pady = 10) 
			setup()
			window.update() 
			window.update_idletasks()

	confirm = tk.Button(window, text='確定', width=5, height=1, bd=0, bg = "#D35400", fg = "white", command = lambda: getResult())
	confirm["font"] = font
	confirm.grid(row = 2, column = 1, pady = 5, padx = 10)
	

	