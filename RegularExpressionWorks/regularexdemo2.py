

from re import finditer

text="I have 3 cars,2 bike and 1 Cycle"
#     01234567890123456789012345678901

pattern="[a-z]"  #chck for all lowercase alphabets

pattern="[a-zA-Z]"  #chck all alphabets

pattern="[0-9]" #chck for digits

pattern="[a-zA-Z0-9]" #chck for alphanumerics

patterns="[^a-zA-Z0-9]" #special characters

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),"==>",obj.group())