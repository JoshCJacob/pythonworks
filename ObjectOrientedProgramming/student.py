
# initialize attributes (instance variables)
# constructor

# initliazing instance variable constructor
# java(classname)
# javascrpit(constructor)
# python(__init__)=>constructor(set_student)=<< we using at this time"__init__


class Student:

    name:str

    rollnumbetr:int

    age:int

    course:str

    # initializing attributes of Student class

    def set_student(self,name,rollnumber,age,course):

        self.name=name

        self.rollnumbetr=rollnumber

        self.age=age

        self.course=course

    def display(self):

        print(self.name,self.age,self.rollnumbetr,self.course)

# reference_name=ClassName()

student_instance1=Student()

student_instance1.set_student("Josh",22,30,"Python")

student_instance1.display()


