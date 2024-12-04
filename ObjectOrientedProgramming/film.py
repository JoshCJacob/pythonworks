

# # movie

# # title,rating,runtime,director,genre,year


# # ARM
# # KGF

# class Movie:

#     title:str

#     rating:int

#     run_time:int

#     director:str

#     genre:str

#     year:int
    
#     # self - current instance followed by it

#     def set_movie(self,title,rating,runtime,director,genre,year):

#      self.title=title

#      self.rating=rating

#      self.run_time=runtime

#      self.director=director

#      self.genre=genre
    
#      self.year=year

#     # we can prin t the particular movie detailes printed it
#     def display(self):

#        print(self.title,self.director,self.run_time,self.genre,self.year)

# film_instance1=Movie()

# film_instance1.set_movie("ARM","jithin lal",120,"Fantasy",2024)        

# film_instance1.display()



class Movie:

    title:str

    rating:int

    run_time:int

    director:str

    genre:str

    def set_Movie(self,title,rating,run_time,director,genre):

        self.title=title

        self.rating=rating

        self.run_time=run_time

        self.director=director

        self.genre=genre


    def display(self):

        print(self.title,self.rating,self.run_time,self.director,self.genre)


movie_instance1=Movie()

movie_instance2=Movie()

movie_instance1.set_Movie("ARM",4.5,"2.30HRS","JITHIN LAL","ADVENTURE")

movie_instance2.set_Movie("KGF",4.8,"2.40hrs","PRASANTH NEEL","ACTION")

movie_instance1.display()

movie_instance2.display()