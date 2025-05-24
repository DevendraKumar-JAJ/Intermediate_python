class Acc:
  def __init__(self,name,acc_num,c_id,bal):
    self.__c_name=name
    self.__acc_num=acc_num
    self.__c_id=c_id
    self.__balance=bal
  
  def showAcc(self):
    return self.__c_name,self.__acc_num,self.__c_id,self.__balance
  
  def withdrow(self,amount):
    if amount>0:
      if self.__balance>=amount:
        self.__balance-=amount
        return self.__balance
      else:
        return -1
      
  def deposit(self,amount):
    if amount>0:
      self.__balance+=amount
      return self.__balance

def main():
  accList=[]
  for i in range(1000):
    choice=input("Do you want to open acc [y/n] : ")
    if  choice=='y' or choice=='Y':
      name=input("Enter your name : ")
      accRange=range(10000,99999)
      acc_num=accRange[i]
      c_id=i
      while True:
        try:
            bal = int(input("Opening Balance : "))
            if bal >= 500:
                break
            else:
                print("Minimum balance required is 500.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
      accList.append(Acc(name,acc_num,c_id+1,bal))
      print(f"Your Account number : {acc_num} And customer Id : {c_id+1}")
      while True:
        while True:
          try:
            choice=int(input("Choose your operation [ 1 ShowAccDetail | 2 WithdrowAmount | 3 DepositAmount | 4 Exit ] : "))
            if choice ==1 or choice==2 or choice== 3 or choice==4:
              break
          except ValueError:
            pass
        match(choice):
          case 1:
            while True:
              try:
                acc_num=int(input('Enter account number : '))
                if acc_num>=10000 or acc_num<=99999:
                  break
              except ValueError:
                pass
            for acc in accList:
              c_name,c_acc_num,c_id,balance = acc.showAcc()
              if c_acc_num  ==acc_num:
                c_name,acc_num,c_id,balance=acc.showAcc()
                print(f"Name : {c_name}, AccountNum : {acc_num}, CustomerId : {c_id}, Current Bal : {balance}")
                break
          case 2:
            while True:
              try:
                acc_num=int(input('Enter account number : '))
                if acc_num>=10000 or acc_num<=99999:
                  break
              except ValueError:
                pass
            while True:
              try:
                amm=int(input("Enter amount : "))
                if amm>0:
                  break
              except ValueError:
                pass
            for acc in accList:
              c_acc_num = acc.showAcc()[1]
              print(c_acc_num)
              if c_acc_num ==acc_num:
                amm=acc.withdrow(amm)   
                if amm==-1:
                  print("No sufficient amount ")
                else:
                  print("Amount left : ",amm)    
                break
          case 3:
            while True:
              try:
                acc_num=int(input('Enter account number : '))
                if acc_num>=10000 or acc_num<=99999:
                  break
              except ValueError:
                pass
            while True:
              try:
                amm=int(input("Enter amount : "))
                if amm>0:
                  break
              except ValueError:
                pass
            for acc in accList:
              c_acc_num = acc.showAcc()[1]
              if c_acc_num==acc_num:
                amm=acc.deposit(amm)  
                print("Total Amount : ",amm)    
                break
          case 4:
            break
          case _ :
            pass
    elif choice=='n' or choice=='N':
      break
if __name__=='__main__':
  main()