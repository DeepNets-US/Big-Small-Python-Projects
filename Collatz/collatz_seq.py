import matplotlib.pyplot as plt

intro = """
Collatz Sequence, or, the 3n + 1 Problem
By Utkarsh Saxena deepnets722.com

The Collatz sequence is a sequence of numbers produced from a starting
number n, following three rules:

1. If n is even, the next number n is n / 2.
2. If n is odd, the next number n is n * 3 + 1.
3. If n is 1, stop. Otherwise, repeat.

It is generally thought, but so far not mathematically proven, that
every starting number eventually terminates at 1. More information
about the Collatz sequence can be found at https://en.wikipedia.org/wiki/
Collatz_conjecture.

"""

print(intro)

# Function to generate the Collatz Sequence


def show_collatz_conjecture(num: int) -> list:
    values = []
    def eq(x): return 3 * x + 1

    while num != 1:
        if num % 2 == 0:             # Even Number
            num = int(num/2)
            values.append(num)
        else:                        # Odd number
            num = eq(num)
            values.append(num)

        if num != 1:
            print(num, end=", ")
        else:
            print(num)

    return values


while True:
    # Get the number input from the user and preprocess it
    num = input(
        "\nEnter a starting number (greater than 0) or QUIT:\n>>>").strip()

    if num.lower() == "q" or num.lower() == "quit":
        break

    try:
        # Generate the Collatz Conjucture from the user input
        num = int(num)
        values = show_collatz_conjecture(num)

        plt.figure(figsize=(8, 5))
        plt.title(f"Collatz Conjecture for {num}")
        plt.plot(range(1, len(values)+1), values)
        plt.scatter(range(1, len(values)+1), values, label="Values")
        plt.xlabel("Number of Iterations")
        plt.ylabel("Achieved values")
        plt.axhline(1, c="black", linestyle="--", label="1")
        plt.legend()
        plt.grid()
        plt.show()

    except:
        print("Enter a valid number, a number greater than 0.")
