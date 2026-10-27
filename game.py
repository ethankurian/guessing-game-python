from random import randint

print("Welcome to the guessing game!")

number = randint(0, 10000)
guess = None

while guess != number:
    
    guess = input("Please enter a number between 0 and 10000 or -1 to quit: ")

    try:
        int(guess)
    except:
        print("Please enter a valid number.")
        continue

    new_guess = int(guess)

    if new_guess == -1:
        break

    if new_guess < 0 or new_guess > 10000:
        print("please enter a number inbetween 0 and 10000.")
        continue

    if new_guess > number:
        print(f"Your guess of {new_guess} was too high, try a smaller number")

    elif new_guess < number:
        print(f"Your guess of {new_guess} was too low, try a bigger number")
    
    else:
        print(f"You did it! Your guess of {new_guess} was spot on!")
        break