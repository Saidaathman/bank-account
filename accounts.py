class BankAccount:
  bank="equity bank"
  branch="machakos"
  def __init__(self,name, balance ,accno):
    self.name=name
    self.balance=balance
    self.accno=accno
shariffa=BankAccount(name="shariffa", balance=100790,accno=11234/90)
caro=BankAccount(name="caro", balance=45689,accno=45678/90)
amina=BankAccount(name="amina", balance=56789,accno=89760/90)
print(shariffa.balance)
print(caro.balance)
print(amina.balance)

#classes          #classes



class BankAccount:
  bank="equity bank"
  
  def __init__(self,first_name,last_name):
    self.first_name=first_name
    self.last_name=last_name
    self.balance=0
    
 #method1   
  def account_name(self):
    name="{} account for {} {}".format(self.bank,self.first_name,self.last_name)
    return name
 
 #method2   
  def deposit(self, amount):
    self .balance+=amount
    if amount>0:
      print("You have deposited {} to your account". format(amount))
    else:
      print("You cannot  deposit  {} into your account".format(amount))
 
 #method3 
  def get_balance(self):
    return("The balance for {} is {} ".format(self.account_name(),self.balance))
  
  #method4
  def withdraw(self,amount):
    amount>0
    if self.balance>=amount:
      self.balance-=amount
      print("You have withdrawn {} from your account".format(amount))
    else:
      print("You cannot withdraw {} from your account".format(amount))  


acc1=BankAccount("maryam","athman")
acc2=BankAccount("said","jamal")
print("---------")
print(acc1.account_name())
print(acc2.account_name())
print("--------")
acc1.deposit(80)
acc2.deposit(50)
acc1.deposit(75)
acc2.deposit(-100)
print("----------")

print(acc1.get_balance())
print(acc2.get_balance())
print("---------")


#quiz.   #  quiz.      # quiz.   # quiz.  

acc3=BankAccount("nahyer","faruk")
acc4=BankAccount("shillah","wendy")
print("--------")
acc3.deposit(100)
acc4.deposit(200)
acc3.deposit(300)
acc4.deposit(400)
print("----------")
acc3.withdraw(500)
acc3.withdraw(600)
acc4.withdraw(700)
acc4.withdraw(800)

print("----------")
print(acc3.get_balance())
print(acc4.get_balance())
  
    