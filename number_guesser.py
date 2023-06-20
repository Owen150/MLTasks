import random

top_of_random_range = input("Type a number: ")      #User Input is also enclosed in quotations thus, if input is digit, convert to integer
if top_of_random_range.isdigit():                   
    top_of_random_range = int(top_of_random_range)
    
    if top_of_random_range <= 0:
        print("Please Type a number larger than 0 next time")
        quit()
else:
    print("Please Type a number next time")
    quit()

random_number = random.randint(0, top_of_random_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue            #Returns to initial if statement
    
    if user_guess == random_number:
        print("You got it correct")
        break               #Terminates the loop
    elif user_guess > random_number:
        print("Your guess is above the random number")
    else:
        print("Your guess is below the random number")

print("You got it in", guesses, "guesses")      #Instead of using + and performing string conversion, use this