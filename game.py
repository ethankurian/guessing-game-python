# Summary: This game asks the user to guess a number, either until they get it correct or run out of guesses.

# I had to import randint from the random module built into python to generate random numbers to guess.
from random import randint

# This is just the greeting/welcome screen.
# _ is used to indicated no counter variable is needed, just something there for the for loop to function.
# Print blank lines to push old output offscreen
for _ in range(15):
    print()
print("Welcome to the guessing game!")
print()

# I tried to use variables for everything so all the necessary changes can be made from right here up top.
low = 0
high = 10000
guesses_limit = 15
guesses_minimum = 1
quit_code = -1

max_guesses = 0
counter = 0

number = randint(low, high)

# This section mainly checks if the max amount of guesses entered is valid (not too high or low, and make sure it is a whole number).
while True:
    max_guesses = input("Please enter the max amount of guesses you want to aim for this time: ")
    
    try:
        max_guesses = int(max_guesses)
        if max_guesses < guesses_minimum:
            print("Max guesses has to be greater than or equal to 1, please try again.")
            print()
            continue
        if max_guesses > guesses_limit:
            print("Max guesses can't be that high, please try again.")
            print()
            continue
        break
    
    except ValueError:
        print("Please enter a valid whole number.")
        print()
        continue

# This is the main game loop which asks the user for input.
while True:

    # Checks if the user has reached max guesses.
    if counter == max_guesses:
        print()
        print("Sorry, you ran out of valid guesses.")
        print(f"The actual number was {number}, better luck next time!")
        print()
        break

    print()
    guess = input(f"Please enter a number between {low} and {high} or {quit_code} to quit: ")
    print()

    # Makes sure input is a whole number.
    try:
        new_guess = int(guess)

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    # Checks if user wants to leave the program.
    if new_guess == quit_code:
        print("Thanks for playing!")
        break

    # Checks if user input is in between the correct high and low values mentioned before.
    if new_guess < low or new_guess > high:
        print(f"Please enter a number in between {low} and {high}.")
        continue

    # This keeps track of the number of valid real guesses.
    counter += 1

    if new_guess > number:
        print(f"Your guess of {new_guess} was too high, try a smaller number.")

    elif new_guess < number:
        print(f"Your guess of {new_guess} was too low, try a bigger number.")
    
    else:
        # Formatting for the winning guess.
        if counter == 1:
            win_guess = "guess"
        else:
            win_guess = "guesses"

        print(f"You did it! Your guess of {new_guess} was spot on!")
        print(f"You won in {counter} {win_guess}!")
        print()
        break

    # How many guesses the user has left
    guesses_left = max_guesses - counter

    # Makes sure the formatting is correct.
    if guesses_left == 1:
        word = "guess"
    else:
        word = "guesses"
    
    print(f"You have {guesses_left} {word} left.")