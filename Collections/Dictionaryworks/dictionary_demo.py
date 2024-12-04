

# dictionary {}

# key:value pairs


#create a dictionary product with keys id,title,price,brand

product={"id":115,"title":"Watch","price":20000,"brand":"ROLEX"}

print(product["price"])

# update product price 30k

product["price"]=30000

print(product)


product["Year"]="Since 1929"

print(product)


product["Offer"]=5

print(product)



# chck key is exit or not

# exist
# not exisit

if "brand" in product:

    print("exist")

else:

    print("not exist")



# add offer as 10 if offer exist else add after as 20


if "offer" in product:

    product["offer"]=10


else:

    product["offer"]=20


print(product)        
