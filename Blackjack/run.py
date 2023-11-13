from blackjack import Blackjack

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
        game.assign_bet(bet)

    # Player's Turn
    while True:

        game.display_hands(True)

        if game.player > 21:
            break

        # Play a move (Player)
        move = input("(H)it, (S)tand, (D)ouble down\n>").lower()

        if move == 'd':
            game.assign_bet(bet)
            print(f"Bet increased to: {game.bet} Money Left: {game.money}")

        if move in ('h', 'd'):
            game.drew_card('p')

            if game.player > 21:
                continue

        if move in ('s', 'd'):
            break

    # Dealer's Turn
    if game.player <= 21:
        while game.dealer < 17:

            print("\nDealer hits:")
            game.drew_card("d")
            game.display_hands(True)

            if game.dealer > 21:
                break

            input("Enter to continue...")
            print("\n\n")

    # Show final hands
    game.display_hands(False)

    # Final Check
    if game.dealer > 21:
        print('Dealer busts! You win ${}!\n'.format(game.bet))
        game = Blackjack(game.money + game.bet * 2)

    elif (game.player > 21) or (game.player < game.dealer):
        print('You lost!\n')
        game = Blackjack(game.money)

    elif game.player > game.dealer:
        print('You won ${}!\n'.format(game.bet))
        game = Blackjack(game.money + game.bet * 2)

    elif game.player == game.dealer:
        print('It\'s a tie, the bet is returned to you.\n')
        game = Blackjack(game.money + game.bet)
