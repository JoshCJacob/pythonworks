

f=open("C:\\Users\\joshc\\OneDrive\\Desktop\\Pythonworks\\Dataset\\frameworks.txt","a") #"a" for append  

frame_works=["wordpress","springboot","oodo","fastapi"]

for fw in frame_works:

    f.write(fw+"\n")

f.close()    

