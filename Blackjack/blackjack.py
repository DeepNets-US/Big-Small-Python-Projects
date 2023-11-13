from random import shuffle
from random import choice
from random import randint

# Set up constants
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)


class Blackjack:

    def __init__(self, money: int) -> None:

        # Game Configs
        self.bet = 0
        self.SUITS = [HEARTS, DIAMONDS, SPADES, CLUBS]
        self.CARDS = ["K", "Q", "A", "J", 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.POINTS = {"K": 10, "Q": 10, "A": choice([1, 11]), "J": 10}
        self.DECK = [(s, c) for s in self.SUITS for c in self.CARDS]

        # Set game values
        self.money = money
        self.player, self.player_hand = 0, []
        self.dealer, self.dealer_hand = 0, []

        # Initialize game
        self.createHands()

    def getCard(self) -> tuple:
        shuffle(self.DECK)
        return self.DECK.pop()

    def updatePoints(self, value: "int or str", user: str) -> None:
        if user == "p":
            try:
                self.player += self.POINTS[value]
            except:
                self.player += value
        else:
            try:
                self.dealer += self.POINTS[value]
            except:
                self.dealer += value

    def drewCard(self, deck: str, n: int = 1):
        for _ in range(n):
            card = self.getCard()

            if deck.lower() == "p":
                self.player_hand.append(card)
                self.updatePoints(card[-1], 'p')

            else:
                self.dealer_hand.append(card)
                self.updatePoints(card[-1], 'd')

    def createHands(self) -> None:

        # Assign player random cards
        self.drewCard("p", 2)

        # Assign dealer random cards
        self.drewCard("d", 2)

    def showHand(self, deck: str, hideDealerHand: bool = False) -> None:

        if deck.lower() == "p":
            deck = self.player_hand.copy()
        else:
            deck = self.dealer_hand.copy()

        top_bottom = " ___ "
        first_side = "|{value}  |"
        second_side = "| {suit} |"
        third_side = "|__{value}|"

        if hideDealerHand:
            deck[0] = ("#", "#")

        # Print the top row
        for _ in range(len(deck)):
            print(top_bottom, end=" ")
        print()

        # Print first side
        for _, value in deck:
            print(first_side.format(value=value), end=" ")
        print()

        # Print second side
        for suit, value in deck:
            print(second_side.format(suit=suit +
                  " " if value == 10 else suit), end=" ")
        print()

        # Print third side
        for _, value in deck:
            print(third_side.format(value=value), end=" ")
        print()
        print()

    def displayHands(self, hideDealerHand: bool = False):

        if hideDealerHand:
            print("\nDEALER: ???")
        else:
            print(f"\nDEALER: {self.dealer:2}")

        self.showHand("d", hideDealerHand)
        print(f"PLAYER: {self.player:2}")
        self.showHand(deck="p")
        print()

    def assignBet(self, bet: int):
        self.bet += bet
        self.money -= bet


if __name__ == "__main__":
    rules = """
    Rules:
        
        1. Receive two cards at the start.
        
        2. Choose to "hit"(H) for an additional card or "stand"(S) to keep the current hand.
        
        3. Aim to achieve a hand value as close to 21 as possible without exceeding it.
        
        4. Aces can be worth 1 or 11 points, and face cards are worth 10 points.
        
        5. Win if the hand is closer to 21 than the dealer's hand without busting (exceeding 21).
        
        6. Blackjack, an Ace with a 10-value card, often results in a higher payout.
        
        7. Push (tie) if the player and dealer have the same hand value.
        
        8. Lose the bet if the hand exceeds 21 or if the dealer's hand is closer to 21.
    """

    # Introduce the player with the game
    print(rules)

    # Game Configs
    game = Blackjack(money=5000)

    # Start Game
    while True:

        # Exit the game
        if game.money <= 0:
            print("\tYou went BROKE!")
            print("\tThanks for playing.")
            quit()

        # Take user bet
        print(f"Money: {game.money}")
        bet = input("How much do you bet?(1-5000 or QUIT)\n>").lower()

        # Additional Functionalities
        if bet == "QUIT".lower() or bet == "q":
            break
        elif bet == "r":
            print(rules)
            continue
        else:
            bet = int(bet)
            game.assignBet(bet)

        # Player's Turn
        while True:

            game.displayHands(True)

            if game.player > 21:
                break

            # Play a move (Player)
            move = input("(H)it, (S)tand, (D)ouble down\n>").lower()

            if move == 'd':
                game.assignBet(bet)
                print(f"Bet increased to: {game.bet} Money Left: {game.money}")

            if move in ('h', 'd'):
                game.drewCard('p')

                if game.player > 21:
                    continue

            if move in ('s', 'd'):
                break

        # Dealer's Turn
        if game.player <= 21:
            while game.dealer < 17:

                print("\nDealer hits:")
                game.drewCard("d")
                game.displayHands(True)

                if game.dealer > 21:
                    break

                input("Enter to continue...")
                print("\n\n")

        # Show final hands
        game.displayHands(False)
        

        # Final Check
        if game.dealer > 21:
            print('Dealer busts! You win ${}!\n'.format(bet))
            game = Blackjack(game.money + game.bet * 2)

        elif (game.player > 21) or (game.player < game.dealer):
            print('You lost!\n')
            game = Blackjack(game.money)

        elif game.player > game.dealer:
            print('You won ${}!\n'.format(bet))
            game = Blackjack(game.money + game.bet * 2)

        elif game.player == game.dealer:
            print('It\'s a tie, the bet is returned to you.\n')
            game = Blackjack(game.money + game.bet)
        