# new function in python is enumerate(iteration)<=index,object




#sample input

arr=[100,200,300,400,500,600,700,800]
#     0   1   2   3   4   5   6   7


# odd_position_elements=[arr[i]for i in range(0,len(arr)) if i%2!=0] #odd position of index

odd_position_elements=[num for index,num in enumerate(arr) if index%2!=0]

odd_position_elements.reverse()

print(odd_position_elements) #[800,600,400,200]
#                               0   1   2   3
