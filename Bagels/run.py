from bagles import Bagels


diff = """
Difficulty Level:           Desc:
Kid(K)                      Guess a 2 digit random number.
Easy(E)                     Guess a 3 digit random number.
Normal(N)                   Guess a 4 digit random number.
Hard(H)                     Guess a 6 digit random number.
Impossible(I)               Guess a 10 digit random number.

"""

play = "y"

while (play == "y"):

    # Show user game information and ask configurations
    print(diff)
    mode = input("Select difficulty: ")

    bagels = Bagels(difficulty=mode)
    print(bagels.desc())

    # Start the game

    for guess in range(1, bagels.n_tries + 1):
        user_input = input(f"(G -{guess:2})Enter the number: ").strip()
        check, won = bagels.check(user_input=user_input)

        if won:
            print("\n\tYou won!!!!\n")
            break

        else:
            print(check)

    if not won:
        print(f"\tI was thinking of : {bagels.get_randn}\n")

    # Ask the user to continue the game
    play_more = input(
        "Do you want to play again(Y or N): ").lower().strip()

    if play_more == "n":
        print("\n\tThanks for Playing!\n")
        play = "n"
