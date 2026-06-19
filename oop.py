'''class Programmer:
    company = "Microsoft"
    def __init__(self ,name, salry, pincode):
        self.name = name
        self.salry = salry
        self.pincode = pincode
        
p = Programmer("Arbaj khan", 12000, 274404)
print(p.name, p.salry,p.pincode,p.company)     '''

'''
class Calculator:
    def __init__(self,n):
        self.n = n
        
    def square(self):
        print(f"the square is {self.n*self.n}")
    def cube(self):
        print(f"the cube is {self.n*self.n}")
    def squareroot(self):
        print(f"the sqrt is {self.n**self.n}")

a = Calculator(4)
a.square()
a.cube()
a.squareroot() '''

'''
class Demo:
    a = 4 

o = Demo()
print(o.a)
o.a = 0
print(o.a)
print(Demo)    '''

from  random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
        
    def book(self,  fro, to):
        print(f" Ticket is booked in train no:{self.trainNo} from {fro} to {to}")
        
    def getStatus(self):
        print(f"TrainNo no : {self.trainNo} is runnig on time")

    def getFare(self , trainNo, fro, to):
        print(f" ticket isin tain no :{self.trainNo} from {fro} to {to} is to {randint(222,5555)}")



t = Train(12399)
t.book("Rampur", "delhi")        
t.getStatus()


         


     
