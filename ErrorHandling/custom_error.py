



# "rasie" keyword is used for our own error creating(custom error)



def review(rating):

    if rating<0:

        raise Exception("too low")
    
    elif rating>10:

        raise Exception("too high")
    
    else:

        print("done!")

# review(12)

# print("Hello")

# print("Hai")

try:

    review(12)

except Exception as e:

    print(e) 

print("Hello")

print("Hai")      








#"assert"  whenever ther is a error in the condition there will provide assertion error


def poll(age):

    assert age>18,"Invalid age"

    print("voted")

try:    

  poll(14)    

except Exception as e:

    print(e)  







def review(rating):

    assert rating>0,"too low"

    assert rating in range(0,11),"too high"

    print("rated")    