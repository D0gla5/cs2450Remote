import random

print ("Hi! I'm going to try to guess your age.")

guessed = False
while(guessed == False):
    guess = random.randint(15, 30)
    print ("I guess you are", guess, "years old.")
    response = input("Am I right? (y, n): ")
    if response == "y":
        guessed = True
        print("Yay!!")
    else:
        print ("Rats.")