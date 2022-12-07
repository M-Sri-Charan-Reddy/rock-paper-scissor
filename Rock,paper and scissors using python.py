import random
print("""Choices are:
1. rock
2. paper
3. scissor""")
choice=int(input("Enter a choice from 1-3: "))
#condition if user selects invalid input
while choice>3 or choice<1:
    choice=int(input("Enter valid choice: "))
#user choice conditions
if choice == 1:
    user="rock"
elif choice == 2:
    user="paper"
else:
    user="scissor"
print("user's choice is:",user)
computer=random.randint(1,3)
if computer == 1:
    computer="rock"
elif computer == 2:
    computer="paper"
else:
    computer="scissor"
print("computer's choice is:",computer)
if user == computer:
    print("Both players selected", user,". It's a tie!")
    result = "tie"
elif ((user == "paper" and computer == "rock") or (user == "rock" and computer == "scissor") or (user == "scissor" and computer == "paper")):
    print("You win(:")
    result = "win"
else:
    print("You lose. try again!")
    result = "lose"