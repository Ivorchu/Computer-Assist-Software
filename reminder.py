	with open('reminder.csv', 'w') as reminderList:
		writer = csv.DictWriter(reminderList)
		writer.writeheader()
		writer.writerows(temp)

def getReminderScript(name):