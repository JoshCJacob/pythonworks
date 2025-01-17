

# true if year is leap year else return false

def is_leap_year(year):

    if year<0:

        return False

    if year%100!=0 and year%4==0 or year%100==0 and year%400==0:

        return True
    
    else:

        return False
    
def test_is_leap_year():

    assert is_leap_year(2024)==True,"non century year chck failed"

    assert is_leap_year(2025)==False,"Invalid non century year chck failed"    
     
    assert is_leap_year(2000)==True,"century leap year chck failed"

    assert is_leap_year(1900)==False,"Invalid century year chck failed"

    assert is_leap_year(-2029)==False,"Invalid year chck failed"

try:
    test_is_leap_year()

    print("test case pass")

except Exception as e:

    print("test failed",e)        