

from re import finditer

text="abbbabababbabaaaab"
#     012345678901234567

pattern="a{2}"

pattern="a{1,3}" #min=1  max=3

pattern="a*"  #* any number including 0

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())