import sys
import copy
import time
import random

# Constants for grid size and cell representation
HEIGHT, WIDTH = 30, 100
ALIVE = "0"
DEAD = " "
SPEED = 0.1  # Speed/Delay in seconds

# Initialize the next state of cells with random alive/dead states
nextCells = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE
        else:
            nextCells[(x, y)] = DEAD

# Function to count the number of alive neighbors for a cell
def count_neighbors(pos: tuple, states: dict) -> int:
    x, y = pos
    n_neighbors = 0

    # Define neighboring coordinates
    neighbors = [
        ((x - 1) % WIDTH, (y - 1) % HEIGHT),
        ((x - 1) % WIDTH, y),
        ((x - 1) % WIDTH, (y + 1) % HEIGHT),
        (x, (y - 1) % HEIGHT),
        (x, (y + 1) % HEIGHT),
        ((x + 1) % WIDTH, (y - 1) % HEIGHT),
        ((x + 1) % WIDTH, y),
        ((x + 1) % WIDTH, (y + 1) % HEIGHT),
    ]

    # Count alive neighbors
    for neighbor in neighbors:
        if states[neighbor] == ALIVE:
            n_neighbors += 1

    return n_neighbors

# Main Program Loop
while True:
    print("\n" * 50)  # Clear console for each step

    # Display the current state of the game
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(nextCells[(x, y)], end="")
        print()

    print("Press Ctrl-C to quit.")

    # Compute the next state of the game
    currentCells = copy.deepcopy(nextCells)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            pos = (x, y)
            n_neighbors = count_neighbors(pos=pos, states=currentCells)

            # Apply rules of the game to determine next state
            if currentCells[pos] == ALIVE:
                if n_neighbors == 2 or n_neighbors == 3:
                    nextCells[pos] = ALIVE
                else:
                    nextCells[pos] = DEAD
            else:
                if n_neighbors == 3:
                    nextCells[pos] = ALIVE

    # Delay for visualization
    time.sleep(SPEED)

    # Clear console after each iteration for smoother visualization
    # This is optional and may not work on all platforms
    print("\033c", end="")  # ASCII escape sequence to clear console
