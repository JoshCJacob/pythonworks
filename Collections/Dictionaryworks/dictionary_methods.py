# methods


# get() 

employee={"id":289,"name":"JOSH","department":"HR","age":23,"salary":30000}
 
print(employee.get("department")) #get(key)
# invalid key return none


# pop(key)  

employee.pop("salary")

print(employee)



# return all keys =>keys()

for k in employee.keys():

    print(k)



# fetch all values =>values()

for v in employee.values():

    print(v)



#fetch key and values =>items()

for k,v in employee.items():

    print(k,v)