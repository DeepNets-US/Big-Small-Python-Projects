import random
"""
A Carrot in a Box game.
"""


def open_box(player_1):
    carrot_found = bool(0 if random.random() < 0.5 else 1)

    if carrot_found:

        print(f"""
            {player_1} here is the inside of the box.
            
               ___VV___
              |   VV   |
              |   VV   |
              |___||___|   ________
             /    ||  /|  /       /|
            +-------+  | +-------+ |
            |  RED  |  | | GOLD  | |
            |  BOX  | /  | BOX   | /
            +-------+/   +-------+/
            (Carrot!!)
            """)

    else:

        print(f"""
            {player_1} here is the inside of the box.
            
               ________
              |        |
              |        |
              |________|       ________
             /        /|     /        /|  
            +--------+ |    +-------+  | 
            | GOLD   | |    |  RED  |  | 
            | BOX    | /    |  BOX  | /
            +--------+/     +-------+/
            (No Carrot!)
            """)
    return carrot_found


def draw_box(player_1, player_2):

    # Code to show the Box
    print(f"""
        HERE ARE TWO BOXES: 
        
          ________    ________
         /       /|  /       /|
        +-------+ | +-------+ |
        |  RED  | | | GOLD  | |
        |  BOX  | / | BOX   | /
        +-------+/  +-------+/
        {player_1.center(11):11} {player_2.center(11):11}
        """)

    print(f"--> {player_1}, You have a RED BOX.")
    print(f"--> {player_2}, You have a GOLD BOX.")


def main():
    # Header of the Creator
    print("Carrot in a Box created by Utkarsh Saxena")

    # Take user input for names
    player_1, player_2 = input("Enter Player 1 Name: "), input(
        "Enter Player 2 Name: ")

    # Show Black Boxes
    draw_box(player_1, player_2)
    input("Press Enter to Continue\n>")
    print(f"\nAsk {player_2} to don't look and close their eyes!")
    input(f"\nWhen {player_2} has closed their eyes, press Enter...")

    # Check if the carrot is found in player 1's box
    carrot_found = open_box(player_1)
    input("Press Enter to Continue...")

    # Clear the outputs
    print("\n"*100)
    print(f"{player_1} say one of the following.")
    print("  1) There is a carrot in my box.")
    print("  2) There is not a carrot in my box.\n")
    input("Press Enter to Continue...")

    # Ask player 2 to make a move
    player_2_move = input(f"{player_2} do you want to swap the boxes!!??\n>>>")
    if player_2_move.upper()[0] == "Y":
        print("\t\tBoxes Swapped!!")

        if carrot_found:
            print(f"""
            {player_2} got the CARROT!!
            
              ___VV___ 
             |   VV   | 
             |   ||   | 
             |___||___|    ________
            /        /|  /       /|
            +-------+ | +-------+ |
            | GOLD  | | |  RED  | |
            |  BOX  | / |  BOX  | /
            +-------+/  +-------+/
        """)

        else:
            print(f"""
            {player_1} got the CARROT!!
            
                           ___VV___ 
                          |   VV   | 
                          |   ||   | 
               _______    |___||___|
             /       /|  /        /|
            +-------+ | +-------+  |
            | GOLD  | | |  RED  |  |
            |  BOX  | / |  BOX  | /
            +-------+/  +-------+/
        """)

    else:
        print("\t\tBoxes kept!!")
        if carrot_found:
            print(f"""
            {player_1} got the CARROT!!
            
               ___VV___ 
              |   VV   | 
              |   ||   | 
              |___||___|    ________
             /        /|  /        /|
            +-------+  | +-------+  |
            |  RED  |  | |  GOLD |  |
            |  BOX  | /  |  BOX  | /
            +-------+/   +-------+/
        """)
        else:
            print(f"""
            {player_2} got the CARROT!!
            
              ___VV___ 
             |   VV   | 
             |   ||   | 
             |___||___|    ________
            /        /|  /       /|
            +-------+ | +-------+ |
            |  RED  | | |  GOLD | |
            |  BOX  | / |  BOX  | /
            +-------+/  +-------+/
        """)


if __name__ == "__main__":
    main()
