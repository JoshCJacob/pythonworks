
from re import fullmatch

user_input=input("Enter variable name:")

# startwith an alphabet(lowercase,uppercase)
# any number of alphabets,digits,


pattern="[a-zA-Z][a-zA-z0-9_]*"

matcher=fullmatch(pattern,user_input)#none

if matcher==None:

    print("invalid")

else:

    print("valid")        