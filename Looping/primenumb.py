number=int(input("enter a number:"))

if number<2:

    is_prime=False

else:

    is_prime=True

    for i in range(2,number):  #i=2,3,4,5,6,7,8

        if number%i==0:

            is_prime=False

            break

print(is_prime)            