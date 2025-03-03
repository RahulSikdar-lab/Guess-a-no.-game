import random
n = random.randint(1,100)
a=-1
guesses = 1
while(a!=n):
    a = int(input("Guess the number:"))
    if(a>n):
        print("Lower Number Please")
        guesses = guesses+1
    elif(a<n):
        print("Higher Number Please")
        guesses=guesses+1

print(f"you have guessed the number {n} correctly in {guesses} attempts")
def score(guesses):
    try:
       
        with open("highest-score.txt", "r") as file:
            highest_score = file.read()
            if highest_score != "":
                highest_score = int(highest_score)
            else:
                highest_score = float('inf')  
    except FileNotFoundError:
        
        highest_score = float('inf')

    print(f"Current highest score: {highest_score} guesses.")
    
    
    if guesses < highest_score:
        
        with open("highest-score.txt", "w") as file:
            file.write(str(guesses))
        print(f"New highest score saved! {guesses} guesses.")
    else:
        print(f"The highest score remains {highest_score} guesses.")

score(guesses)

    
    
