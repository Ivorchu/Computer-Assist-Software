import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
import time
import sys

def run(window, font):
	ask = tk.Label(window, text = "請選擇輸入Google或Facebook帳戶及密碼", bg = "#ABB2B9")
	ask["font"] = font
	ask.grid(row = 0, column = 0, pady = (80, 10)) 
	combo = ttk.Combobox(window, values=['', 'Google', 'Facebook'], state="readonly")
	combo.grid(row = 1, column = 0, pady = 5) 
	combo.current(0)

	instructions = tk.Button(window, text='操作說明', width=10, height=1, bd=0, bg = "#D35400", fg = "white", command = lambda: instruct())

	def instruct():
		root = tk.Tk()
		root.title('操作說明')
		root.geometry('300x50') 
		root.resizable(0,0)
		intro = tk.Label(root, text = "按Alt+G登入Google並前往Gmail\n按Alt+F前往並登入Facebook")
		intro["font"] = font
		intro.grid(row = 0, column = 0) 
		root.mainloop()

	def instruction_window():
		instructions["font"] = font
		instructions.grid(row = 7, column = 0, pady = (220,0), padx = (480,0))

	result = ""	
	
	def setup():
		acc = tk.StringVar()
		account = tk.Entry(window, textvariable = acc)
		account["font"] = font
		account.insert(0, '帳號')
		account.grid(row = 4, column = 0, pady = 10, padx = 160) 

		passw = tk.StringVar()
		password = tk.Entry(window, textvariable = passw)
		password["font"] = font
		password.insert(0, '密碼')
		password.grid(row = 5, column = 0, pady = 10, padx = 160) 

		instructions.grid(row = 7, column = 0, pady = 53, padx = (480,0))


		def importData():
			acnt = acc.get()
			acnt = str(acnt)
			psw = passw.get()
			psw = str(psw)

			f = open("ahkData.ahk", "r", encoding = 'utf-8')
			lines = f.readlines()
			lines[0] = "account = " + acnt 
			lines[1] = "password = " + psw

			f = open("ahkData.ahk", "a", encoding = 'utf-8')
			f.writelines(lines)

			content = '''
			;按下Alt+g去gmail信箱
			!g::
			run, "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" -incognito "https://gmail.com/" 
			sleep, 5000
			send, {shift}
			sleep, 2000
			send, %account% {enter}
			sleep, 2000
			send, {shift}
			sleep, 5000
			send, %password% {enter}
			return

			;按下Alt+f去fb
			!f::
			run, "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" -incognito "https://www.facebook.com" 
			sleep, 5000
			send, {shift}
			sleep, 2000
			send, %fb% {enter}
			sleep, 2000
			send, {shift}
			sleep, 5000
			send, %fbPassword% {enter}
			return
			'''
			f.writelines(content)
			f.close()
			os.system('ahkData.ahk')


		btn = tk.Button(window, text='儲存', width=5, height=1, bd=0, bg = "#D35400", fg = "white", command = importData)
		btn["font"] = font
		btn.grid(row = 6, column = 0, pady = 10, padx = 160)
		
		
	label = tk.Label(window, text = "")
	label["font"] = font
	def getResult():
		if combo.get() == combo['values'][1]:
			label['text'] = "請輸入您的Google帳戶及密碼"
			label.grid(row = 3, column = 0, pady = 5) 
			setup()
			window.update() 
			window.update_idletasks()
			
		elif combo.get() == combo['values'][2]:
			label['text'] = "請輸入您的Facebook帳戶及密碼"
			label.grid(row = 3, column = 0, pady = 5) 
			setup()
			window.update() 
			window.update_idletasks()


	confirm = tk.Button(window, text='確定', width=5, height=1, bd=0, bg = "#D35400", fg = "white", command = lambda: getResult())
	confirm["font"] = font
	confirm.grid(row = 2, column = 0, pady = 5, padx = 10)
	
	instruction_window()


