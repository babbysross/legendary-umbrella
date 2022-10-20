import random

while True:
    name = input("Hi, What's your name?\n")
    if not name.isalpha():
        print("Please type a real name in.")
    else:
        break

print("Well, " + name + ", I'm thinking of a number between 1 and 20, can you guess it?")
answer = random.randint(1, 20)

for guesses in range(1, 7):
    try:
        guess = int(input("Go on, guess! \n"))
    except ValueError:
        continue

    if guess < answer:
        print("Oops, too low!")
        guesses = guesses + 1
    elif guess > answer:
        print("Aww, too high!")
        guesses = guesses + 1
    else:
        print("Wow, " + name + ", you got it!")
        break

if not guess == answer:
    print("Too many wrong guesses, better luck next time.")
else:
    print("\nThanks for playing!")