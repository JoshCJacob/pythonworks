#lst=[]
# tp=()


#set


st=set() #empty set               #st={} #dictionary


st={10,20,30}

print(st)



st={10,20,10,30,40,20}

print(st)


st={10,20,30,10,20,"hai","hello",True}

print(st)  #set doesnot support indexing


#add()

colors={"purple","green","orange"}

colors.add("red")

print(colors)



#intersection()


st1={10,20,30,40,50}

st2={10,20,40,60,70}

intersection_set=st1.intersection(st2)

print(intersection_set)


#union()


union_set=st1.union(st2)

print(union_set)


#differnce()


st1={10,20,30,40,50}

st2={10,20,40,60,70}

difference_set=st1.difference(st2)

print(difference_set)


#remove()

st={10,20,30,40,50}

st.remove(40)

print(st)


#lst to set


colors=["purple","green","orange"]

colors_set=set(colors)

print(colors_set)



#issubset()

st1={1,2,3}

st2={1,2,3,4,5}

print(st1.issubset(st2)) 



#issuperset()


print(st2.issuperset(st1))



#symmetric_difference()  - AUB-A^B


st1={1,2,3,10,20}

st2={1,2,3,4,5}

symmetric_difference=st1.symmetric_difference(st2)

print(symmetric_difference)



# update()


st1={1,2,3,10,20}

st2={1,2,3,4,5}

st1.update(st2)

print(st1)










