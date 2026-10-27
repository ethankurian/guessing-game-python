# Guessing Game

A command-line number guessing game written in Python. The computer picks a secret number, and you try to guess it before you run out of attempts.

## How to play

1. Choose the maximum number of attempts you want (1 to 15).
2. Guess a number between 0 and 10000. After each guess, the game tells you if it was too high or too low.
3. Enter `-1` at any time to quit.

Only valid guesses count as attempts, so typos and out-of-range numbers won't cost you a turn. If you run out of attempts, the game reveals the secret number.

## Run it

You need Python 3 installed. From this folder, run:

```bash
python3 game.py
```