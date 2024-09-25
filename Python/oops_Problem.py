#  Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class twoDVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"The 2-D Vector is {self.i}i + {self.j}j")

class threeDVector(twoDVector):   
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
        print(f"The 3-D Vector is {self.i}i + {self.j}j + {self.k}k")

a=twoDVector(2,3)
a.show()
b=threeDVector(5,6,8)
b.show()


# Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def __add__(self,num):
        return complex(self.r+num.r , self.i+num.i)
    def __mul__(self,num):
        return complex(self.r * num.r , self.i*num.i)
    def __str__(self):
        return f"{self.r}+{self.i}i"

p=complex(5,6)
q=complex(1,2)
print(p+q)
print(p*q)
