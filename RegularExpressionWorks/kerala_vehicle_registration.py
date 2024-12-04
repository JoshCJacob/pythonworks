


# starting with KL

# 2digit

# alphabets minimum1 maximum2

# 4digit



from re import fullmatch

reg_num=input("Enter registration number:")

pattern="(KL)[0-9]{2}[A-Z]{1,2}[0-9]{4}"

matcher=fullmatch(pattern,reg_num)

if matcher==None:

    print("Invalid")

else:

    print("Valid")    




# '|' it is the or case here