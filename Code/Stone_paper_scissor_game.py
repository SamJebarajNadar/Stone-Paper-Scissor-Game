import random

print("\t\t\t-----------------STONE PAPER SCISSOR GAME ------------------\n")

##Computer choice area
randNo=random.randint(1,3)
if  randNo==1:
	computer_choice='s'
elif randNo==2:
	computer_choice='p'
elif randNo==3:
	computer_choice='x'


## Taking user input and converting it into lower case
user_input=input("Choices:\n Stone (s) \n Paper(p) \n Scissor(x) \nEnter your choice -->")
user_choice=user_input.lower()


## Making function for comparing computer_choice and user_choice 
def userwin(computer_choice,user_choice):
	if computer_choice==user_choice:
		return None

	if computer_choice=='s':
		if user_choice=='x':
			return False
		elif user_choice=='p':
			return True

	if computer_choice=='p':
		if user_choice=='s':
			return False
		elif user_choice=='x':
			return True

	if computer_choice=='x':
		if user_choice=='p':
			return False
		elif user_choice=='p':
			return True


##Calling compare function 
calling_compare_function=userwin(computer_choice,user_choice)			


##Printing  computer and user choices
print("\n\n---------Arena-----------")
print(f"Computer chose--> {computer_choice}")
print(f"User chose--> {user_choice}")


##Calling compare function and finding who won
if calling_compare_function==None:
	print("Game is Tied!")

elif calling_compare_function==True:
	print("You won!")

else:
	print("You lose!")






OUTPUT:
Choices:
 Stone (s) 
 Paper(p) 
 Scissor(x) 
Enter your choice -->p


---------Arena-----------
Computer chose--> p
User chose--> p
Game is Tied!







