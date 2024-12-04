

text="ABABBCCDDEH"

# character_frequence

character_frequence={ch:text.count(ch) for ch in text}

print(character_frequence) #{'A': 2, 'B': 3, 'C': 2, 'D': 2, 'E': 1}



# print non recursive elements

for k,v in character_frequence.items():

    if v==1:

        print(k)


# list comprehnsion


non_frequence_elements=[k for k,v in character_frequence.items() if v==1 ]        

print(non_frequence_elements)