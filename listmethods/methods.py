# class list:

#     def append(self):
      
#      def pop(self,index) 
 
#       def insert(self,index,object)
 
#        def index(self,object)  

#         def copy(self)

#         def sort(self)
            
#           def sort(self,reverse=false)
       

#append


colors=["red","green","blue"]

#colors.append() insert  new object end of the list

colors.append("yellow")

print(colors)




#pop



colors=["red","green","blue","yellow"]

#colors.pop() remove the last object from list and returns it

popped_element=colors.pop()

print(colors)



colors.pop(1)#choose the element removing

print(colors)



#insert


colors=["red","green","blue","yellow"]

colors.insert(1,"violet")#spectific location adding the object

print(colors)



#index

colors=["red","green","blue","yellow"]

red_index=colors.index("red")#returns index of first occurance red

print(red_index)





#copy

josh_fvt_colors=["red","white","green","blue"]

mammokka_fvt_colors=josh_fvt_colors.copy()

mammokka_fvt_colors.pop()

print("ikaa",mammokka_fvt_colors)

print("josh",josh_fvt_colors)




#sort


lst=[2,3,6,7,8,9,7]


lst.sort() #ascending order

lst.sort(reverse=True) #decending order

print(lst)


#extend   (merge)


fruits=["apple","mango","orange"]

products=["onion","brinjal","potato"]

products.extend(fruits)

print(products)



#reverse

fruits.reverse()

print(fruits)


#count

lst=[10,20,10,30,40]

ten_occurance=lst.count(10)

print(ten_occurance)












