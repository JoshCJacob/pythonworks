
# #half pyramid



for row in range(5,0,-1):

    for col in range(1,row+1):

        print("*",end="\t")

    print("")    






# #inverted half pyramid



for row in range(1,6):

    for col in range(5,row-1,-1):

        print("*",end="\t")

    print()    





# #fully pyramid



for row in range(1,7):

    for sp in range(1,7-row):

        print(" ",end="")

    for col in range(1,row+1):

        print("* ",end="")

    print()      





#inverted fully pyramid



for row in range(1,7):

    for sp in range(1,7-row):

        print(" ",end="")


    for col in range(1,):

       print("*",end="")

print()    