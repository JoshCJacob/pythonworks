# read number 15
# print fizz if num /3
# print buzz if num/5
# print fizzbuzz if num /15
# print default invalid number


number=int(input("Enter the Number:"))


if number%15==0:

    print("FIZZBUZZ.....")

elif number%5==0:

    print("BUZZ")

elif number%3==0:

    print("FIZZ")  

else:

    print("Invalid Number")        