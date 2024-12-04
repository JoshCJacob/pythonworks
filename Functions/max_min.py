#create a function max_two with two parameter num1,num2 return largest number
#create a function min_two with two parameter num1,num2 return smallest number


def max_two(num1,num2):
    return num1 if num1>num2 else num2 

print(max_two(100,200))



def min_two(num1,num2):
    return num1 if num1<num2 else num2

print(min_two(100,200))








"""create a function multplication table(number,n)
print multiplication table of number till n"""



def multiplication_table(number,n=10):
    for i in range(1,n+1) :
     print(f"{i} * {number} = {i*number}")

multiplication_table(5)   




#create a function exponent with two paramters num1,n


def exponent(number,n):  #(number,n=2)
   
   return number**n

print(exponent(6,2))  #(exponent(6))



#create a function smart_sub with 3 parameters num1,num2.reverse
#reverse takes boolean value
#if reverse==True then return num2-num1 else return num1-num2


def smart_sub(num1,num2,reverse):
   
   
   return num2-num1 if reverse==True else num1-num2
   
   
print(smart_sub(10,20,True))    



 
   





