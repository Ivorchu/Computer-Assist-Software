import calendar
from datetime import datetime
import time
import csv

def addReminder(name, description='', year=datetime.now().year, month=datetime.now().month, date=datetime.now().date, hour=0, mint=0, minRemind=0, activate=True):
	with open('reminder.csv', 'w+') as reminderList:
		fieldNames = ['name', 'description', 'year', 'month', 'date', 'hour', 'mint', 'minRemind', 'activate']
		writer = csv.DictWriter(reminderList, fieldnames=fieldNames)

		writer.writeheader()
		writer.writerow({'name':name, 'description':description, 'year':year, 'month':month, 'date':date, 'hour':hour, 'mint':mint, 'minRemind':minRemind, 'activate':activate})

def deleteReminder(name):
	temp = list()
	with open('reminder.csv', 'r') as reminderList:
		reader = csv.DictReader(reminderList)

		for row in reader:
			temp.append(row)
			for field in row:
				if field==name:
					temp.remove(row)

	with open('reminder.csv', 'w') as reminderList:
		writer = csv.DictWriter(reminderList)
		writer.writerows(temp)

def getReminderScript(name):
	with open('reminder.csv', 'r') as reminderList:
		reader = csv.DictReader(reminderList)

		for row in reminderList:
			if name==row['name']:
				return row['description']
		return 'Reminder Not Found!'

def getReminderYear(name):
	with open('reminder.csv', 'r') as reminderList:
		reader = csv.DictReader(reminderList)

		for row in reminderList:
			if name==row['name']:
				return row['year']
		return 'Reminder Not Found!'

def getReminderMonth(name):
	with open('reminder.csv', 'r') as reminderList:
		reader = csv.DictReader(reminderList)

		for row in reminderList:
			if name==row['name']:
				return row['month']
		return 'Reminder Not Found!'

def getReminderDate(name):
	with open('reminder.csv', 'r') as reminderList:
		reader = csv.DictReader(reminderList)

		for row in reminderList:
			if name==row['name']:
				return row['date']
		return 'Reminder Not Found!'

def getReminderHour(name):
	with open('reminder.csv', 'r') as reminderList:
		reader = csv.DictReader(reminderList)

		for row in reminderList:
			if name==row['name']:
				return row['hour']
		return 'Reminder Not Found!'

def getReminderMint(name):
	with open('reminder.csv', 'r') as reminderList:
		reader = csv.DictReader(reminderList)

		for row in reminderList:
			if name==row['name']:
				return row['mint']
		return 'Reminder Not Found!'

def getReminderMinRemind(name):
	with open('reminder.csv', 'r') as reminderList:
		reader = csv.DictReader(reminderList)

		for row in reminderList:
			if name==row['name']:
				return row['minRemind']
		return 'Reminder Not Found!'

def activateReminder(name):
	with open('reminder.csv', 'r') as reminderList:
		reader = csv.DictReader(reminderList)

		for row in reminderList:
			if name==row['name']:
				row['activate'] = True
				return
		return 'Reminder Not Found!'

def deactivateReminder(name):
	with open('reminder.csv', 'r') as reminderList:
		reader = csv.DictReader(reminderList)

		for row in reminderList:
			if name==row['name']:
				row['activate'] = False
				return
		return 'Reminder Not Found!'
