class Car:
   
#    attributes of the class

    # name=str

    # brand=str

    # fuel_type=str

# initialization   

    def __init__(self,name,brand,fuel_type):

        self.name=name

        self.brand=brand

        self.fuel_type=fuel_type

#  print

    def display (self):

        print(self.name,self.brand,self.fuel_type)

  
# string representation of an object

    def __str__(self):   #return value is string value

        return self.name


car_instance1=Car("swift","suzuki","petrol")

car_instance1.display()

print(car_instance1)


# string representation of an object
# __str__(self)


