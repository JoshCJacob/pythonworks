

arr=[
    1,2,
    [10,20],
    [1,2,5,[10,3]],
    100
]

# find the largest list


# list_object=[]

# for item in arr:

#     if isinstance(item,list):

#         list_object.append(item)

# print(list_object)        


list_object=[item for item in arr if isinstance(item,list)]

# print(list_object)

print(max(list_object,key=len))



