
# finditer" for exctly be with each line not by word
# for finditer using obj


from re import finditer

f=open("C:\\Users\\joshc\\OneDrive\\Desktop\\Pythonworks\\regular_exp_fireworks\\social_post.txt")

for line in f:

    word=line.rstrip("\n")

    pattern="#\w+"

    matcher=finditer(pattern,word)

    for obj in matcher:

        print(obj.group())





    