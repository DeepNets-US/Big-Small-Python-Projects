import sys
import time
import random

try:
    import bext
except:
    print("The program requires BEXT library, which is not installed in the system.")
    print("Bext can be installed using `pip install bext`")

# Get the window size
W, H = bext.size()

# In the last column a New Line is automatically added.
W -= 1

# Number of LOGOS present on the screen
N_LOGOS = int(input(("Enter Number of Logos: ")))

# The delay or the duration of the logo on the screen
DELAY = 0.05

# Each logo has a different color
COLORS = [
    'red',
    'blue',
    'yellow',
    'green',
    'cyan',
    'white',
    'magenta'
]

# The possible actions we can take in this env
TR, TL = 'ur', 'ul'
BR, BL = 'dr', 'dl'
DIRECTIONS = (TR, TL, BR, BL)


# Clear any previous data
bext.clear()

# A set of LOGOS
LOGOS = [
    {
        'color': random.choice(COLORS),
        'direction': random.choice(DIRECTIONS),
        'x': random.randint(1, (W - 4)//2) * 2,
        'y': random.randint(1, H - 4),
    } for _ in range(N_LOGOS)
]

"""
X: random.randint(0, W//2) * 2

The reason that X is initialized in this manner is that we wanr the logo to strike the corner. And if we have to do so, we need to have even values for the X coordinate.

"""

# A function to manage the bouncing of the walls situation


def bounce_of_walls(logo, counter, collision):

    # If the logo hits the top left corner.
    if logo['x'] == 0 and logo['y'] == 0:
        logo['direction'] = BR
        counter += 1
        collision += 1

    # If the logo hits the bottom left corner.
    elif logo['x'] == 0 and logo['y'] == H - 1:
        logo['direction'] = TR
        counter += 1
        collision += 1

    # If the logo hits the top right corner.
    elif logo['x'] == W - 3 and logo['y'] == 0:
        logo['direction'] = BL
        counter += 1
        collision += 1

    # If the logo hits the bottom right corner.
    elif logo['x'] == W - 3 and logo['y'] == H - 1:
        logo['direction'] = TL
        counter += 1
        collision += 1

    # The logo hits the left wall
    elif logo['x'] == 0 and logo['direction'] == BL:
        logo['direction'] = BR
        collision += 1

    elif logo['x'] == 0 and logo['direction'] == TL:
        logo['direction'] = TR
        collision += 1

     # The logo hits the right wall
    elif logo['x'] == W - 3 and logo['direction'] == BR:
        logo['direction'] = BL
        collision += 1

    elif logo['x'] == W - 3 and logo['direction'] == TR:
        logo['direction'] = TL
        collision += 1

    # The logo hits the upper wall
    elif logo['y'] == 0 and logo['direction'] == TR:
        logo['direction'] = BR
        collision += 1

    elif logo['y'] == 0 and logo['direction'] == TL:
        logo['direction'] = BL
        collision += 1

    # The logo hits the lower wall
    elif logo['y'] == H - 1 and logo['direction'] == BR:
        logo['direction'] = TR
        collision += 1

    elif logo['y'] == H - 1 and logo['direction'] == BL:
        logo['direction'] = TL
        collision += 1

    return counter, collision

# A function to handle the movement of the logo


def move(logo):
    DIR = logo['direction']

    if DIR == TR:
        logo['x'] += 2
        logo['y'] -= 1

    elif DIR == TL:
        logo['x'] -= 2
        logo['y'] -= 1

    elif DIR == BR:
        logo['x'] += 2
        logo['y'] += 1

    elif DIR == BL:
        logo['x'] -= 2
        logo['y'] += 1


# Start the main loop
cornerCollisions = 0
NCOLLISIONS = 0

while True:

    # For each of the LOGO
    for logo in LOGOS:

        # Initialize the logo at the starting position
        bext.goto(logo['x'], logo['y'])

        # (!) Try commenting this line out.
        print(' ', end='')

        # Record the original direction
        orgDir = logo['direction']

        # Create the bouncing effect
        cornerCollisions, NCOLLISIONS = bounce_of_walls(
            logo,
            cornerCollisions,
            NCOLLISIONS
        )

        # Change collor after collision
        if logo['direction'] != orgDir:
            logo['color'] = random.choice(COLORS)

        # Move the logo
        move(logo)

    # Dislay for the Corner Collisions
    bext.goto(5, 0)
    bext.fg('white')
    print('Corner bounces:', cornerCollisions, end='')
    
    bext.goto(5, 1)
    bext.fg('white')
    print('N Collisions  :', NCOLLISIONS, end='')
    

    # Update the location of the logo
    for logo in LOGOS:
        bext.goto(logo['x'], logo['y'])
        bext.fg(logo['color'])
        print('DVD', end='')

    # Re-config and continuation
    bext.goto(0, 0)
    sys.stdout.flush()
    time.sleep(DELAY)
