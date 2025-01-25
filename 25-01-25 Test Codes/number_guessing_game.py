import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    
    while True:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess < secret_number:
            print("Too Low!")
        elif guess > secret_number:
            print("Too High")
        else:
            print("Correct! You guessed the number.")
            break

number_guessing_game()
