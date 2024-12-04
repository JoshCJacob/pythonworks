class Person:

    name=str

    age=str

    def __init__ (self,name,age):

        self.name=name

        self.age=age
    
    @property
    def get_age(self):

        print(self.age)

    @property
    def get_name(self):

        print(self.name)


person_instance=Person("hari",26)

person_instance.get_name


# normal method gives to decorator we using here is property decorator