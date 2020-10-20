from datetime import datetime
import time
import csv
import calendar

temp = list()

def update():
	with open('reminder.csv', 'r') as reminderList:
		reader = csv.DictReader(reminderList)

		global temp
		for row in reader:
			temp.append(row)

def overWrite():
	with open('reminder.csv', 'w') as reminderList:
		global temp
		fieldNames = ['name', 'description', 'date']
		reader = csv.DictReader(reminderList, fieldnames=fieldNames)
		writer = csv.DictWriter(reminderList, fieldnames=fieldNames)
		writer.writeheader()
		writer.writerows(temp)

def printAll():
	update()
	global temp
	for row in temp:
		print(row)

def addReminder(name, description='', date=datetime.now().date()):
	update()
	global temp
	temp.append({'name':name, 'description':description, 'date':date})
	overWrite()

def getReminderScript(name):
	update()
	global temp
	for row in temp:
		if name==row['name']:
			return row['description']
	return 'Reminder Not Found!'

def getReminderYear(name):
	update()
	global temp
	for row in temp:
		if name==row['name']:
			return row['description']
	return 'Reminder Not Found!'

def getReminderMonth(name):
	update()
	global temp
	for row in temp:
		if name==row['name']:
			return row['description']
	return 'Reminder Not Found!'

def getReminderDate(name):
	update()
	global temp
	for row in temp:
		if name==row['name']:
			return row['description']
	return 'Reminder Not Found!'

def currentTime():
	return time.localtime(time.clock())

def getCalendar(year=datetime.now().year, month=datetime.now().month):
	return calendar.month(year, month)

def alert(name):
	update()
	global temp
	for row in temp:
		if name==row['name']:
			for i in row:
				print(i)

def activateTime():
	update()
	global temp
	while True:
		for row in temp:
			if datetime.now().date() == (row['year'], row['month'], row['date']):
				alert()


