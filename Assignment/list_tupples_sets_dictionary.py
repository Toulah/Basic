print('          LISTS')
days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(days_of_the_week[5])
print(days_of_the_week)
weekdays = (days_of_the_week[1:6])
print(weekdays)
weekends = days_of_the_week[0], days_of_the_week[-1]
print(weekends)

if "Monday" in days_of_the_week:
    print("yes Monday is a day of the week")

days_of_the_week[4:] = "jodi", "vondredi", "samedi"
print(days_of_the_week)

days_of_the_week[1:4] = ["lundi", "mardi", "macredi"]
print(days_of_the_week)

days_of_the_week.insert(1, "Monday")
print(days_of_the_week)

days_of_the_week.append("Tueday")
print(days_of_the_week)