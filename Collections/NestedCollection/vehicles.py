

cars=[
    {
     "id":1,"name":"fronx","price":1200000,"brand":"nexa",
     "colors":["red","blue","white"],
     "transmissions":["manuel","amt","cvt"]
     },
    {
     "id":2,"name":"baleno","price":1100000,"brand":"nexa",
     "colors":["grey","blue","white"],
     "transmissions":["manuel","amt","cvt"]
     },
    {
     "id":3,"name":"3xo","price":900000,"brand":"mahindra",
     "colors":["red","white","black"], 
     "transmissions":["amt","cvt"]
     },
    {
     "id":4,"name":"punch","price":700000,"brand":"tata",
     "colors":["red","blue","white","green"],
     "transmissions":["manuel","cvt"]
     },
    {
     "id":5,"name":"nexon","price":1400000,"brand":"tata",
     "colors":["red","white"],
     "transmissions":["manuel","amt","cvt"]},
    {
     "id":6,"name":"kiger","price":1000000,"brand":"renault",
     "colors":["blue","white"],
     "transmissions":["manuel","cvt","dct"]},
    {
     "id":7,"name":"taigun","price":2300000,"brand":"volkswagon",
     "colors":["red","blue","white"],
     "transmissions":["manuel","cvt","torque"]
     },
]


#  print count of vehicles

print(f"total vehicles=>{len(cars)}")

# print available colors of baleno

baleno_colors=[c.get("colors")for c in cars if c.get("name")=="baleno"]

print(baleno_colors[0])  #the [0]is add it with index of it

# print all brands

all_brand=[c.get("brand")for c in cars]

# all_brand={c.get("brand")for c in cars}
# print(all_brand)

print(set(all_brand))


# print car names available in amt transmission

amt_cars=[c.get("name")for c in cars if "amt" in c.get("transmissions")]

print(amt_cars)

# cars available in blue color

blue_color_cars=[c.get("name")for c in cars if "blue" in c.get("colors")]

print(blue_color_cars) 


# print all transmissions

all_transmission={t for c in cars for t in c.get("transmissions")}

print(all_transmission)


# print all colors

all_colors={color for c in cars for color in c.get("colors")}

print(all_colors)


# most popular color

# {blue:4,red:2}



# costly car

costly_car=max(cars,key=lambda d:d.get("price"))

print(costly_car.get("name"))

# car with minimum cost

minimum_cost=min(cars,key=lambda d:d.get("price"))

print(minimum_cost.get("name"))

# sort wrt price

sorted_car=sorted(cars,key=lambda d:d.get("price"),reverse=True)

sorted_car_name={c.get("name"):[c.get("price"),c.get("brand")] for c in sorted_car}

print(sorted_car_name)






 

