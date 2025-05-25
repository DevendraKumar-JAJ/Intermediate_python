class Greet:
    # constructor 
    def __init__(self,name,age):
        self.name=name
        # protected data member 
        self._age=age
        # private data member 
        self.hii="Hii"
    def greetMe(self):
        print(f"{self.hii}!\n\t{self.name}")

# inheriting Greet class into student class
class Student(Greet):
    #  constructor also a private member function 
    def __init__(self,name ,roll):
        self.roll=roll
        self.name=name

#  polymorphism | Definig another function with the same name of previous function..
    def greetMe(self):
        print(f"Hello!\n\t{self.name}, and your roll is {self.roll}")

    def aboutMe(self):
        print(f"Name : {self.name},  and Roll : {self.roll}\n")
        
    def changeData(self):
        self.name=input('Enter Name : ')
        self.roll=input("Roll : ")

# taking number of objects user want 
size=int(input("Enter number of records you want : "))

# creating empty list
objs = list()

#creating list of objects with defaualt value "",""
for i in range(size):
    objs.append(Student("",""))
    

#  taking object data by the user and change the default data 
j=1
for i in objs:
    print (f"Obj {j}",end=' ')
    i.changeData()
    j+=1
    
    
# liner searching based on name 
def basedOnName(sname):
    j=0
    for i in objs:
        if(i.name==sname):
            return j
        j+=1
    return -1
            

# liner searching based on roll
def basedOnRoll(sroll):
    j=0
    for i in objs:
        if(i.roll==sroll):
            return j
        j+=1
    return -1

#  asking user multiple time want to search or not 
while True:
    choice=input('Do you want to search data [y/n] : ')
    
    # use may enter Y or y if yes 
    if (choice=='y' or choice=='Y' ):
        
        #asking based on
        basedOn=  input('Based on [1 _ Name | 2 _ Roll ] ')
        # based on name
        if (basedOn=='1'):
            name=input("Enter name to search : ")
            obj=basedOnName(name)
            if(obj==-1):
                print ("Data not found")
            else:
                objs[obj].aboutMe()
            
        # based on roll
        elif (basedOn=='2'):
            roll=input("Enter name to search : ")
            obj=basedOnRoll(roll)
            if(obj==-1):
                print ("Data not found")
            else:
                objs[obj].aboutMe()
        
    elif (choice=='n' or choice=='N'):
        break


" Note : Private member | function never inherit or used by the other class or out of class, The protected is inherit by the other class but not used out of the class or inherited class  And The public Data | function  member which is by default created if we not define the access modifer type to the class elements   and it used any where of the program "
