from functions import greet
from Lb2 import exactChange
from Lb4 import passwordGenerator
from Lb5 import inputCheck
from Lb6 import leap_year
from Lb7 import age
from Lb8 import num_pyramid
from Lb9 import is_odd_pow3
from Lb10 import leapYears

print("Welcome to my portfolio")
print("================================")
print("================================")


portfolio_state = True

while portfolio_state==True:
	print("Labs")
	print("1. Project STEM Silly Sentances")
	print("2. Lab 2 Exact Change")
	print("3. Project Stem Calculatr area of room")
	print("4. Lab 4 Password Generator")
	print("5. Lab 5 Input Checker")
	print("6. Project STEM Room Area")
	print("7. Project STEM Chatbox")
	print("8. Project STEM Divisible by 3")
	print("9. Do Now ASCII Cat or Pingulo")
	print("10. Lab 6 Leap Year")
	print("11. Lab 7 Age Related Conditions")
	print("12. Lab 8 Number Pyramids")
	print("13. Lab 9 Odd Power of 3")
	print("14. Project STEM Calender")
	

	lab_choice= input("Which Lab do you want to see? (1/2/3/4/5/6/7/8/9/10): ")
	if lab_choice == 1:
		greet()
	elif lab_choice==2:
		exactChange()

	#elif lab_choice==3:
		#ermerm()
	elif lab_choice==4:
		passwordGenerator()

	elif lab_choice==5:
		inputCheck()
		
	elif lab_choice==6:
		leap_year()
	elif lab_choice==7:
		age()

	
	elif lab_choice==8:
		num_pyramid()
	elif lab_choice==9:
		is_odd_pow3()
	
	else:
		print("Choose a Valid Lab Number")

	playAgain = input("Do you want to keep exploring my portfolio? (y/n): ")
	if playAgain !="y":
		portfolio_state = False
	print("")

print("Thanks for taking the time to look at my python programming work! If you have any feedback email me")



