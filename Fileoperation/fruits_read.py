

f=open("C:\\Users\\joshc\\OneDrive\\Desktop\\Pythonworks\\Dataset\\fruits.txt","r")


fruits=[]

for line in f:

    fruits.append(line.rstrip("\n"))

print(fruits)    
