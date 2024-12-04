


# initialize attributes (instance variables)
# constructor

# initliazing instance variable constructor
# python(__init__)=>constructor(set_student)=<< we using at this time"__init__

class Mobile:

    name:str

    price:int

    brand:str

    def __init__(self,name,price,brand):

        self.name=name

        self.price=price

        self.brand=brand

    def display(self):

        print(self.name,self.price,self.brand)

mobile_instance1=Mobile("VIVOV20SE",25000,"VIVO")

mobile_instance1.display()

