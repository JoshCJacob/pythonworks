


text="this is a simple programming question to find with word maximum number of characters "

words=text.split(" ")

# words='this', 'is', 'a', 'simple', 'programming', 'question', 'to', 'find', 'with', 'word', 'maximum', 'number', 'of', 'characters', '']

# def get_length(w):

#     return len(w)

# print(max(words,key=get_length))

def get_length(w):

    return len(w)

srt_words=sorted(words,key=get_length,reverse=True)

print(srt_words)




text="this is a simple programming question to find with word maximum number of characters "

# most recursive word

words=text.split(" ")

def get_count(w):

    return words.count(w)

most_frequent_word=max(words,key=get_count)

print(most_frequent_word)








