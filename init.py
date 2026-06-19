class Emplouyee:
   
    language = "py"
    salary = 12000

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print(" creating object")

    def getInfo(self):
        print(f" The language is {self.language}. the salaty is {self.salary}")

    def greet(self):
        print("goood morining")
harry = Emplouyee("HArry", 130000, "javascripts")
harry.name = "Arbaj"
print(harry.name, harry.salary)