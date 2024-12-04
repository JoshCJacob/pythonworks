
# from re import finditer

# f=open("C:\\Users\\joshc\\OneDrive\\Desktop\\Pythonworks\\regular_exp_fireworks\\url_smaple.txt")

# for line in f:

#     sample_url=line.rstrip("\n")

#     pattern="https?://[\w\S./]+"

#     matcher=finditer(pattern,sample_url)

#     for obj in matcher:

#         print(obj.group())






from re import findall

f=open("C:\\Users\\joshc\\OneDrive\\Desktop\\Pythonworks\\regular_exp_fireworks\\url_smaple.txt")

content=f.read()   #for using read all file in the content

# print(content)

pattern="https?://[\w\S./]+"

urls=findall(pattern,content)

for url in urls:

    print(url)



