from datetime import datetime
import time
import csv
import calendar
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

temp = list()

def clearFrame(frame):
	for widget in frame.winfo_children():
		widget.destroy()
		frame.pack_forget()
		frame.pack()

def update():
	with open('reminder.csv', 'r') as reminderList:
		reader = csv.DictReader(reminderList)

		global temp
		temp.clear()
		for row in reader:
			temp.append(row)

def overWrite():
	with open('reminder.csv', 'w') as reminderList:
		global temp
		fieldNames = ['name', 'description', 'date']
		writer = csv.DictWriter(reminderList, fieldnames=fieldNames)
		writer.writeheader()
		writer.writerows(temp)

def printAll(window, font):
	update()
	global temp
	names = []
	for row in temp:
		names.append(row['name'])

	reminder = tk.Label(window, text = '行事曆')
	reminder.grid(row=1, column=0)
	btn_add = tk.Button(window, text='新增', width=5, height=1, bd=0, bg = "#D35400", fg = "white", command = lambda: [clearFrame(window), addReminderPage(window, font)])
	btn_add.grid(row=2, column=0)
	combo = ttk.Combobox(window, values=names, state="readonly")
	combo.grid(row = 3, column = 0, pady = 5) 
	combo.current(0)
	btn_del = tk.Button(window, text='刪除', width=5, height=1, bd=0, bg = "#D35400", fg = "white", command = lambda: deleteReminder(window, font, combo.get()))
	btn_del.grid(row=3, column=1)
	total_rows = len(temp) 
	total_columns = 3
	text = tk.Text(window, width=80, fg='blue', font=font, padx = 10, pady = 5)
	text.grid(row=3, column=0)
	for row in temp: 
		for data in row:
			text.insert(tk.END, row[data])
			text.insert(tk.END, ', ')
		text.insert(tk.END, '\n')

def addReminder(window, font, name, description='', date=datetime.now().date()):
	update()
	global temp
	temp.append({'name':name, 'description':description, 'date':date})
	overWrite()

def deleteReminder(window, font, name):
	update()
	global temp
	for row in temp:
		if row['name'] == name:
			for data in row:
				temp.remove(row[data])
	overWrite()
	printAll(window, font)

def currentTime():
	return time.localtime(time.clock())

def alert(name):
	update()
	global temp
	msg=''
	for row in temp:
		if name==row['name']:
			for data in row:
				msg.append(data)
				msg+='\n'
	tk.messagebox.showinfo("提醒事項", msg)


def activateTime():
	update()
	global temp
	while True:
		for row in temp:
			if datetime.now().date() == (row['year'], row['month'], row['date']):
				alert()

def addReminderPage(window, font):
	title = tk.Label(window, text="新增備忘錄")
	title['font'] = font

	title.grid(row = 0, column = 1, pady = (80, 10)) 
	name = tk.StringVar()
	description = tk.StringVar()
	year = tk.StringVar()
	month = tk.StringVar()
	date = tk.StringVar()

	eventName = tk.Entry(window, textvariable = name, bg = "#ABB2B9")
	eventName["font"] = font
	eventName.insert(0, '名稱')
	eventName.grid(row = 1, column = 1, pady = 10, padx = 160) 

	eventDesc = tk.Entry(window, textvariable = description)
	eventDesc["font"] = font
	eventDesc.insert(0, '簡述')
	eventDesc.grid(row = 2, column = 1, pady = 10, padx = 160)

	eventYear = tk.Entry(window, textvariable = year)
	eventYear["font"] = font
	eventYear.insert(0, datetime.now().year)
	eventYear.grid(row = 3, column = 1, pady = 10, padx = 160) 

	eventMonth = tk.Entry(window, textvariable = month)
	eventMonth["font"] = font
	eventMonth.insert(0, datetime.now().month)
	eventMonth.grid(row = 4, column = 1, pady = 10, padx = 160) 

	eventDate = tk.Entry(window, textvariable = date)
	eventDate["font"] = font
	eventDate.insert(0, datetime.now().day)
	eventDate.grid(row = 5, column = 1, pady = 10, padx = 160)  

	btn = tk.Button(window, text='確認', width=5, height=1, bd=0, bg = "#D35400", fg = "white", command = lambda: [clearFrame(window), addReminder(window, font, name.get(), description.get(), (year.get(), month.get(), date.get())), printAll(window, font)])
	btn["font"] = font
	btn.grid(row = 6, column = 1, pady = 10, padx = 160)


