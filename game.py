# Summary: This game asks the user to guess a number, either until they get it correct or run out of attempts.

# I had to import randint from the random module built into python to generate random numbers to guess.
from random import randint

# This is just the greeting/welcome screen.
# i is used as a counter variable, which is necessary for a for loop.
# Print blank lines to push old output offscreen
for i in range(15):
    print()
print("Welcome to the guessing game!")
print()

# I tried to use variables for everything so all the necessary changes can be made from right here up top.
low = 0
high = 10000
attempts_limit = 15
attempts_minimum = 1
quit_code = -1

max_attempts = 0
counter = 0

number = randint(low, high)
guess = None

# This section mainly checks if the max amount of attempts entered is valid (not too high or low, and make sure it is a whole number).
while True:
    max_attempts = input("Please enter the max amount of attempts you want to aim for this time: ")
    
    try:
        max_attempts = int(max_attempts)
        if max_attempts < attempts_minimum:
            print("Max attempts has to be greater than or equal to 1, please try again.")
            print()
            continue
        if max_attempts > attempts_limit:
            print("Max attempts can't be that high, please try again.")
            print()
            continue
        break
    except ValueError:
        print("Please enter a valid whole number.")
        print()
        continue

# This is the main game loop which asks the user for input.
while True:

    # Checks if the user has reached max attempts.
    if counter == max_attempts:
        print("Sorry, you ran out of valid attempts.")
        print(f"The actual number was {number}, better luck next time!")
        print()
        break

    print()
    guess = input(f"Please enter a number between {low} and {high} or {quit_code} to quit: ")

    # Makes sure input is a whole number.
    try:
        new_guess = int(guess)
    except ValueError:
        print("Please enter a valid whole number.")
        continue

    # Checks if user wants to leave the program.
    if new_guess == quit_code:
        break

    # Checks if user input is in between the correct high and low values mentioned before.
    if new_guess < low or new_guess > high:
        print(f"Please enter a number in between {low} and {high}.")
        continue

    # This keeps track of the number of valid real attempts.
    counter += 1

    if new_guess > number:
        print(f"Your guess of {new_guess} was too high, try a smaller number")

    elif new_guess < number:
        print(f"Your guess of {new_guess} was too low, try a bigger number")
    
    else:
        print(f"You did it! Your guess of {new_guess} was spot on!")
        print(f"You won in {counter} guesses!")
        print()
        break