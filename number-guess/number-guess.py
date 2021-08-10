import random       # Import random module

random_number = random.randint(7, 49)       # Variable to store the random numbers, Randit returns a random number depending on range set.

tries = 1       # Variable tries = 1 

username = input("Hello Friend, Whats your username ? ")       # User input 

print("Hello", username + ", ",)

question = input ("Wanna play a game ? [Yes/No] ")

if question == "No":

    print("Chickens are out, I see ")

if question == "Yes":
    
    print("I have a number between  7 and 49 ")

    guess = int(input("Guess a number : "))

    if guess > random_number:

        print("Too high my friend, Have another go.")
    
    if guess < random_number:

        print("Too Low my friend, Have another go.")


    while guess != random_number:   # While loop till the != random_number

        tries += 1      # increase tries by 1, with each loop

        guess = int(input("Give it another try."))

        if guess < random_number:

            print("Too Low my friend, Have another go. ")

    if guess == random_number:

        print("Holy !!! You Win ! The number was ", random_number, "and it only took ", tries, "tries")



