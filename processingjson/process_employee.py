
from json import load

f=open("C:\\Users\\joshc\\OneDrive\\Desktop\\Pythonworks\\Dataset\\employee.json")

data=load(f)

for emp in data:

    print(emp)