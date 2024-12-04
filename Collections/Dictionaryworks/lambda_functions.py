
# add number
# def add_number(num1,num2):

#     return num1+num2

# print(add_number(100,200))


# subtrate two numbers

# def cubes(n1,n2):
    
#     return n1-n2

# print(cubes(100,200))





# lambda functions

# lambda functions for adding 2 numbers

add=lambda n1,n2:n1+n2

print(add(100,200))

# lambda function for subtracting 2 numbers

sub=lambda n1,n2:n1-n2

print(sub(10,2))

# lambda function for finding cube for a number

cube=lambda n:n**3

print(cube(2))



# max_two

max_two=lambda str1,str2:str1 if len(str1)>len(str2) else str2

print(max_two("hai","morning"))


# min_two

min_two=lambda str1,str2:str1 if len(str1)<len(str2) else str2

print(min_two("hai","morning"))




# smart_sub

# def smart_sub(num1,num2):
#     return num1-num2 if num1>num2 else num2-num1

smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1

print(smart_sub(30,100))




words=["hello","hai","good","morning","apple"]

# def get_length(w):

#     return len(w)

get_length=lambda w:len(w)

print(max(words,key=get_length))

print(min(words,key=get_length))









