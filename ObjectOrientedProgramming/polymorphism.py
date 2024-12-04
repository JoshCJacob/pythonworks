# polymorphism
# perform a single task in different way


# two topics Under polymorphism
# method overloading
# method_overriding


# python is interperted language

# method overloading(same method name and different number of parameters)
# not supporting this method in python(implementing here as *args and keyword)
# it provides we call the method overloading in the method(*args)


class Operation:


 def add(self,num1,num2):
     
    print(num1+num2)

 def add(self,num1,num2,num3):

   print(num1+num2+num3)


obj=Operation()

obj.add(10,20,30)


obj.add(10,20) #the recently add only working.it is not working

