import random

# Computer randomly picks: 1 (snake), 0 (gun), -1 (water)
computer = random.choice([1, 0, -1])  # Use list, not set!

youstr = input("Enter your choice (s/w/g): ").strip().lower()

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Validate input
if youstr not in youDict:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
else:
    you = youDict[youstr]

    print(f"You chose {reverseDict[you]}. Computer chose {reverseDict[computer]}.")

    if computer == you:
        print("It's a draw!")
    else:
        # Winning conditions for you
        if (computer == -1 and you == 1) or \
           (computer == 1 and you == 0) or \
           (computer == 0 and you == -1):
            print("You Win!")
        else:
            print("You Lose!")