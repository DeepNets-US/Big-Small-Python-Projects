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
        """
        Initialize the Blackjack game with the given initial amount of money.

        Parameters:
        - money (int): The initial amount of money for the player.

        Returns:
        None
        """

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
        self.create_hands()

    def get_card(self) -> tuple:
        """
        Get a card from the shuffled deck.

        Shuffles the deck and returns a tuple representing a card. The card is removed
        from the deck.

        Parameters:
        None

        Returns:
        tuple: A tuple representing a card, where the first element is the suit and the
               second element is the card value.
        """

        shuffle(self.DECK)
        return self.DECK.pop()

    def update_points(self, value: "int or str", user: str) -> None:
        """
        Update the points for the specified user based on the given value.

        If the value is a string, it is assumed to be a card identifier, and the corresponding
        point value is retrieved from the POINTS dictionary. The points are then added to either
        the player's or dealer's total based on the user parameter.

        If the value is an integer, it is directly added to the points of the specified user.

        Parameters:
        - value ("int or str"): The value to update the points. If a string, it is treated as a card identifier.
        - user (str): A string representing the user ('p' for player or 'd' for dealer).

        Returns:
        None
        """

        if isinstance(value, str):
            value = self.POINTS[value]

        if user.lower() == 'p':
            self.player += value
        else:
            self.dealer += value

    def drew_card(self, deck: str, n: int = 1):
        """
        Draw cards from the specified deck and update the player or dealer hands and points.

        Parameters:
        - deck (str): A string indicating the deck from which to draw cards. 'p' for player deck, 'd' for dealer deck.
        - n (int, optional): The number of cards to draw. Default is 1.

        Returns:
        None
        """

        for _ in range(n):

            card = self.get_card()
            if deck.lower() == "p":
                self.player_hand.append(card)
                self.update_points(card[-1], 'p')

            else:
                self.dealer_hand.append(card)
                self.update_points(card[-1], 'd')

    def create_hands(self) -> None:
        """
        Initialize and create the initial hands for both the player and the dealer.

        Draws two cards for the player and two cards for the dealer, updating their respective hands and points.

        Parameters:
        None

        Returns:
        None
        """
        self.drew_card("p", 2)
        self.drew_card("d", 2)

    def show_hand(self, deck: str, hide_dealer_hand: bool = False) -> None:
        """
        Display the cards in the specified deck (player or dealer) with a visual representation.

        Parameters:
        - deck (str): A string indicating the deck to display. 'p' for player deck, 'd' for dealer deck.
        - hide_dealer_hand (bool, optional): Whether to hide the dealer's second card. Default is False.

        Returns:
        None
        """

        if deck.lower() == "p":
            deck = self.player_hand.copy()
        else:
            deck = self.dealer_hand.copy()

        top_bottom = " ___ "
        first_side = "|{value}  |"
        second_side = "| {suit} |"
        third_side = "|__{value}|"

        if hide_dealer_hand:
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

    def display_hands(self, hide_dealer_hand: bool = False):
        """
        Display the current hands of both the player and the dealer.

        Parameters:
        - hide_dealer_hand (bool, optional): Whether to hide the dealer's second card. Default is False.

        Returns:
        None
        """

        if hide_dealer_hand:
            print("\nDEALER: ???")
        else:
            print(f"\nDEALER: {self.dealer:2}")

        self.show_hand("d", hide_dealer_hand)
        print(f"PLAYER: {self.player:2}")
        self.show_hand(deck="p")
        print()

    def assign_bet(self, bet: int):
        """
        Assign a bet for the current round.

        Parameters:
        - bet (int): The amount of money to bet for the current round.

        Returns:
        None
        """

        self.bet += bet
        self.money -= bet