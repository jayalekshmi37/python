class Bankaccount:
  def __init__(self,accno,name,acctype,balance=0):
   self.accno=accno
   self.name=name
   self.acctype=acctype
   self.balance=balance
  def deposit(self,amount):
   if(amount>0):
    self.balance=self.balance+amount
    print("successfull deposit of",amount)
    print("new balance:",self.balance)
   else:
    print("not successfull")
  def withdraw(self,amount):
   if(0<amount<self.balance):
    self.balance=self.balance-amount
   elif(amount>self.balance):
    print("not possible to withdraw")
   else:
    print("invalid")
  def getbalance(self):
   print("current balance:",self.balance)
accno=int(input("enter the account number:"))
name=input("enter your name:")
acctype=input("enter the type of account:")
account1=Bankaccount(accno,name,acctype)
while True:
 print("1.deposit \n2.withdraw \n3.balance \n4.exit")
 ch=int(input("enter your choice:"))
 if(ch==1):
    damount=int(input("enter the amount to be deposited:"))
    account1.deposit(damount)
 elif(ch==2):
     wamount=int(input("enter the amount to be withdraw:"))
     account1.withdraw(wamount)
     account1.getbalance()
 elif(ch==3):
    account1.getbalance()
 elif(ch==4):
  exit(0)
 else:
   print("wrong choice")
