# Guessing Game

A command-line number guessing game written in Python. The computer picks a secret number between 0 and 10000, and you try to guess it before you run out of guesses.

## How to play

1. Choose the maximum number of guesses you want, from 1 to 15.
2. Guess a number between 0 and 10000. After each wrong guess, the game tells you whether it was too high or too low, and how many guesses you have left.
3. Enter `-1` at any time to quit.

Only valid guesses count toward your limit, so typos and out-of-range numbers won't cost you a turn. If you win, the game tells you how many guesses it took. If you run out of guesses, it reveals the secret number.

## Example

```
Please enter the max amount of guesses you want to aim for this time: 10

Please enter a number between 0 and 10000 or -1 to quit: 5000

Your guess of 5000 was too high, try a smaller number.
You have 9 guesses left.
```

## Run it

You need Python 3 installed. From this folder, run:

```
python3 game.py
```

## Customize it

The settings are variables at the top of `game.py`, so you can change the number range (`low` and `high`), the largest and smallest number of guesses allowed (`guesses_limit` and `guesses_minimum`), and the quit code (`quit_code`).

## What I practiced

- `while` loops with `break` and `continue`
- Input validation with `try` / `except ValueError`
- Variables at the top of the file, so the settings are easy to change
- f-strings and the `random` module from Python's standard library
- Building a project in small steps, with a git commit after each change