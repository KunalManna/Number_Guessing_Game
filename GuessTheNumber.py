import random
num=random.randint(1,100) #Wil generate random number between 1 to 100
guess=None
nguess=1                  #Counter Variable for count the attempt by the user
while guess!=num:
    guess=int(input("Enter the number between 1 to 100:\n"))   #User input
    if guess>100:
        print("Please give the proper input.")
    elif guess>num:
        print("Lower Number please.")
    elif guess<num:
        print("Higher Number please.")
    else:
        print(f"Correct Guess! You have answered it in {nguess} attempt")
    nguess+=1
