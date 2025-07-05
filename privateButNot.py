
class Acc:
    def __init__(self):
        self.__listt = ["Dev", "Devendra"]

    # returning original list reference
    def showML(self):
        return self.__listt

    # returning shallow copy using slicing
    def showUML(self):
        return self.__listt[:]  # slicing | returning shallow copy

# case first
print("Case first : Returning original list reference")
a1 = Acc()
li = a1.showML()
print(li)
li[0] = "Ratan"  # here data will change
print(a1.showML())

# case second
print("Case second : Returning shallow copy")
a2 = Acc()
li = a2.showUML()
print(li)
li[0] = "Ratan"  # here data will not change
print(a2.showUML())
