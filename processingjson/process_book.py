

from json import load

f=open("C:\\Users\\joshc\\OneDrive\\Desktop\\Pythonworks\\Dataset\\books.json")

data=load(f)

# for book in data:

#     print(book)


all_titles=[book.get("title") for book in data] 

# print(all_titles)


#  book with pages<250

page_filter=[book.get("title")for book in data if book.get("pages") <250]

# print(page_filter)


# print all genre

all_genres=[book.get("genre")for book in data]

# print(set(all_genres))


genre_count={genre:all_genres.count(genre)for genre in all_genres}

# print(genre_count)


# print costly book

costly_books=[book.get("title")for book in data if book.get("price") >17 ]

print(costly_books)