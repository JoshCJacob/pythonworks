

text="ABAABBC"

# most recursive character

# non recursive character



def get_count(chr):

    return text.count(chr)

most_frequent_charcter=max(text,key=get_count)

print(most_frequent_charcter)


least_recursive_character=min(text,key=get_count)

print(least_recursive_character)