

begin=int(input("enter the limit start:"))

end=int(input("enter limit"))


if begin>end:
    
    begin,end=end,begin

#10,,,,,,,,,,50

i=begin

while(i<=end):

    if i%2==0:

        print(i)

    i+=1


#odd numbers


i=begin

while(i<=end):

    if i%2!=0:

        print(i)

    i+=1