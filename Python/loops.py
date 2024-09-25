# for i in range(1,10):
#     print(i)

# i=0
# while i<=10:
#     print(i)
#     i=i+1


# print the content of list using whilw loop, for loop

# listitem=[1,5,6,9,8,"harrteue","dhjdkcgd","dhb jchdf",True,False]

# for i in listitem:
#     print(i)

# i=0
# while(i<len(listitem)):
#     print(listitem[i])
#     i=i+1


# print  1 to 100 with 4 gap

# for i in range(1,100,4):
#     print(i)


# For loop with else statement

# for i in range(1,10):
#     print(i)
# else:
#     print("Done..")


# Check Prime Number

# num= int(input("Enter a numbr"))

# for i in range(2,num):
#     if(num%i==0):
#          print("Not a prime")
#          break
# else: print("number is prime")



#                                                                 *****
#                                                                 *   *
#                                                                 *   *
#                                                                 *   *
#                                                                 *****

# n=int(input("Enter a number"))

# for i in range(0,n):
#     ans=""
#     for j in range(0,n):
#         if(i==0 or j==0 or i== n-1 or j==n-1): ans+="*"
#         else: ans+=" "
#     print(ans)


# print multiplication table in reverse order

n=int(input("Enter A number :"))
for i in range(10,0,-1):
    print(f"{n} X {i} = {n*i}")