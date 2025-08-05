import random 
n=random.randint(1,100)
a=-1
guesses=1
while (a!=n):
    
    a=int(input("ENTER THE NUMBER:"))
    if(a>n):
        print("LOWER NUMBER PELASE")
        guesses+=1
    elif(a<n):
        print("HIGHER NUMBER PLEASE")
        guesses+=1
print(f"YOU GUESSED THE NUMBER({n}) IN{guesses} attempts")

    