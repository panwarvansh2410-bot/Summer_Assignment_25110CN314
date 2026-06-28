class Bank:
    def __init__(self,account_number,account_holder_name,account_type,balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type = account_type
        self.balance = balance

    def create_account(self):
        print("account number = ",self.account_number)
        print("account holder = ",self.account_holder_name)
        print("account type = ",self.account_type)

    def deposit(self):
        
        deposit= int(input("enter amount to be deposited :"))
        self.balance += deposit
        print("amount deposited successfully. ")

    def withdraw(self):
        
        withdrawl = int(input("enter amount to be withdrawl :"))
        if withdrawl <=self.balance:
            self.balance -= withdrawl
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")
    
    

    def check_balance(self):
        print("current balance =",self.balance)


    def bank_details(self):
        print("account number = ",self.account_number)
        print("account holder = ",self.account_holder_name)
        print("account type = ",self.account_type)
        print("balance = ",self.balance)

bn = Bank(101,'suresh','savings',6000)
bn.withdraw()  
bn.check_balance() 
bn.bank_details()     




        