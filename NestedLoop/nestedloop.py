#Good $$ Afternoon      All


print("Good",end="$$")

print("Afternoon",end="\t") #\t=Tab

print("All")






for row in range(1,6):

    for col in range(1,4):

        print("*",end="\t")

    print()     







for row in range(1,7):

    for col in range(1,row+1):

        print("$",end="\t")

    print()   









for row in range(1,6):

    for col in range(1,row+1):

        print(row,end="\t")

    print()    








for row in range(5,0,-1):

    for col in range(1,row+1):

        print("*",end="\t")

    print("")    










for row in range(1,6):

    for col in range(5,row-1,-1):

        print("*",end="\t")

    print()    