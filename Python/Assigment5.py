## Q1

# data = [('apple', 3), ('banana', 1), ('orange', 2)]
#
# sorted_data=sorted(data, key=lambda x :x[0],reverse=True)
# print(sorted_data)


## Q2

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filter_this=list(filter(lambda x:x>5,numbers))
# print(filter_this)

# # Q3

# class Fibo:
#     def __init__(self,n):
#         self.n=n
#         self.index=0
#         self.a,self.b=0,1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index>self.n:
#             raise StopIteration
#         elif self.index==0:
#             self.index+=1
#             return 0
#         elif self.index==1:
#             self.index+=1
#             return 1
#         else :
#             self.a,self.b=self.b,self.a+self.b
#             self.index+=1
#             return self.b
#
# fiboseries= Fibo(5)
# # print(fiboseries)
# for num in fiboseries:
#     print(num)




class ReverseIterator:
    def __init__(self,listdata):
        self.listdata=listdata
        self.index=len(self.listdata)-1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index<0:
            raise StopIteration
        else :
            val=self.listdata[self.index]
            self.index-=1
            return val

numbers = [1, 2, 3, 4, 5]
reverse=ReverseIterator(numbers)
for i in reverse:
    print(i)

