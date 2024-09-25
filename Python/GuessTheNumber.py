import random

num=random.randint(1,100)  
a=-1
numOfGuess=0
while(a!=num): 
    inp=int(input("Enter Your Guess :"))
    numOfGuess+=1
    if(num==inp):
        print(f"You Guessed Correctly in {numOfGuess} Guesses")
        break
    elif(num>inp):
        print(f"High Guess Please!! ")
    elif(num<inp):
        print(f"Lower Guess Please!!")
    
