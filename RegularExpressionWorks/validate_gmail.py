

# validate gmail

# lowercase
# starts with an alphabet
# numbers optional
# before at 64 characters max.
# @gmail.com


from re import fullmatch

pattern="[a-z]+[a-z0-9]{5,63}@gmail.com"

gmail_id=input("Enter the gmail:")

matcher=fullmatch(pattern,gmail_id)

print("Invalid" if matcher==None else "Valid")  