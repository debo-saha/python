# def print_sum(sum_list):
#     sum=0
#     for i in sum_list:
#         sum+=i
#     print(sum)

# sum_list=list(map(int,input().split(" ")))
# print_sum(sum_list)



# def factorial(a):
#     fact=1
#     for i in range(1,a+1):
#         fact*=i
#     print(fact)

# num=int(input("Enter A number :"))
# factorial(num)


# def Print_fibo_sequence(a):
#     sum=0
#     if (a==1):
#         return 1
#     elif(a==2):
#         return 1
#     else:
#         sum= (Print_fibo_sequence(a-1)+Print_fibo_sequence(a-2))
#     return sum

# num=int(input("Enter A number :"))
# for i in range(1,num+1):
#     print(Print_fibo_sequence(i))



# def palindromic_checker(string):
#     if(string[::-1]==string[::1]):
#         print("Palindromic")
#     else:
#         print("Not A Palindromic")
# palindromic_checker("aaa")


# def Prime_num_check(num):
#     flag=0
#     for i in range(2,num):
#         if(num%i==0):
#             flag=1
#             return flag
#             break
#         return flag
# ans=Prime_num_check(5)

# if(ans):
#     print("This is not Prime")
# else:
#     print("This is Prime")



# def second_largest(list):
#     list.sort()
#     print(list[-2])
# list=[2,5,8,9,6,20]
# second_largest(list)


def GCD_calculator(a, b):
    while b != 0 and a!=0:
        a, b = b, a % b
    print(a)

GCD_calculator(3, 6)



# def Prime_num_check(num):
#     flag=0
#     for i in range(2,num):
#         if(num%i==0):
#             flag=1
#             return flag
#             break
#         return flag


# for i in range(2,10):
#     ans=Prime_num_check(i)
#     if(ans):
#         print(f"{i} This is not Prime")
#     else:
#         print(f"{i} This is Prime")



# # def count_length(string):
# #     count=0
# #     for i in string:
# #         count+=1
# #     print(count)
# # count_length("debojyoti")


# def count_length(num):
#     sum=0
#     while(num!=0):
#         # sum+=num%10
        
#         sum+=num%10
#         num=int(num/10)
#         # print(sum)
#     print(sum)
# count_length(55555)

