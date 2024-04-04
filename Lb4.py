#commenting functions
import random #calls a library

print("Below is a password generator:")

def passwordGenerator():
  #the purpose of this function is to make a random generated password using animals, numbers and characters
    listOfAnimals=["cat", "dog", "leapord", "wolf", "dokey", "dragon", "bird", "horse", "gorilla", "panda", "bear", "snake", "rabbit", "frog", "lion", "eagle",]
  #a list of animals
    ani=random.choice(listOfAnimals)
  #choosing a random choice from the list i already wrote
    beginingNum = random.randint(7, 2109487)
  #choosing a random number from 7 to 2109487
    lastNum=random.randint(4, 500)
  #choosing a random number from 4 to 500
    listOfChare=["!", "@", "#", "$", "%", "&", "_"]
    char=random.choice(listOfChare)
  #making it so when you call "char" it will randomly chooser a character in the list
    newPass=str(beginingNum)+ani+char+str(lastNum)
    print(newPass)    
  #putting all the different parameters together so when the function is called a random password is generated 
    
#password generator
passwordGenerator()
passwordGenerator()
passwordGenerator()
passwordGenerator()
passwordGenerator()

print("")

def rollingDice():
  #the purpose of this function is to simulate the rolling of a dice numerically 
    num = random.randint(1,6)
  #randomly choosing a number from 1 to 6
    num2 = random.randint(1, 6)
    print("The first dice rolled a " + str(num))
    print("The second dice rolled a " +str(num2))
    print("In total you rolled a " + str(num+num2))
rollingDice()