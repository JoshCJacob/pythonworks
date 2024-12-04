

# "self" keyword is used for current instance pointing


# "super" keyword is used for parent(for parent class calling)



class SuperHero:
 
   name=str

   suit=str

   def __init__(self,name,suit):

     self.name=name

     self.suit=suit


   def __str__(self):
      
      return self.name
    

class SpiderMan(SuperHero):
  
  def __init__(self,name,suit):
     
     super().__init__(name,suit)


  def super_power(self):
     
     print("spidersense","web shooting","sticky hands")


# spiderman_instance=SpiderMan("SpiderMan","SpideySuit")
     
# print(spiderman_instance)

# spiderman_instance.super_power()


class MinnalMurali(SuperHero):
   
   def __init__(self, name, suit):
      
      super().__init__(name,suit)

   def super_power(self):
      
      print("running","jumping","reflex")

minnalmurali_instance=MinnalMurali("MinnalMurali","MinnalSuit")

print(minnalmurali_instance)

minnalmurali_instance.super_power()
      







