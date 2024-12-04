


# strting with an alphabet from p-t
# in second place must be a number that is \ by 3
# followed by anuy number alphabets,numbers,@

# s6abc
# a6vvhvh


from re import fullmatch

user_input=input("Enter the variable:")

pattern="[p-tP-T][369][a-zA-Z0-9@]*"

matcher=fullmatch(pattern,user_input)

if matcher==None:

    print("Invalid")

else:

    print("valid")    