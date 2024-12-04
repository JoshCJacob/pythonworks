

arr=[10,20,30,40,2,3]

# {10:100,20:400,,,}

result={} # create empty dictionary

for num in arr: #taken the numbers in array each one in form num

    square=num**2  #square the num

    result[num]=square  


print(result)




# dictionary comprehension


arr=[10,20,30,40,2,3]

# result={key:value iteration condition}

result={num:num**3 for num in arr}

print(result)




# even_squares

# odd_cubes


arr=[10,20,30,40,2,3,5,7,8]

even_squares={num:num**2 for num in arr if num%2==0}

print(even_squares)


odd_cubes={num:num**3 for num in arr if num%2!=0}

print(odd_cubes)



# frequence of numbers


arr=[10,20,30,40,2,3,5,7,8,10,30]

frequence_count={num:arr.count(num) for num in arr}

print(frequence_count)

