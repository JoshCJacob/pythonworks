


expenses=[10000,11000,12000,13000]

for exp in expenses:

    print(exp)


#total_expenses

expenses=[10000,11000,12000,13000]

total=0

for exp in expenses:
    
    total=total+exp

print("total exp=",total)


#max_expense without using max()

expenses=[10000,15000,12000,13000]

max_exp=0

for exp in expenses:

    if exp > max_exp:

        max_exp=exp

print(max_exp)



#min_expense

expenses=[10000,15000,12000,13000]

min_exp=0

for exp in expenses:

    if exp<min_exp:

        min_exp=exp

print("Minimum_exp=",min_exp)        

#avg
#most frequency exp



