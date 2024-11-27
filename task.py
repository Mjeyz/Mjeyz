import random

random_number = random.randint(1, 100)
print("Welcome to Number Guessing Game! ")
print("I'm thingking of number between 1 and 100.")
choose_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if choose_level == "easy":
    print("You have 10 attempts remaining to guess a number.")
    for _ in range(10):
        guess = int(input("Make a guess : "))
        if guess > random_number:
            print("Too high")
            print("Guess again.")
        elif guess < random_number:
            print("Too low.")
            print("Guess again.")
        elif guess == random_number:
            print("Congratulation 🫡 you win. ")
            break
        else:
            print("inValid Number.")
    else:
        print("sorry! your attempts has finished. and you lose 😭")

if choose_level == "hard":
    print("You have 5 attempts remaining to guess a number.")
    for _ in range(5):
        guess = int(input("Make a guess : "))
        if guess > random_number:
            print("Too high")
            print("Guess again.")
        elif guess < random_number:
            print("Too low.")
            print("Guess again.")
        elif guess == random_number:
            print("Congratulation 🫡 you win. ")
            break
        else:
            print("inValid Number.")
    else:
        print("sorry! your attempts has finished. and you lose 😭")
