class Emoloyee:
    company = "google"
    name = " Default name "
    def show(self):
        print(f"Thr name is {self.name} and the salry id {self.company}")


class Coder:
     language = "Python"
     def printLanguage(self):
         print(f"the Out of all the language is your language:{self.language}")

class Programmer(Emoloyee, Coder):
    company = " ITC infotect"
    def showLanguage(self):
        print(f"the name is {self.name} and thr salarly id {self.name} languyage")


a = Emoloyee()
b = Programmer()


b.show()
b.printLanguage()
b.showLanguage()
