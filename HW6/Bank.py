
from enum import Enum
class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2
######################

class BankAccount():
    "Class Bank Account specifying owner and Account type"
    def __init__(self, owner, accountType):
        self.owner = owner
        self.balance = 0
        self.AccountType = accountType
        
    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError("Cannot withdraw a negative value")
        if amount > self.balance:
            raise AttributeError("Insufficient funds")
        
        self.balance = self.balance - amount
        print("Withdrawal of ",amount," from account ",self.AccountType.name,". Remaining balance ", self.balance)
    
    def deposit(self,deposit):
        if deposit <=0:
            raise ValueError
        else:
            self.balance +=deposit
            print("Deposit of ", deposit, " and new balance is ", self.balance)
        
    def __str__(self):
        
        return "Owner of account "+ self.owner + " and account type is " + self.AccountType.name
    
    def __len__(self):
        #return the balance of acc
        return self.balance

######################

class BankUser():
    
    def __init__(self,owner):
        self.owner = owner
        self.savings = 0
        self.checking = 0
        self.myCaccount = 0
        self.mySaccount = 0
        
    def addAccount(self, accountType):
        #Check what account type and then whether the account is there
        if accountType == AccountType.SAVINGS:
            if self.savings == 0:
                self.savings = 1
                self.mySaccount = BankAccount(self.owner,accountType)
            
            else:
                raise ValueError("You already have a savings account")
                
        elif accountType == AccountType.CHECKING:
            if self.checking == 0:
                self.checking = 1
                self.myCaccount = BankAccount(self.owner,accountType)
            
            else:
                raise ValueError("You already have a checking account")
        else:
            raise ValueError("Account type is not valid")
    
    def getBalance(self,accountType):
        if accountType == AccountType.SAVINGS:
            if self.mySaccount == 0:
                raise ValueError("No savings account")
            else:
                return self.mySaccount.balance
            
        elif accountType == AccountType.CHECKING:
            if self.myCaccount == 0:
                raise ValueError("No checking account")
            else:
                return self.myCaccount.balance
        else:
            raise ValueError("Invalid account type inserted")
    
    def deposit(self,accountType,amount):
        if accountType == AccountType.SAVINGS:
            if self.mySaccount == 0:
                raise ValueError("No savings account")
            else:
                return self.mySaccount.deposit(amount)
            
        elif accountType == AccountType.CHECKING:
            if self.myCaccount == 0:
                raise ValueError("No checking account")
            else:
                return self.myCaccount.deposit(amount)
        
        else:
            raise ValueError("Invalid account type inserted")
            
    def withdraw(self,accountType,amount):
        #analogous to deposit
        if accountType == AccountType.SAVINGS:
            if self.mySaccount == 0:
                raise ValueError("No savings account")
            else:
                return self.mySaccount.withdraw(amount)
            
        elif accountType == AccountType.CHECKING:
            if self.myCaccount == 0:
                raise ValueError("No checking account")
            else:
                return self.myCaccount.withdraw(amount)
        
        else:
            raise ValueError("Invalid account type inserted")
        
######################

def ATMSession(bankUser):
    def interface():
        while True:
            user_input = int(input('Enter Option: \n 1)Exit \n 2)Create Account \n 3)Check Balance \n 4)Deposit \n 5)Withdraw \n'))
            
            #Exit
            if user_input == 1:
                print("Exiting...")
                break
            
            #Create Account
            elif user_input == 2:
                try:
                    choice = int(input("\nEnter Option :\n1.Checking Account\n2.Savings Account\n\n"))
                    if (choice >2) or (choice<1):
                        raise ValueError
                except ValueError:
                    print("\n Invalid choice, retry")
                if choice ==1:
                    try:
                        bankUser.addAccount(AccountType.CHECKING)
                        print("Checking account created!")
                    except ValueError:
                        print("Checking already exists!")
                if choice ==2:
                    try:
                        bankUser.addAccount(AccountType.SAVINGS)
                        print("Savings account created!")
                    except ValueError:
                        print("Savings already exists!")
                
            #Check balance
            elif user_input == 3:   
                try:
                    choice = int(input("\nEnter Option :\n1.Checking Account\n2.Savings Account\n\n"))
                    if (choice >2) or (choice<1):
                        raise ValueError
                except ValueError:
                    print("\n Invalid choice, retry")
                if choice ==1:
                    try:
                        balance = bankUser.getBalance(AccountType.CHECKING)
                        print("Checking balance: ", balance)
                    except ValueError:
                        print("No checking account!")
                if choice ==2:
                    try:
                        balance = bankUser.getBalance(AccountType.SAVINGS)
                        print("Savings balance: ", balance)
                    except ValueError:
                        print("No savings account!")
            
            #Deposit
            elif user_input == 4:
                try:
                    choice = int(input("\nEnter Option :\n1.Checking Account\n2.Savings Account\n\n"))
                    if (choice >2) or (choice<1):
                        raise ValueError
                except ValueError:
                    print("\n Invalid choice, retry")
                    
                if choice ==1:
                    try:
                        deposit_amt = int(input("\nEnter Integer Amount, Cannot be Negative :\n"))
                        if deposit_amt < 0:
                            raise ValueError
                    except ValueError:
                        print("Amount invalid!")
                    if deposit_amt >= 0:
                        try:
                            bankUser.deposit(AccountType.CHECKING,deposit_amt)
                        except ValueError:
                            print("No checking account")
                        
                if choice ==2:
                    try:
                        deposit_amt = int(input("\nEnter Integer Amount, Cannot be Negative :\n"))
                        if deposit_amt < 0:
                            raise ValueError
                    except ValueError:
                        print("Amount invalid!")
                    if deposit_amt >= 0:
                        try:
                            bankUser.deposit(AccountType.SAVINGS,deposit_amt)
                        except ValueError:
                            print("No savings account")
            #Withdraw
            elif user_input == 5:
                try:
                    choice = int(input("\nEnter Option :\n1.Checking Account\n2.Savings Account\n\n"))
                    if (choice >2) or (choice<1):
                        raise ValueError
                except ValueError:
                    print("\n Invalid choice, retry")
                
                if choice ==1:
                    try:
                        withdraw_amt = int(input("\nEnter Integer Amount, Cannot be Negative :\n"))
                        if withdraw_amt < 0:
                            raise ValueError
                    except ValueError:
                        print("Amount invalid!")
                    
                    if withdraw_amt >= 0:
                        try:
                            bankUser.withdraw(AccountType.CHECKING,withdraw_amt)
                    
                        except ValueError:
                            print("No checking account!")
                    
                        except AttributeError:
                            print("not enough funds!")
                        
                if choice ==2:
                    try:
                        withdraw_amt = int(input("\nEnter Integer Amount, Cannot be Negative :\n"))
                        if withdraw_amt < 0:
                            raise ValueError
                    except ValueError:
                        print("Amount invalid!")
                    if withdraw_amt >= 0:
                        try:
                            bankUser.withdraw(AccountType.SAVINGS,withdraw_amt)
                    
                        except ValueError:
                            print("No savings account!")
                    
                        except AttributeError:
                            print("not enough funds!")
            else:
                print("Not a valid choice, try again")
                
                
    return interface