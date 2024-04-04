def leapYears():
	def leap_year(y):
	   if y % 4 == 0 and(y % 100 != 0 or y % 400 == 0):
	       return 1
	   else :
	       return 0
	def number_of_days(m, y):
	   if m in [1, 3, 5, 7, 8, 10, 12]:
	       return 31
	   elif m in [4, 6, 9, 11]:
	       return 30
	   elif m == 2:
	       return 28 + leap_year(y)
	def days_passed(d, m, y):
	   days = 0
	   for month in range(1, m):
	       days += number_of_days(month, y)
	   return days + d - 1
	day = int(input("Please enter a day: "))
	month = int(input("Please enter a month: "))
	year = int(input("Please enter a year: "))
	print("Menu:")
	print("1) Calculate the number of days in the given month.")
	print("2) Calculate the number of days passed in the given year.")
	choice = int(input())
	if choice == 1:
	   print(number_of_days(month, year))
	elif choice == 2:
	   print(days_passed(day, month, year))