


from re import fullmatch

date=input("Enter the date:")

pattern="([1-9]|0[1-9]|1[0-2])"
# 01,02,,,123456789,10,11,12


matcher=fullmatch(pattern,date)

if matcher==None:

    print("Invalid")

else:

    print("Valid")    




