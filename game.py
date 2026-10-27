from random import randint

for i in range(15):
    print()
print("Welcome to the guessing game!")
print()

low = 0
high = 10000
quit = -1

max_attempts = 0
counter = 0

number = randint(low, high)
guess = None

while True:
    max_attempts = input("Please enter the max amount of attempts you want to aim for this time (number must be bigger than 0): ")
    
    try:
        max_attempts = int(max_attempts)
        if max_attempts < 1:
            continue
        break
    except ValueError:
        print("Please enter a valid number.")
        continue

while True:

    if counter == max_attempts:
        print("Sorry, you ran out of attempts. Try again later.")
        break

    guess = input(f"Please enter a number between {low} and {high} or -1 to quit: ")

    try:
        new_guess = int(guess)
    except ValueError:
        print("Please enter a valid number.")
        continue

    if new_guess == quit:
        break

    if new_guess < low or new_guess > high:
        print(f"please enter a number inbetween {low} and {high}.")
        continue

    if new_guess > number:
        print(f"Your guess of {new_guess} was too high, try a smaller number")
        counter += 1

    elif new_guess < number:
        print(f"Your guess of {new_guess} was too low, try a bigger number")
        counter += 1
    
    else:
        print(f"You did it! Your guess of {new_guess} was spot on!")
        break