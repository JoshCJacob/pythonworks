



class BankAccount:

    def __init__(self,customer_name,mpin,account_type,balance):

        self.customer_name=customer_name

        self.__mpin=mpin

        self.account_type=account_type

        self.__balance=balance    

    def get_balance(self): 

        print(self.__balance)   

    def __str__(self):

        return self.customer_name
    
bank_account_instance=BankAccount("Hari",43566,"Savings",30000)    

print(bank_account_instance.mpin)




# the class we are initilaize the mpin&balance but outside the class we are hiding the mpin&balance
# public > private change it