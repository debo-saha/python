## Q 1

# class student:
#     name=""
#     age=0
#     grade=''
#     def get_grade(self):
#         print(self.grade)
#     def get_info(self):
#         print(f'Name: {self.name}, Age: {self.age}.')
# student1=student()
# student1.name="debo"
# student1.age=55
# student1.grade='A++'
# student1.get_info()
# print(student1.name)


## Q 2

# class rectengular:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         return print(f' Area : {self.length * self.width}')
#     def perimeter(self):
#         return print(f' Perimeter : { 2*(self.length + self.width)}')
# rec1=rectengular(5,6)
# rec1.area()
# rec1.perimeter()


## Q 3

# class BankAccount:
#     def __init__(self,owner,balance=100):
#         self.owner=owner
#         self.balance=balance
#     def deposit(self):
#         return print(f' diposit : {self.balance + 1000}')
#     def withdraw(self):
#         if(self.balance>=1000):
#             return print(f' withdraw : {self.balance-1000}')
#         else:
#             print("Insuficient Balance")
#     def get_balance(self):
#         print(self.balance)
# rec1=BankAccount('amitd',100)
# rec1.deposit()
# rec1.withdraw()
# rec1.get_balance()


## Q 4

# class book:
#     def __init__(self,title,author,year):
#         self.title=title
#         self.author=author
#         self.year=year
#     def area(self):
#         return print(f' Area : {self.length * self.width}')
#     def perimeter(self):
#         return print(f' Perimeter : { 2*(self.length + self.width)}')
# rec1=rectengular(5,6)
# rec1.area()
# rec1.perimeter()



## Q 5

class Car:
    def __init__(self, make, model, year, mileage=0.0):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
    def drive(self):
        self.mileage += 100
        return print(self.mileage)
    def get_details(self):
        return print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Mileage: {self.mileage}")
c1=Car("BMW", "I5", "2020", 260)
c1.drive()
c1.get_details()
