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
	
	def setup():
		acc = tk.StringVar()
		account = tk.Entry(window, textvariable = acc)
		account["font"] = font
		account.insert(0, '帳號')
		account.grid(row = 4, column = 1, pady = 10, padx = 160) 

		passw = tk.StringVar()
		password = tk.Entry(window, textvariable = passw)
		password["font"] = font
		password.insert(0, '密碼')
		password.grid(row = 5, column = 1, pady = 10, padx = 160) 


		def importData():
			acnt = acc.get()
			acnt = str(acnt)
			psw = passw.get()
			psw = str(psw)
			f = open("data.ahk", "r", encoding="utf-8")
			for i in f:
				if i == "##### Data Starts #####":
					f = open("data.ahk", "a", encoding="utf-8")
					content = acnt + "\t" + psw + "\n"
					f.write(content)
					f.close()

		btn = tk.Button(window, text='儲存', width=5, height=1, bd=0, bg = "#D35400", fg = "white", command = importData)
		btn["font"] = font
		btn.grid(row = 6, column = 1, pady = 10, padx = 160)

		
		
	label = tk.Label(window, text = "")
	label["font"] = font
	def getResult():
		if combo.get() == combo['values'][1]:
			label['text'] = "請輸入您的Google帳戶及密碼"
			label.grid(row = 3, column = 1, pady = 5) 
			setup()
			window.update() 
			window.update_idletasks()
			
		elif combo.get() == combo['values'][2]:
			label['text'] = "請輸入您的Facebook帳戶及密碼"
			label.grid(row = 3, column = 1, pady = 5) 
			setup()
			window.update() 
			window.update_idletasks()

	def instruct():
		root = tk.Tk
		root.title('指示')
		root.geometry('100x100') 
		root.resizable(0,0)
		root.mainloop()

	confirm = tk.Button(window, text='確定', width=5, height=1, bd=0, bg = "#D35400", fg = "white", command = lambda: getResult())
	confirm["font"] = font
	confirm.grid(row = 2, column = 1, pady = 5, padx = 10)
	
	instructions = tk.Button(window, text='使用指示', width=5, height=1, bd=0, bg = "#D35400", fg = "white", command = lambda: instruct())
	instructions["font"] = font
	instructions.grid(row = 2, column = 1, pady = 5, padx = 10)
	#root = tk.Tk()

	#root.mainloop()



	