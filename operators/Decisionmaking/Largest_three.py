#Largest among three numbers

num1=int(input("enter the num1:"))

num2=int(input("enter the num2:"))

num3=int(input("enter the num3:"))


if num1>num2 and num1>num3:

    print("num1 is largest")

elif num2>num1 and num2>num3:

    print("num2 is largest")

elif num3>num2 and num2>num1:

    print("num3 is largest") 

elif num1==num2 and num1==num3:

    print("these all are equal")   