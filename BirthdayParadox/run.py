import matplotlib.pyplot as plt
from birthdayParadox import BirthdayParadox

# Take user input
while True:
    Npeople = int(input("How many birthdays shall I generate? (Max 100)\n>"))
    if (0 < Npeople <= 100):
        break

# Generate Birthdays
bp = BirthdayParadox(Npeople)
print(
    f"Birthdays: \t{', '.join(birthday for birthday in bp.show_birthdays())}")

# Find a Match
match = bp.get_match()
if match != None:
    print(f"""
        In this simulation multiple people have birthdat on: {bp.readable(match)}
    """)
else:
    print("There are no matching birthdays.")

# Generate birthdays for the same people for 100,000 times
print('\nGenerating', Npeople, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

# Starting simulation
print('\nLet\'s run another 100,000 simulations.')

stepCase = int(input("Compute data after every ? steps.\n>"))

# Track number of the matches found
simMatch = 0
NSims = 100_000
midSimMatch = 0
stepCaseProbs = []

# Start Simulation
for i in range(1, NSims+1):

    # Show information after every 10,000 runs.
    if i % stepCase == 0:
        print(i, 'simulations run...')

        midSimProba = round(midSimMatch / stepCase, 2)
        stepCaseProbs.append(midSimProba)
        midSimMatch = 0

    birthdays = BirthdayParadox(Npeople)
    if birthdays.get_match() != None:
        simMatch += 1
        midSimMatch += 1

print('100,000 simulations ran.\n')

probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', Npeople, 'people, there was a')
print('matching birthday in that group', simMatch, 'This means')
print('that', Npeople, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')

# A probability graph for individual step case probabilities
stepRuns = [(i+1) * 10_000 for i in range(len(stepCaseProbs))]

plt.title(f"Probability after each {stepCase} runs")
plt.plot(stepRuns, stepCaseProbs, linestyle="--")
plt.scatter(stepRuns, stepCaseProbs, marker="*", s=50, c="green")
plt.ylim([min(stepCaseProbs) - 0.01, max(stepCaseProbs) + 0.01])
plt.show()

# Bar graph for the final probability.
probability /= 100
plt.title("Probability of same Birthday")
plt.bar(x="Match", height=probability, color="green")
plt.bar(x="No Match", height=1 - probability, color="red")
plt.xlabel("Possibilities")
plt.ylim([0, 1])
plt.show()
