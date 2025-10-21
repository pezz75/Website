import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
    else:
        random_number = random.randrange(1, top_of_range + 1)
else:
    print("Please type a number next time.")
    quit()

while True:
    user_guess = input("Make a guess: ")

    if not user_guess.isdigit():
        print("Please type a number next time.")
        continue

    user_guess = int(user_guess)

    if user_guess <= 0:
        print("Please type a number larger than 0 next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess < random_number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
        print("ypu got it!"+gueses,"guesses")
    