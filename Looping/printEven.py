

#print all numbers from start to end

#read(start,end)

start=int(input("enter the start number:"))

end=int(input("enter the end limit:"))


for num in range(start,end+1,1):     

    print(num)



#for incr & decr order


if start<end:

    for num in range(start,end+1,1):

        print(num)


else:

    for num in range(start,end-1,-1):

        print(num)                 

     

