
# create dictionary  employee with keys eid,name,salary,department,experience

employee={"eid":123,
          "name":"Josh",
          "salary":20000,
          "depatment":"software developer",
          "experience":6
          }

print(employee["salary"])


# add contact as 2345678

employee["contact"]=2345678

print(employee)


# if experience>5 update employee salary as current_salary+=30000 else current_saklary+=2000


if employee["experience"]>5:

    employee["salary"]+=30000

else:

    employee["salary"]+=2000

print(employee)        



# add role as SDE if exp>5 else add role as JDE


if employee["experience"]>5:

    employee["role"]="SDE"

else:

    employee["role"]="JDE"

print(employee)        




