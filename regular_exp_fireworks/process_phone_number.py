
from re import fullmatch

f=open("C:\\Users\\joshc\\OneDrive\\Desktop\\Pythonworks\\regular_exp_fireworks\\phone_number.txt")

for line in f:

    phone=line.rstrip("\n")

    pattern="(91)?[0-9]{10}"   #"91 is optional and 0-9 any number with 10 number"

    matcher=fullmatch(pattern,phone)

    if matcher !=None:

        print(phone)

        