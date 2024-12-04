


arr=[2,3,4,5,6,7,8]

squares=[]

for num in arr:

    result=num**2

    squares.append(result)

print(squares)


# list comprehension
#[ return , iteration , condition]

arr=[2,3,4,5,6,7,8]

#squares

squares=[num**2 for num in arr] 
#        return    iteration

print(squares)


#cubes

cubes=[num**3 for num in arr]

print(cubes)

#add ten

add_ten=[num+10 for num in arr]

print(add_ten)

#condtion method in even and odd

even_number=[num for num in arr if num%2==0]
#            return   iteration   condition 
print(even_number)


odd_number=[num for num in arr if num%2!=0]

print(odd_number)

num_gt_five=[num for num in arr if num >5]

print(num_gt_five)



#read new list num+1 if num>5 else num-1

arr=[2,3,4,5,6,7,8]

map_num=[num+1 if num>5 else num-1 for num in arr]
#                return              iteration



text=["apple","iphone","orange","potatto"]

#word staring with vowels

vowel_words=[w for w in text if w[0] in ['a','e','i','o','u]']]

print(vowel_words)

consonant_words=[w for w in text if w[0] not in ['a','e','i','o','u']]

# print(consonant_words)

#longest word

long=max([len(w) for w in text])

# print(long)

longest_word=[w for w in text if len(w)==long]

print(longest_word)





#mapping - (no condition)
#filter - (condition)
#reduce - max() min() sum()