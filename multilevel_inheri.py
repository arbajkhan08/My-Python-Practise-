class Employee:

    def __init__(self):
         print("constructor of Employee")
         
    a = 1
class Pogrammer(Employee):
      
    def __init__(self):
         print("constructor of Programmer")
    b = 2
class Manager(Pogrammer):
     
    def __init__(self):
         super().__init__()
         print("constructor of Manager")
    c = 3


o = Employee()
print(o.a)
 
o = Manager()
print(o.c)