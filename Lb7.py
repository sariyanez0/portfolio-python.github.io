def age():	
	#age related conditions
	name = input("Hello!, What is your name? ")
	print("Nice to meet you "+name+"!")
	
	age=int(input("How old are you "+name+"? "))
	if age>=18:
		print("You can get your drivers license!")
	elif age<18 and age>=16:
		print("Sorry you cant get your license just yet, but you can get your permit!")
	else:
		print("Oh im afriad you are too young to drive")
	
	if age>=18:
		print("Did you also know you can vote!")
	else:
		print("You are not allowed to vote just yet!")
	
	if age>=17:
		print("You are allowed to watch NC-17 movies")
	elif age>13 and age<17:
		print("You are allowed to watch R rated movies but preferly with adult supervision")
	elif age>=13:
		print("People over the age of 13 can watch PG-13 movies")
	elif age>=0:
		print("You can watch G rated movies!")
	
