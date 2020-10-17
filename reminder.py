import calendar
import datetime
import time
import csv

def setCalendar(firstweek=0):
	global cal
	cal = calendar.TextCalendar(firstweek=firstweek)

def getMonthDates(year,month):
	return calendar.formatmonth(theyear=year, themonth=month)

def getYearDates(year):
	return calendar.formatyear(theyear=year)

def getDate():
	return datetime.date

def getTime():
	return datetime.time

def addReminder(name, description, year, month, date, hour=0, mint=0, minRemind=0):
	with open('reminder.csv', 'w+') as reminderList:
		fieldNames = ['name', 'description', 'year', 'month', 'date', 'hour', 'mint', 'minRemind']
		writer = csv.DictWriter(reminderList, fieldnames=fieldNames)

		writer.writeheader()
		writer.writerow({'name':name, 'description':description, 'year':year, 'month':month, 'date':date, 'hour':hour, 'mint':mint, 'minRemind':minRemind})

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

