class Emplopyee:
    a = 1
    @classmethod
    def show(cls):
        print(f" the x class value is {cls.a}")

    @property
    def name(self):
       return self.ename
     

    @name.setter
    def name(self , value):
        self.ename = value 


e =  Emplopyee()
e.a = 45
e.name = 'arbajkhan'
print(e.name)
e.show()
