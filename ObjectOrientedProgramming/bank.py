

# bank(accno,balance,acctype,customer_name)  
# [initiliaze,deposit(amount),withdraw(amount),get_balance()]


class Bank:

    customer_name:str

    acctype:str

    accnumber:int

    balance:int

    def __init__(self,customer_name,acctype,accnumber,balance):

        self.customer_name=customer_name

        self.acctype=acctype

        self.accnumber=accnumber

        self.balance=balance

    def deposit(self,amount):

        self.balance+=amount

        print(f"your account{self.accnumber}has been credited with amount {amount} avl bal{self.balance}")


    def withdraw(self,amount):

        if self.balance<amount:

            self.balance-=amount

            print(f"your account{self.accnumber}has been debited with amount {amount} avl bal{self.balance}")

        else:

            print("insuffiecnt balance")

    def get_balance(self):

        print("your aval bal",self.balance)


customer_instance1=Bank("Assed","Cuurent",35378346483,4500)

customer_instance1.withdraw(1000)