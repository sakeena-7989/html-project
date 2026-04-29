import random

print("🎯 Welcome to the Number Guessing Game!")

while True:
    secret_number = random.randint(1, 100)

    attempts = 0

    print("\nI have chosen a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try higher. ⬆️")
            elif guess > secret_number:
                print("Too high! Try lower. ⬇️")
            else:
                print("🎉 Correct! You guessed the number.")
                print("Number of attempts:", attempts)

                # Score system
                if attempts <= 3:
                    score = 100
                elif attempts <= 6:
                    score = 70
                elif attempts <= 10:
                    score = 40
                else:
                    score = 10

                print("Your Score:", score)
                break

        except ValueError:
            print("❌ Please enter a valid 60number!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break