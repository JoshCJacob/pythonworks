

source_word="CHICKEN"

target_word="HEN"


# step 1 to find the source_word character count

# create empty dictionary

# character_count={}

# # iteration 

# for ch in source_word:

#     if ch in character_count:

#         character_count[ch]+=1
#     else:

#         character_count[ch]=1

# print(character_count)    



character_count={ch:source_word.count(ch) for ch in source_word}

is_kangaroo=True

for ch in target_word:

    if ch in character_count and character_count.get(ch)>0:

        character_count[ch]=-1

    else:

        is_kangaroo=False

        break

print(is_kangaroo)            



