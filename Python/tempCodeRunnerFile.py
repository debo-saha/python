# print("hii")
#
# def fib(n):
#     fibs=[0,1]
#     while len(fib_sequence) < n:
#         fibs.append(fibs[-1]+fibs[-2])
#     return fib_sequence
# n=int(input("enter a number"))
# fibbo=fib(n)
# for i in fibbo:
#     print(i)


# books={
#     "title":888,
#     "author":8554,
#     "year":1899}
#
#
# # for i in books:
# print(sum(books.values())/len(books

# num=int(input("dnjfd"))
# ll=[]
# for i in range(num):
#     a=int(input("kbkb"))
#     ll.append(a)
# print(ll)
#
#
# class Reverse:
#     def __init__(self,aa):
#         self.aa=aa
#         self.index=len(aa)-1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index<0:
#             raise StopIteration
#         else:
#             val=self.aa[self.index]
#             self.index-=1
#             return val
# numbers=[5,9,6,3,2,5,8,1]
#
# reverse=Reverse(numbers)
# for i in reverse:
#     print(i)
#
class fibbo:
    def __init__(self,n):
        self.n=n
        self.index=0
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>self.n:
            raise StopIteration
        elif self.index==0:
            self.index+=1
            return 0
        elif self.index==1:
            self.index+=1
            return 1
        else :
            self.a,self.b=self.b,self.a+self.b
            self.index += 1
            return self.b

fib=fibbo(5)
for i in fib :
    print((i))




