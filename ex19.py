import random

number = random.randint(1, 100)
guess_count = 0
max_guesses = 7

while guess_count < max_guesses:
    guess = int(input("Guess the number (between 1 and 100): "))
    guess_count += 1

    if guess == number:
        print("Congratulations! You guessed the number in", guess_count, "tries.")
        break
    elif guess < number:
        print("Too low.")
    else:
        print("Too high.")

if guess_count == max_guesses:
    print("Sorry, you ran out of guesses. The number was", number)
