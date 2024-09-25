import random

def checkWinner(a,b):
    if((a==1 and b==2) or (a==2 and b==3)  or (a==3 and b==1)): 
        return 1
    elif(a==b): 
        return -1
    else: 
        return 0

comp=random.randint(1,3)
inp1=input("Enter Your Choise : ")
gameDict={
    "R":1,
    "P":2,
    "S":3
}
inpValue=gameDict[inp1]
# print(inpValue)
# print(comp)
winner=checkWinner(comp,inpValue)
if(winner==-1): print("Draw")
elif(winner==1): print("You Win")
else: print("Computer Win")