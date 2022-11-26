def add(x,y):
  return x+y
def sub(x,y):
  return x-y
def Withdraw(CashAvilable,WithdrawCash):
   CashBalance = sub(CashAvilable,WithdrawCash)
   return CashBalance 
     
def Deposite(CashAvilable,DepositeCash):
  CashBalance = add(CashAvilable,DepositeCash)
  return CashBalance
a = ("                                                            WElCOME TO SARAS NATIONAL BANK ATM")

b = ("Mr.John")
print(a)
print("____________________________________________________________________________________________________________________________________________________________________________")
print(" ")
print(" ")
print("Name:",b)
print(" ")
c=float(100000)
print("Cash Avilable In Savings Account: Rs.","{0:.2f}".format(c))
print("   ")
print("1.Withdraw cash: ")
print(" ")
print("2.Deposit cash: ")
print(' ')
choice = input("Select the option 1/2")

if choice == "1":
  print(" ")
  d = float(input("Enter Amount Withdraw: Rs."))
  print(" ")
  print( "Current Balance Status: Rs.","{0:.2f}".format(Withdraw(c,d)))
elif choice == "2":
  d = float(input("Enter Amount Deposite:"))
  print(" Current Balance Status: Rs.","{0:.2f}".format(Deposite(c,d)))

else:
  print("contact to branch of bank")
z = Withdraw(c,d)
if choice == "1" and z<5000:
  print(" ")
  print("Low Balance")
else:
  print("contact to branch of your bank")