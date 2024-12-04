#create two paramters

def sum(num1,num2):
    result=num1+num2

    print(result)

sum(100,200)




# sub(num1,num2)

def sub(num1,num2):
    result=num1-num2

    print(result)

sum(10,5)    


#multiplication(num1,num2)

def multiplication(num1,num2):
    result=num1*num2
    print(result)

multiplication(12,5)



#division(num1,num2)

def div(num1,num2):
    result=num1//num2
    print(result)

div(10,5)    








#create a fun   last_didgit_max with num1,num2 parameters
#num1=123
#num2=872



def last_digit_max(num1,num2):
    num1_last_digit=num1%10
    num2_last_digit=num2%10
    print(num1 if num1_last_digit>num2_last_digit else num2)
print(last_digit_max(123,871)) 


#create a function is_prime(num)

#create function factorial(num) 





    


    
    

    




def factorial(num):

    fact=1

    for i in range(1,num+1):

        fact=fact*1

    return fact

result=factorial(3)
  
print(result)


