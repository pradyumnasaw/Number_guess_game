import random

print("Hi welcome to the game, This is a number guessing game.\nYou got 7 chances to guess the number. Let's start the game")

number_to_guess = random.randrange(100)  # Random number between 0 and 99
chances = 7
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1

    try:
        my_guess = int(input('Please Enter your Guess (0-99): '))
        if my_guess > 99:
            print("Invalid input! The number must be between 0 and 99.")
            guess_counter -= 1  # Don't count this as an attempt
            continue
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        guess_counter -= 1  # Don't count invalid input as an attempt
        continue

    if my_guess == number_to_guess:
        print(f'The number is {number_to_guess} and you found it right!! in the {guess_counter} attempt')
        break

    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f'Oops sorry, The number is {number_to_guess}. Better luck next time!')

    elif my_guess > number_to_guess:
        print('Your guess is higher.')

    elif my_guess < number_to_guess:
        print('Your guess is lesser.')

