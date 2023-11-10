from random import randint


class Bagels:
    def __init__(self, difficulty: str = "easy"):
        """ 
        Initialize the Bagels game with the given difficulty level.

        Args:
            difficulty (str, optional): The difficulty level of the game. Defaults to "easy".

        Raises:
            ValueError: If an invalid difficulty level is selected.
        """
        self.difficulty = difficulty.lower()

        if self.difficulty == "kid" or self.difficulty == "k":
            self.N, self.n_tries = 2, 50
        elif self.difficulty == "easy" or self.difficulty == "e":
            self.N, self.n_tries = 3, 20
        elif self.difficulty == "normal" or self.difficulty == "n":
            self.N, self.n_tries = 4, 10
        elif self.difficulty == "hard" or self.difficulty == "h":
            self.N, self.n_tries = 6, 5
        elif self.difficulty == "impossible" or self.difficulty == "i":
            self.N, self.n_tries = 10, 2
        else:
            raise ValueError("Invalid Difficulty Level selected.")

        self.__rand_num = str(randint(10**self.N, 10**(self.N + 1) - 1))

    def desc(self):
        """Return the game description and instructions."""
        author = "Utkarsh Saxena"
        email = "deepnets722@gmail.com"

        details = f"""
        Bagels, a deductive logic game.
        By {author} {email}

        I am thinking of a {self.N}-digit number. Try to guess what it is.

        Here are some clues:
        When I say:     That means:
            Pico        One digit is correct but in the wrong position.
            Fermi       One digit is correct and in the right position.
            Bagels      No digit is correct.
            
        I have thought up a number.
        You have {self.n_tries} guesses to get it.
        
        Good Luck!!!
        """

        return details

    def __repr__(self):
        """Return a string representation of the Bagels object."""
        return f"Bagels(Num: {'*' * self.N}, Difficulty: {self.difficulty}, Tries: {self.n_tries})"

    def len_check(self, user_input: str):
        """Check if the length of user input matches the required number of digits.

        Args:
            user_input (str): The user's input.

        Returns:
            bool: True if the length matches, False otherwise.
        """
        return len(user_input) == self.N

    def check_states(self, user_input: str):
        """Check the state of the user's guess and determine if they have won.

        Args:
            user_input (str): The user's input.

        Returns:
            tuple: A tuple containing the game state and a boolean indicating if the user has won.
        """
        states = []
        for index, char in enumerate(user_input):
            if char in self.__rand_num:
                if char == self.__rand_num[index]:
                    states.append("Fermi")
                else:
                    states.append("Pico")
            else:
                states.append("Bagels")

        state = " ".join(state for state in states)

        if states == ["Fermi"] * self.N:
            return state, True

        return state, False

    def all_digit(self, user_input: str):
        """Check if all characters in the user's input are digits.

        Args:
            user_input (str): The user's input.

        Returns:
            bool: True if all characters are digits, False otherwise.
        """
        return all(map(str.isdigit, user_input))

    def check(self, user_input: str):
        """Check the user's input and determine the game state and if they have won.

        Args:
            user_input (str): The user's input.

        Returns:
            tuple: A tuple containing the game state message and a boolean indicating if the user has won.
        """
        check, won = "", False

        if self.len_check(user_input):
            if self.all_digit(user_input):
                check, won = self.check_states(user_input)
            else:
                check = "All values must be digits."
        else:
            check = "Length does not match."

        check += "\n"
        return check, won

    @property
    def get_randn(self):
        """Get the randomly generated number for testing or debugging purposes."""
        return self.__rand_num
