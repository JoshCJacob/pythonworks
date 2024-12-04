


def add_number(num1,num2):

    return num1+num2









def add_number(num1,num2,num3):

    return num1+num2+num3

print(add_number(100,200,300))






def add_number(*args):

    return sum(args)

print(add_number(10,20))

print(add_number(10,20,30))

print(add_number(10,20,30,40,50))


# create a function that accept any number of arguments and return second maximum number


def second_max_number(*args):

    sorted_number=sorted(args,reverse=True)

    # print(sorted_number)

    return sorted_number[1]


print(second_max_number(10,11,12,13))

print(second_max_number(10,11,12,13,14,15))






def display_mobile_data(**kwargs):

    print(kwargs.get("name"))

    print(kwargs.get("price"))

display_mobile_data(name="oneplus",price=32000,display="amoled")





# calculator(10,20,30,operation="+")

# calculator(10,11,12,13,14,operation="*")




def calculator(*args,**kwargs):

    if kwargs.get("operation")=="+":

        return sum(args)
    
    if kwargs.get("operation")=="*":

        result=1

        for num in args:

            result=result*num

        return result

print(calculator(10,20,30,operation="*"))
#                        ,operation="+"




# def student_info(45,43,44,operation="avg")

# def student_info(45,43,44,operation="total")



def student_info(*args,**kwargs):

    if kwargs.get("operation")=="total":

        return sum(args)
    
    if kwargs.get("operation")=="avg":

        return sum(args)/len(args)
    
print(student_info(45,43,44,operation="total"))





# def sort_numbers(1,2,6,4,15,11,reverse="True") desc

# def sort_numbers(1,2,6,4,15,11,reverse="False") asec


def sort_numbers(*args,**kwargs):

    if kwargs.get("reverse")=="True":

        return sorted(args,reverse=True)
    
    if kwargs.get("reverse")=="False":

        return sorted(args,reverse=False)
    
print(sort_numbers(1,2,6,4,15,11,reverse="False"))   
#                                         "True" 







    