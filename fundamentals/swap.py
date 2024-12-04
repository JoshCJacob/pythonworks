#create a python file swap.py

#num1=100
#num2=200

#write a python program to print swap these two numbers


num1=100

num2=200

#values b4 swapping num1=100,num2=200

print(f"values b4 swapping num1={num1},num2={num2}")#num1=100,num2=200

#logic1

# dummy=num1 #dummy=temp

# num1=num2

# num2=dummy

#logic 2

num1=num1+num2 #num1=100+200=300

num2=num1-num2 #num2=300-200=100

num1=num1-num2 #num1=300-100=200

print(f"values after swapping num1={num1},num2={num2}")
