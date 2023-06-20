print("Welcome to my Computer Quiz")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
        
print("Okay, Let's Play")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct")
