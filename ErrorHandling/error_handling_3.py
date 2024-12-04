

num1=int(input("Enter the num1:"))

num2=int(input("Enter the num2:"))

try:                        #it is for error doubtful

    result=num1/num2

    print(result)


except:                      #it is for handling the error

    num2=int(input("Enter the Number:"))

    result=num1/num2

    print(result)


finally:                      #cleanup method


    print("file operation")

    print("db commit")


