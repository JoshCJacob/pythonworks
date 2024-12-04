

words=["hai","hello","hai","hello","hai"]


words_count={}  #empty set

# iteration words

for w in words:

    if w in words_count:  #if hai in word_count

        words_count[w]+=1   #each word count the value

    else:

        words_count[w]=1

print(words_count)            






text="ABBACB"
# A:2
# B:3
# c:1

# for ch in text:
    #  print(ch)

char_count={}

for ch in text:

    if ch in char_count:

        char_count[ch]+=1

    else:

        char_count[ch]=1

print(char_count)            


# first recursive character


