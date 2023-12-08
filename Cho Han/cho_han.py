import random
from random import randint


class ChoHan:

    def __init__(self, random_state: int = 42):

        self.bet = 0
        self.money = 5000
        self.GUESSES = ["cho", "han"]
        self.number_mapping = {
            1: "ICHI",
            2: "NI",
            3: "SAN",
            4: "YON",
            5: "GO",
            6: "ROKU"
        }

    def reset_bet(self):
        self.bet = 0

    def assign_bet(self, bet: int):
        self.bet += bet

    def roll_dice(self):
        return [randint(1, 6) for _ in range(2)]

    def check_user_guess(self, user_guess: str):

        # Wait untill the correct input
        while (user_guess.strip().lower() not in self.GUESSES):
            print("Enter a guess value. Either 'CHO' or 'HAN'.")
            user_guess = input("\nCHO (even) or HAN (odd)?\n>")

        # Move ahead and disclose the numbers
        print("\nThe dealer lifts the cup to reveal:")
        dice_values = self.roll_dice()

        print(f"""
    {self.number_mapping[dice_values[0]]} - {self.number_mapping[dice_values[1]]}
    {dice_values[0]} - {dice_values[1]}
    """)

        if (sum(dice_values) % 2 == 0):

            if (user_guess.strip().lower() == "cho"):
                print(f"You won! You take {self.bet} mon.")
                print(f"The house collects a {self.bet // 10} mon fee.")
                self.money += (self.bet - (self.bet//10))
                self.reset_bet()

            else:
                self.money -= self.bet
                self.reset_bet()
                print("You lost!\n")
        else:

            if (user_guess.strip().lower() == "han"):
                print(f"You won! You take {self.bet} mon.")
                print(f"The house collects a {self.bet // 10} mon fee.\n")
                self.money += (self.bet - (self.bet//10))
                self.reset_bet()

            else:
                self.money -= self.bet
                self.reset_bet()

                print("You lost!\n")

    def play(self):
        print("Created by Utkarsh Saxena (deepnets722@gmail.com)")

        print("""
        In this traditional Japanese dice game, two dice are rolled in a bamboo
        cup by the dealer sitting on the floor. The player must guess if the
        dice total to an even (cho) or odd (han) number.
        """)

        while True:

            # Break if the user wents broke
            if (self.money <= 0):
                print("\n\tYou Went BROKE!!")
                break

            # Get the bet from the user and assign it
            print(f"\nYou have {self.money} mon. ", end=" ")
            user_bet = input("How much do you bet? (or QUIT)\n>")

            # Check if the user wanna play or not
            try:
                user_bet = int(user_bet)

                self.assign_bet(user_bet)

                print("""   
The dealer swirls the cup and you hear the rattle of dice.
The dealer slams the cup on the floor, still covering the 
dice and asks for your bet.""")

                # Get the user guess
                user_guess = input("\nCHO (even) or HAN (odd)?\n>")
                self.check_user_guess(user_guess)

            except:
                if (user_bet.lower() == "quit" or user_bet.lower() == "q"):
                    print("You Quit the game!!")
                    break

    def __repr__(self):
        return f"Nums: {self.nums}"


if __name__ == "__main__":
    game = ChoHan()
    game.play()
