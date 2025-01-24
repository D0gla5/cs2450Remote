import random

print ("Hi! I'm going to try to guess your age.")

guessed = False
guesses = []
while(guessed == False):
    guess = random.randint(15, 30)
    if all(num in guesses for num in range(15, 31)):
        print("Okay, I give up.")
        break
    if guess in guesses:
        continue

    print ("Are you", guess, "years old.")
    response = input("Am I right? (y, n): ")
    if response == "y":
        guessed = True
        print("Yay!!")
    else:
        print ("Rats.")
        guesses.append(guess)

