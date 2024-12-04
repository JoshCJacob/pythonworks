


class Parent:

    def vehicles(self):

        self.bikes=["jawa350","ntorque"]

        return self.bikes
    

class Child(Parent):

    def vehicles(self):

        self.bikes=super().vehicles() #["jawa350","ntorque"]

        self.bikes.append("hunter")
        
        return self.bikes
    
child_instance=Child()

print(child_instance.vehicles())


