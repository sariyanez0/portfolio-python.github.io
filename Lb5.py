def inputCheck():
	#input checker
	input_1 = int(input("Enter a 4-digit whole number: "))
	#if len(input_1)==4 and input_1.isdecimal() and input_1[0]
	if input_1 >= 1000:
	  print("Thanks!")
	
	else:
	  print("That's not a 4-digit number.")
	
	input_2 = int(input("Enter an integer less than 50: "))
	if input_2>50:
	#(input_2.isdeciaml() or (input_2[1:].isdecimal and input_2[0]=="-")) and int(input_2) >50:
		print("not a number less than 50")
	
	 # print("Thanks!")
	
	#else:
	 # print("That's not a number less than 50")
	
	input_3 = input("Enter a string that begins with a vowel: ")
	if (input_3[0].lower() in "aeiou"):
		print("thanks")
	
	input_4 = input("Enter a string that ends with a consonant: ")
	if input_4[-1].isalpha() and input_4.lower()not in "aeiou": 
		print("thanks")
	else:
		print("that is not end on a consonant.")