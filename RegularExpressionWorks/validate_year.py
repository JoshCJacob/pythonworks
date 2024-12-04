# validate years from 1800-2024



from re import fullmatch

pattern="((18|19)[0-9]{2}|200[0-9]|201[0-9]|202[0-4])"

year=input("Enter Year:")

matcher=fullmatch(pattern,year)

print("Invalid" if matcher==None else "Valid")



