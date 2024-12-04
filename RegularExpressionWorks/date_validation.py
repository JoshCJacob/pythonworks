


from re import fullmatch

pattern="(0?[1-9]|[12][0-9]|3[01])"

date=input("Enter the date:")

matcher=fullmatch(pattern,date)

print("INvalid" if matcher==None else "Valid")    