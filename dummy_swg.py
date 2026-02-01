import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter s (snake), w (water), g (gun): ")
youDict = {"s": 1, "w": -1, "g": 0}
you = youDict[youstr]

if computer == you:
    print("Draw")

elif (computer == -1 and you == 1) or \
     (computer == 1 and you == 0) or \
     (computer == 0 and you == -1):
    print("You Win!")

else:
    print("You Lose!")
