import random

# # file open

# f=open("abc.txt")
# data=f.read()
# print(data)
# f.close()


# # write a file

# st="Hey You Are Amazing"

# ff=open("abc2.txt","w")
# ff.write(st)
# ff.close


# def game():
#     score=random.randint(0,50)
#     print("The Game is Plauing...")
#     print(f"your Score is {score}")
#     return score

# game_score=game()
# f=open("HiScore.txt")
# HiScore=f.read()
# if(HiScore!=""):
#     HiScore=int(HiScore)
# else:
#     HiScore=0
# f=open("HiScore.txt","w")

# if(HiScore<game_score):
#     f.write(str(game_score))
# f.close()



# generate multiplication table from 2 to 20 and store it in different files

def generateMultiplicationTable(a):
    table=""
    for j in range(1,11):
        table+=f"{a} x {j} = {a*j} \n"
        # print(f"{a} x {j} = {a*j}")
    f=open(f"table/table_{a}.txt","w")
    f.write(table)


for i in range(2,21):
    generateMultiplicationTable(i)