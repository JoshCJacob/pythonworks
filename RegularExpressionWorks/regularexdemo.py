

from re import finditer

text="fatcattrunsveryfasttocaththerat"

matcher=finditer("at",text)  #(start,group)

for obj in matcher:

    print(obj.start(),obj.group())





