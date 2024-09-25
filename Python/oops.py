# class employee:
#     language="py"  # This is a class atribute
#     salary=1200000

# haryy=employee()
# haryy.name="Harry vai" # This is an instance atribute
# print(haryy.language,haryy.name)



# self delaration

# class pokemon:
#     power="lightning attack"
#     hp=400
#     def greating(self):
#         print(f"hii {self.power}. your hp {self.hp}")
# # As there is no require of self we can use static method
#     @staticmethod
#     def greet():
#         print("Good Morning")

# pikachuu=pokemon()
# pikachuu.greating()
# pikachuu.greet()



# class pokemon:
#     power="lightning attack"
#     hp=400
#     def greeting(self):
#         print(f"hii {self.power}. your hp {self.hp}")

#     # autometically call
#     def __init__(self): #dunder Method
#         print("HII i am init")

# pikachuu=pokemon()
# pikachuu.greeting()



# make a calculator to calculate square,cube,squareroot

class calculator:
    def __init__(self,number):
        self.number=number
    def square(self):
        print(f"The square is {self.number *  self.number}")
    def cube(self):
        print(f"The Cube is {self.number *  self.number *self.number}")
    def squareRoot(self):
        print(f"The squareRoot is {self.number**(1/2)  }")

a=calculator(36)
a.square()
a.squareRoot()
a.cube()