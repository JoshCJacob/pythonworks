text="The quick brown fox jumps over the lazy dog".casefold()

# pangram
# not pangram


alphabets="abcdefghijklmnopqrstuvwxyz"

is_pangram=True

for ch in alphabets:

    if ch not in text:

        is_pangram=False

        break

print(is_pangram) 






source_word="silent"

target_word="listen"

#anagram