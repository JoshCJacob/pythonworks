


read_path=open("C:\\Users\\joshc\\OneDrive\\Desktop\\Pythonworks\\Dataset\\words.txt")

write_path=open("C:\\Users\\joshc\\OneDrive\\Desktop\\Pythonworks\\Dataset\\palindrome.txt","w")

for line in read_path:

    word=line.rstrip("\n")

    reversed_word=word[::-1]

    if word==reversed_word:

        write_path.write(word+"\n")

read_path.close()

write_path.close()

    

