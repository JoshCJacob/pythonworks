

f=open("C:\\Users\\joshc\\OneDrive\\Desktop\\Pythonworks\\Dataset\\sentence.txt","r")

words=[]

for line in f:

    line=line.rstrip("\n")

    all_words=line.split(" ")

    for w in all_words:

        words.append(w)

print(words)        



word_count={w:words.count(w) for w in words}

# print(word_count)



# sorted_word_count=sorted(word_count,key=lambda k:word_count.get(k),reverse=True)

# print(sorted_word_count)


# value_key=[[v,k]for k,v in word_count.items()]

# print(sorted(value_key,reverse=True))


nested_word=[[v,k]for v,k in word_count.items()]

print(sorted(nested_word,reverse=True))





sample={"banana":20,"mango":80,"orange":75,"apple":200}

nested_list=[[v,k]for k,v in sample.items()]

print(sorted(nested_list,reverse=True))