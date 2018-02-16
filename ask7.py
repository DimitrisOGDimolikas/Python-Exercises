from datetime import datetime, date, timedelta

# Function that returns the difference between two dates
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)


# Info about the current day
currentDay = datetime.today().strftime("%a")
currentYear = datetime.today().year
currentMonth = datetime.today().month
currentDate = int(datetime.today().strftime("%d"))

numberOfDays = 0

# Range of dates
start_date = date(int(currentYear), int(currentMonth), currentDate)
end_date = date(int(currentYear) + 10, int(currentMonth), currentDate)

for x in daterange(start_date, end_date):
	myDate = x
	# If both dates match, add one to the counter
	if (myDate.strftime("%a") == currentDay and int(myDate.strftime("%d")) == currentDate):
			numberOfDays += 1

print "Number of " + datetime.today().strftime("%A") + "s the next 10 years that match today's date: " + str(numberOfDays)

raw_input("Press enter to exit....")