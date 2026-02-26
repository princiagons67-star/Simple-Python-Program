import random
print("Hello...Welcome to number guessing game...\nYou have only 5 chances to guess the number")
lb=int(input("Enter the lower bound: "))
ub=int(input("Enter the upper bound: "))
print(f"You have 5 chances to guess the number which lies b/w {lb} and {ub}. Let's Start!!!!")
num=random.randint(lb,ub)
chances=5
guess=0
while guess<chances:
    guess+=1
    NumGuessed=int(input("Enter your guess: "))
    if NumGuessed==num:
        print(f"Amazing...The Number is {num}...You guessed it in {guess} chances")
        break
    elif guess>=chances:
        print(f"OOOOPPPS!!!Chances are Over...The number was {num}...Better luck Next time...")
    elif NumGuessed<num:
        print("Higher")
    elif NumGuessed>num:
        print("Lower")
   
