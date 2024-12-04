 #number=51
# is 51 is fibnoacci number?

number=int(input("Enter the number:")) #51

previous=0

current=1

is_fibo=False

for i in range(1,number+1): #0 1 1 2 3 4 8 13 21 34 55 89 144,,,,,,,,,,,,,(51 times printing)

    next=previous+current

    previous=current
    
    current=next

    if next==number:

        is_fibo=True

        break

print(is_fibo)    




