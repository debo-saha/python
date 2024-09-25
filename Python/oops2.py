# Inheritance 

# class employee:
#     company="ITC"
#     def showDetails(self):
#         print(f"The Name is {self.company}")

# class programmer(employee):
#     company="ITC Interforce"
#     def showDetails(self):
#         print(f"This is also a good one")

# a=employee()
# print(a.company)
# b=programmer()
# print(b.company)


## Multiple InHeritance

# class Employee:
#     def __init__(self, lang="Python"):
#         self.lang = lang
        
#     def show(self):
#         print(f"This is a show {self.lang}")

# class Coder:
#     def __init__(self, salary=120000):
#         self.salary = salary
        
#     def show2(self):
#         print(f"This is a salary {self.salary}")

# class Programmer(Employee, Coder):
#     def __init__(self, lang="Python", salary=120000, company="ITC"):
#         Employee.__init__(self, lang)
#         Coder.__init__(self, salary)
#         self.company = company
        
#     def abc(self):
#         print(f"HII how are you {self.company}")

# a = Employee()
# b = Programmer()

# b.show()   # This will print: This is a show Python
# b.show2()  # This will print: This is a salary 120000
# b.abc()    # This will print: HII how are you ITC



# Multi lEvel Inheritance

# class programmer:
#     a=1
    
# class employee(programmer):
#     b=2

# class maneger(employee):
#     c=3

# o=programmer()
# print(o.a)
# o=employee()
# print(o.a,o.b)
# o=maneger()
# print(o.a,o.b,o.c)



## Super Constructor

# class programmer:
#     a=1
#     def __init__(self):
#         print("This is Programmer constructor")

# class employee(programmer):
#     b=2
#     def __init__(self):
#         print("This is employee constructor")

# class maneger(employee):
#     c=3
#     def __init__(self):
#         super().__init__() # Thiis Will Call The previious one constructor
#         print("This is maneger constructor")

# o=programmer()
# print(o.a)
# o=employee()
# print(o.b)
# o=maneger()
# print(o.c)





## Class Method

# class employee:
#     a=1
#     @classmethod
#     def show(self):
#         print(f"The Value of a is : {self.a}")

# o=employee()
# o.a=5 ## After assigning the value if we want to get the previous a value then we use ((@classmethod))
# o.show()


## Abstruction And Incapsulation
 
class employee:
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

e=employee()
e.name="Debojyoti kumar Saha"

print(e.name)


## Operator OverLoading

class number:
    def __init__(self,n):
        self.n=n
    def __add__(self,num):
        return self.n+num.n
    def __mul__(self,num):
        return self.n*num.n
    def __sub__(self,num):
        return self.n-num.n
    def __truediv__(self,num):
        return self.n/num.n
    def __floordiv__(self,num):
        return self.n//num.n
n=number(58)
m=number(6)
print(n+m)
print(n-m)
print(n*m)
print(n/m)
print(n//m)