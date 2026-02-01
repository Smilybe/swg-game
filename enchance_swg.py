import random

class SnakeWaterGun:
    def __init__(self):
        self.choices = {"s": "Snake", "w": "Water", "g": "Gun"}
        self.rules = {
            ("Snake", "Water"): "win",
            ("Water", "Gun"): "win",
            ("Gun", "Snake"): "win",
        }
        self.score = {"wins": 0, "losses": 0, "draws": 0}
    
    def get_computer_choice(self):
        return random.choice(list(self.choices.values()))
    
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "draw"
        elif (user_choice, computer_choice) in self.rules:
            return "win"
        else:
            return "lose"
    
    def play_round(self):
        print("\n" + "="*30)
        print("Snake-Water-Gun Game")
        print("="*30)
        
        # Get user choice
        while True:
            user_input = input("Enter your choice (s=Snake/w=Water/g=Gun): ").strip().lower()
            if user_input in self.choices:
                user_choice = self.choices[user_input]
                break
            print("Invalid input! Please enter 's', 'w', or 'g'.")
        
        # Get computer choice
        computer_choice = self.get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine result
        result = self.determine_winner(user_choice, computer_choice)
        
        if result == "win":
            print("🎉 You Win!")
            self.score["wins"] += 1
        elif result == "lose":
            print("💻 You Lose!")
            self.score["losses"] += 1
        else:
            print("🤝 It's a Draw!")
            self.score["draws"] += 1
        
        print(f"\nScore: Wins: {self.score['wins']}, Losses: {self.score['losses']}, Draws: {self.score['draws']}")
    
    def play(self):
        print("Welcome to Snake-Water-Gun Game!")
        print("Rules: Snake drinks Water, Water drowns Gun, Gun shoots Snake")
        
        while True:
            self.play_round()
            play_again = input("\nPlay again? (y/n): ").strip().lower()
            if play_again != 'y':
                print("\nThanks for playing!")
                print(f"Final Score: {self.score}")
                break

if __name__ == "__main__":
    game = SnakeWaterGun()
    game.play()