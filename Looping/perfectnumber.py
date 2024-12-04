
#num

#1,num


#write a pgm to chck a number is perfect or not

num=int(input("Enter the number:"))


total=0


for i in range(1,num):

    if num%i==0:

        total+=i

print("Perfect Number" if total==num else "Not Perfect Number")        




