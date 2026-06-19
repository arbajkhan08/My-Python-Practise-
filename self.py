class Emplouyee:
   
    language = "py"
    salary = 12000

    def getInfo(self):
        print(f" The language is {self.language}. the salaty is {self.salary}")

    def greet(self):
        print("goood morining")
harry = Emplouyee()
# harry.name = "Arbaj"
harry.getInfo()
harry.greet()