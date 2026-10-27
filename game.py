from random import randint

for i in range(15):
    print()
print("Welcome to the guessing game!")
print()

low = 0
high = 10000
attempts_limit = 15
attempts_minimum = 1
quit_code = -1

max_attempts = 0
counter = 0

number = randint(low, high)
guess = None

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

while True:

    if counter == max_attempts:
        print("Sorry, you ran out of attempts. Try again later.")
        print()
        break

    print()
    guess = input(f"Please enter a number between {low} and {high} or {quit_code} to quit: ")

    try:
        new_guess = int(guess)
    except ValueError:
        print("Please enter a valid whole number.")
        continue

    if new_guess == quit_code:
        break

    if new_guess < low or new_guess > high:
        print(f"Please enter a number in between {low} and {high}.")
        continue

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