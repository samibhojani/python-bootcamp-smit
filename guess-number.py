guessing_game = 78

while True:
    user_input = int(input("Enter your guess: "))

    if user_input == guessing_game:
        print("You win!")
        break
    elif user_input < guessing_game:
        print("Wrong guess, try a higher number!")
    else:
        print("Wrong guess, try a lower number!")
