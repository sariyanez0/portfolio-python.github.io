def leap_year():	
	#leap year
	year = int(input("Enter a year: "))
	if (year<=1751):
	  print("Leap years didn't exist back then!")
	elif(year>1751):
	  if(year%400==0):
	      print("It was NOT a leap year")
	  elif(year%4==0 and year%400==0):
	    print("It was a leap year.")
	
	if (year==1752):
	  print("It was a leap year.")
