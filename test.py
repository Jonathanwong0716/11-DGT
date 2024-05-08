import random


print("Welcome to the Guessing Game!")
print("Try to guess the number I am thinking of between 1 and 200.")

number = random.randint(1,200)  # generate random number
guess = -1  # initialize guess to an invalid value

while guess != number:
    guess_str = input("Enter your number: ")
    guess = int(guess_str)

    if guess < number:
        print("Too low, try again.")
    elif guess > number:
        print("Too high, try again.")

print("Congratulations! You guessed the number {number} correctly!") 
print("game over")
