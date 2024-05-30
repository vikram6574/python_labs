# The game will prompt the user to guess a number between 1 and 10, providing feedback on whether the guess is too high, too low, or correct. Use random. "import random"

import random
#def main():
print("Guess a number between 1 and 10")
number = random.randint(1, 10)
print(number)
guess = int(input("Enter a number: "))
while guess != number:
        if guess < number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        guess = int(input("Enter a number: "))
print("You win")
    